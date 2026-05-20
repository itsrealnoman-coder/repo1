#!/usr/bin/env python3
"""Quality checks for the GlowPick Baby Boy Clothes article per the build prompt."""
import re
from pathlib import Path

HTML = Path("/projects/sandbox/repo1/best-baby-boy-clothes-2026-article-v1.html").read_text()

ASINS = [
    "B088NTLG5C", "B0B6D8GVR1", "B07QPQLW34", "B075F8WNR1", "B0C7HFR853",
    "B0C7HJ2BY2", "B0D73L76HR", "B08BV2M73D", "B08X6GJGCS", "B0G52H9VQP",
]

checks = []

def add(name, ok, detail=""):
    icon = "OK" if ok else "FAIL"
    checks.append((ok, name, detail))
    print(f"[{icon}] {name}{(' -- ' + detail) if detail else ''}")

# 1. WP blocks (post-comments-form + comments)
pcf = HTML.count("<!-- wp:post-comments-form /-->")
wpc = HTML.count("<!-- wp:comments /-->")
add("WP blocks: post-comments-form + comments", pcf == 1 and wpc == 1, f"post-comments-form: {pcf}, comments: {wpc}")

# 2. Product sections: 10/10
prod_count = len(re.findall(r'<div id="review-\d+">', HTML))
add("Product sections: 10/10", prod_count == 10, f"found {prod_count}")

# 3. Buy on Amazon buttons in TABLE only (10) + none after Our Take
buy_buttons = HTML.count('class="dyu-btn-amazon"')
buy_after_take = 0
for m in re.finditer(r'<div class="dyu-our-take">.*?</div>\s*</div>', HTML, re.DOTALL):
    if 'dyu-btn-amazon' in m.group(0):
        buy_after_take += 1
add("Buy on Amazon buttons: 10 (table only)", buy_buttons == 10 and buy_after_take == 0,
    f"total buttons: {buy_buttons}, after Our Take: {buy_after_take}")

# 4. Table images clickable with affiliate link
table_section = re.search(r'<div class="dyu-table-wrapper">.*?</div>', HTML, re.DOTALL)
table_html = table_section.group(0) if table_section else ""
clickable_imgs = len(re.findall(r'<a href="https://www\.amazon\.com/dp/[^"]*tag=delightfulyou-20"[^>]*><img class="dyu-table-img"', table_html))
add("Table images clickable with affiliate link: True (10/10)", clickable_imgs == 10, f"found {clickable_imgs}")

# 5. Table ratings: decimal + review count format
rating_format = len(re.findall(r'<span class="dyu-stars">[^<]+</span>\s*\d\.\d', HTML))
review_count_format = len(re.findall(r'class="dyu-review-count">[\d,]+\s+reviews</span>', HTML))
add("Table ratings: decimal stars + review count", rating_format == 10 and review_count_format == 10,
    f"rating cells: {rating_format}, review-count cells: {review_count_format}")

# 6. Badge = remark only (no number in badge)
badges = re.findall(r'<span class="dyu-rank-badge">([^<]+)</span>', HTML)
def strip_entities(s):
    return re.sub(r'&#\d+;', '', s)
no_number_in_badge = all(not re.search(r'\b\d+\b', strip_entities(b)) for b in badges)
add("Badge = remark only (no number in badge)", len(badges) == 10 and no_number_in_badge,
    f"badges: {len(badges)}, sample: {badges[0] if badges else 'none'}")

# 7. Number in h4: True (10/10)
h4_with_number = len(re.findall(r'<h4>\d+\.\s', HTML))
add("Number in h4: True (10/10)", h4_with_number == 10, f"found {h4_with_number}")

# 8. Product order: Best Overall at #1
first_badge = badges[0] if badges else ""
add("Product order: Best Overall at #1", "Best Overall" in strip_entities(first_badge), f"first badge: {first_badge}")

# 9. No inline onclick anywhere
onclick_count = len(re.findall(r'\bonclick\s*=', HTML, re.IGNORECASE))
add("No inline onclick anywhere", onclick_count == 0, f"onclick attributes: {onclick_count}")

# 10. TOC arrows/symbols: False
toc_button = re.search(r'<button class="dyu-toc-toggle"[^>]*>(.+?)</button>', HTML, re.DOTALL)
toc_text = toc_button.group(1) if toc_button else ""
arrow_chars = re.findall(r'[\u25B6\u25BC\u25BA\u2192\u2193\u25BD\u25B2+]', toc_text)
add("TOC arrows/symbols: False", len(arrow_chars) == 0 and "&#x25" not in toc_text,
    f"toc text: '{toc_text.strip()}'")

# 11. Verdict section: False
verdict_count = len(re.findall(r'<h4[^>]*>[^<]*verdict[^<]*</h4>', HTML, re.IGNORECASE))
add("Verdict section: False", verdict_count == 0, f"verdict h4 found: {verdict_count}")

# 12. Sticky columns 1+2: True
sticky1 = "td:nth-child(1) { position: sticky" in HTML
sticky2 = "td:nth-child(2) { position: sticky" in HTML
add("Sticky columns 1+2: True", sticky1 and sticky2)

# 13. No ::after fade gradient
fade = re.search(r'\.dyu-table-wrapper[^{]*::after', HTML)
add("No ::after fade gradient: True", fade is None)

# 14. Scroll hint centered above table
scroll_hint = re.search(r'<p class="dyu-scroll-hint"[^>]*>.*?</p>\s*<div class="dyu-table-wrapper">', HTML, re.DOTALL)
add("Scroll hint centered above table: True", scroll_hint is not None)

