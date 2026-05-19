#!/usr/bin/env python3
"""Quality checks for the GlowPick article per the build prompt."""
import re
from pathlib import Path

HTML = Path("/projects/sandbox/repo1/best-body-lotions-2026-article-v1.html").read_text()

ASINS = [
    "B0FKC23886", "B08KT2Z93D", "B0CRQYQBZ4", "B08KQ9RNMD", "B00TTD9BRC",
    "B01HTJTV4U", "B001459IEE", "B07DJPC8JB", "B0009F3O8Q", "B0BVPH918S",
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
# Check for buy buttons appearing after "Our Take" in any product section
buy_after_take = 0
for m in re.finditer(r'<div class="dyu-our-take">.*?</div>\s*</div>', HTML, re.DOTALL):
    if 'dyu-btn-amazon' in m.group(0):
        buy_after_take += 1
add("Buy on Amazon buttons: 10 (table only)", buy_buttons == 10 and buy_after_take == 0,
    f"total buttons: {buy_buttons}, after Our Take: {buy_after_take}")

# 4. Table ratings: decimal + review count format
rating_format = len(re.findall(r'<span class="dyu-stars">[^<]+</span>\s*\d\.\d', HTML))
review_count_format = len(re.findall(r'class="dyu-review-count">[\d,]+\s+reviews</span>', HTML))
add("Table ratings: decimal stars + review count", rating_format == 10 and review_count_format == 10,
    f"rating cells: {rating_format}, review-count cells: {review_count_format}")

# 5. Badge = remark only (no number in badge)
badges = re.findall(r'<span class="dyu-rank-badge">([^<]+)</span>', HTML)
# Strip HTML entities (emoji codepoints) before checking for digits
def strip_entities(s):
    return re.sub(r'&#\d+;', '', s)
no_number_in_badge = all(not re.search(r'\b\d+\b', strip_entities(b)) for b in badges)
add("Badge = remark only (no number in badge)", len(badges) == 10 and no_number_in_badge,
    f"badges: {len(badges)}, sample: {badges[0] if badges else 'none'}")

# 6. Number in h4: True (10/10)
h4_with_number = len(re.findall(r'<h4>\d+\.\s', HTML))
add("Number in h4: True (10/10)", h4_with_number == 10, f"found {h4_with_number}")

# 7. No inline onclick anywhere
onclick_count = len(re.findall(r'\bonclick\s*=', HTML, re.IGNORECASE))
add("No inline onclick anywhere", onclick_count == 0, f"onclick attributes: {onclick_count}")

# 8. TOC arrows/symbols: False (no triangles, arrows, plus/minus in toggle button)
toc_button = re.search(r'<button class="dyu-toc-toggle"[^>]*>(.+?)</button>', HTML, re.DOTALL)
toc_text = toc_button.group(1) if toc_button else ""
arrow_chars = re.findall(r'[\u25B6\u25BC\u25BA\u2192\u2193\u25BD\u25B2+]', toc_text)
add("TOC arrows/symbols: False", len(arrow_chars) == 0 and "&#x25" not in toc_text,
    f"toc text: '{toc_text.strip()}'")

# 9. Verdict section: False (no <h4> with 'verdict')
verdict_count = len(re.findall(r'<h4[^>]*>[^<]*verdict[^<]*</h4>', HTML, re.IGNORECASE))
add("Verdict section: False", verdict_count == 0, f"verdict h4 found: {verdict_count}")

# 10. Sticky columns 1+2: True
sticky1 = "td:nth-child(1) { position: sticky" in HTML
sticky2 = "td:nth-child(2) { position: sticky" in HTML
add("Sticky columns 1+2: True", sticky1 and sticky2)

# 11. No ::after fade gradient on table wrapper
fade = re.search(r'\.dyu-table-wrapper[^{]*::after', HTML)
add("No ::after fade gradient: True", fade is None)

# 12. Scroll hint centered above table
scroll_hint = re.search(r'<p class="dyu-scroll-hint"[^>]*>.*?</p>\s*<div class="dyu-table-wrapper">', HTML, re.DOTALL)
add("Scroll hint centered above table: True", scroll_hint is not None)

# 13. Gold border ONLY on .dyu-hostinger-wrap
gold_borders = re.findall(r'border:[^;]*#d4a843', HTML)
gold_block_no_border = ".dyu-gold-block { border: none" in HTML
add("Gold border only on .dyu-hostinger-wrap: True", len(gold_borders) == 1 and gold_block_no_border,
    f"gold border declarations: {len(gold_borders)}")

# 14. .dyu-gold-block border:none
add(".dyu-gold-block border:none: True", ".dyu-gold-block { border: none" in HTML)

# 15. Hostinger block format
hostinger_blocks = re.findall(r'<!-- wp:hostinger-affiliate-plugin/block .+? /-->', HTML)
correct_format = sum(
    1 for b in hostinger_blocks
    if '"display_type":"multiple_product_list"' in b and '"list_layout":"list_with_description"' in b
)
add("Hostinger block format: multiple_product_list + list_with_description",
    correct_format == 10, f"correct format: {correct_format}/10")

# 16. All 10 ASINs present in links
asins_in_html = sum(1 for a in ASINS if a in HTML)
add("All 10 ASINs present", asins_in_html == 10, f"present: {asins_in_html}/10")

# 17. Affiliate tag delightfulyou-20 on all Amazon links
amazon_links = re.findall(r'https://www\.amazon\.com/dp/[^"\s]+', HTML)
# Filter out hostinger plugin internal urls (those don't need tag)
buy_button_links = re.findall(r'href="(https://www\.amazon\.com/dp/[^"]+)"\s+target="_blank"\s+rel="nofollow', HTML)
all_tagged = all("tag=delightfulyou-20" in u for u in buy_button_links)
add("Affiliate tag on all Buy on Amazon links", all_tagged and len(buy_button_links) == 10,
    f"buy links: {len(buy_button_links)}, all tagged: {all_tagged}")

# 18. rel="nofollow sponsored noopener" on all Amazon affiliate links
nofollow_count = HTML.count('rel="nofollow sponsored noopener"')
add('rel="nofollow sponsored noopener" on all 10 Amazon links', nofollow_count == 10,
    f"count: {nofollow_count}")

# 19. Author popup: hover + click trigger, white card, red name, outlined buttons
author_popup_present = ".dyu-author-popup" in HTML
hover_trigger = ".dyu-author-name-btn:hover .dyu-author-popup" in HTML
click_trigger = ".dyu-author-name-btn.active .dyu-author-popup" in HTML
red_name = ".dyu-author-popup-name { font-weight: 700; color: #c0392b" in HTML
outlined_btn = ".dyu-author-popup-link { display: inline-flex" in HTML and "border: 1.5px solid" in HTML
add("Author popup: hover + click trigger, white, red name, outlined links",
    author_popup_present and hover_trigger and click_trigger and red_name and outlined_btn)

# 20. Evidence Based button inside author block, right-aligned, teal on hover
evidence_in_author = re.search(
    r'<div class="dyu-author-block">\s*<div class="dyu-evidence-wrapper">', HTML
)
right_align = "justify-content: flex-end" in HTML
teal_hover = ".dyu-evidence-wrapper:hover .dyu-evidence-btn { background: #148f77" in HTML
add("Evidence Based: inside author block, right-aligned, teal on hover",
    evidence_in_author is not None and right_align and teal_hover)

# 21. Disclosure inside Evidence Based tooltip ONLY
disclosure_in_tooltip = "Amazon affiliate links" in HTML
# Make sure there's no separate disclosure paragraph at the bottom
bottom_section = HTML[-2000:]
bottom_disclosure = "affiliate" in bottom_section.lower() and "disclosure" in bottom_section.lower()
add("Disclosure: inside Evidence Based tooltip only",
    disclosure_in_tooltip and not bottom_disclosure)

# 22. No "Last Updated" date
no_last_updated = not re.search(r'last\s+updated', HTML, re.IGNORECASE)
add("No Last Updated date", no_last_updated)

# 23. No standalone disclosure paragraph at bottom
add("No standalone disclosure paragraph at bottom", not bottom_disclosure)

# 24. GlowPick (not DelightfulYou.com) in blue helpful box
helpful_box = re.search(r'<div class="dyu-helpful-box">.+?</div>', HTML, re.DOTALL)
hb_text = helpful_box.group(0) if helpful_box else ""
add("GlowPick in blue helpful box", "GlowPick" in hb_text and "DelightfulYou.com" not in hb_text)

# 25. 10 Hostinger blocks (one per product)
add("10 Hostinger blocks present", len(hostinger_blocks) == 10, f"found: {len(hostinger_blocks)}")

# 26. 6 FAQ items
faq_count = len(re.findall(r'<p class="dyu-faq-q">', HTML))
add("FAQ: 6 questions", faq_count == 6, f"found: {faq_count}")

# 27. 5 author rows
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