# 15. Gold border ONLY on .dyu-hostinger-wrap
gold_borders = re.findall(r'border:[^;]*#d4a843', HTML)
gold_block_no_border = ".dyu-gold-block { border: none" in HTML
add("Gold border only on .dyu-hostinger-wrap: True", len(gold_borders) == 1 and gold_block_no_border,
    f"gold border declarations: {len(gold_borders)}")

# 16. .dyu-gold-block border:none
add(".dyu-gold-block border:none: True", ".dyu-gold-block { border: none" in HTML)

# 17. Hostinger block format
hostinger_blocks = re.findall(r'<!-- wp:hostinger-affiliate-plugin/block .+? /-->', HTML)
correct_format = sum(
    1 for b in hostinger_blocks
    if '"display_type":"multiple_product_list"' in b and '"list_layout":"list_with_description"' in b
)
add("Hostinger block format: multiple_product_list + list_with_description",
    correct_format == 10, f"correct format: {correct_format}/10")

# 18. All 10 ASINs present
asins_in_html = sum(1 for a in ASINS if a in HTML)
add("All 10 ASINs present", asins_in_html == 10, f"present: {asins_in_html}/10")

# 19. Affiliate tag delightfulyou-20 on all Amazon links
buy_button_links = re.findall(r'href="(https://www\.amazon\.com/dp/[^"]+)"\s+target="_blank"\s+rel="nofollow', HTML)
all_tagged = all("tag=delightfulyou-20" in u for u in buy_button_links)
add("Affiliate tag on all Amazon links", all_tagged and len(buy_button_links) >= 10,
    f"affiliate links: {len(buy_button_links)}, all tagged: {all_tagged}")

# 20. rel="nofollow sponsored noopener" on all Amazon links
nofollow_count = HTML.count('rel="nofollow sponsored noopener"')
add('rel="nofollow sponsored noopener" on all Amazon links', nofollow_count >= 20,
    f"count: {nofollow_count}")

# 21. Author popup: hover + click trigger, white card, red name, outlined buttons
author_popup_present = ".dyu-author-popup" in HTML
hover_trigger = ".dyu-author-name-btn:hover .dyu-author-popup" in HTML
click_trigger = ".dyu-author-name-btn.active .dyu-author-popup" in HTML
red_name = ".dyu-author-popup-name { font-weight: 700; color: #c0392b" in HTML
outlined_btn = ".dyu-author-popup-link { display: inline-flex" in HTML and "border: 1.5px solid" in HTML
add("Author popup: hover + click trigger, white, red name, outlined links",
    author_popup_present and hover_trigger and click_trigger and red_name and outlined_btn)

# 22. Evidence Based button inside author block, right-aligned, teal on hover
evidence_in_author = re.search(
    r'<div class="dyu-author-block">\s*<div class="dyu-evidence-wrapper">', HTML
)
right_align = "justify-content: flex-end" in HTML
teal_hover = ".dyu-evidence-wrapper:hover .dyu-evidence-btn { background: #148f77" in HTML
add("Evidence Based: inside author block, right-aligned, teal on hover",
    evidence_in_author is not None and right_align and teal_hover)

# 23. Disclosure inside Evidence Based tooltip ONLY
disclosure_in_tooltip = "affiliate links" in HTML
bottom_section = HTML[-2000:]
bottom_disclosure = "affiliate" in bottom_section.lower() and "disclosure" in bottom_section.lower()
add("Disclosure: inside Evidence Based tooltip only",
    disclosure_in_tooltip and not bottom_disclosure)

# 24. No "Last Updated" date
no_last_updated = not re.search(r'last\s+updated', HTML, re.IGNORECASE)
add("No Last Updated date", no_last_updated)

# 25. No standalone disclosure paragraph at bottom
add("No standalone disclosure paragraph at bottom", not bottom_disclosure)

# 26. GlowPick (not DelightfulYou.com) in blue helpful box
helpful_box = re.search(r'<div class="dyu-helpful-box">.+?</div>', HTML, re.DOTALL)
hb_text = helpful_box.group(0) if helpful_box else ""
add("GlowPick in blue helpful box", "GlowPick" in hb_text and "DelightfulYou.com" not in hb_text)

# 27. table-only.html and faq-only.html checks
table_only = Path("/projects/sandbox/repo1/table-only.html").read_text()
faq_only = Path("/projects/sandbox/repo1/faq-only.html").read_text()

table_has_scroll_hint_element = '<p class="dyu-scroll-hint"' in table_only
table_ok = (
    "overflow-x: visible" in table_only and
    not table_has_scroll_hint_element and
    "min-width: unset" in table_only
)
add("table-only.html: full-width, no scroll, no scroll-hint", table_ok)

faq_q_elements = faq_only.count('<p class="dyu-faq-q">')
faq_ok = (
    "dyu-faq-item" in faq_only and
    faq_q_elements == 6 and
    "dyu-article" in faq_only
)
add("faq-only.html: styled, all 6 FAQs", faq_ok, f"faq-q elements: {faq_q_elements}")

# Additional checks
# 10 Hostinger blocks
add("10 Hostinger blocks present", len(hostinger_blocks) == 10, f"found: {len(hostinger_blocks)}")

# 6 FAQ items
faq_count = len(re.findall(r'<p class="dyu-faq-q">', HTML))
add("FAQ: 6 questions", faq_count == 6, f"found: {faq_count}")

# 5 author rows
author_rows = len(re.findall(r'<div class="dyu-author-row">', HTML))
add("Author rows: 5", author_rows == 5, f"found: {author_rows}")

# Summary
total = len(checks)
passed = sum(1 for c in checks if c[0])
print(f"\n{'='*60}")
print(f"PASSED: {passed}/{total}")
print(f"{'='*60}")
if passed < total:
    print("\nFAILED CHECKS:")
    for ok, name, detail in checks:
        if not ok:
            print(f"  - {name}: {detail}")
