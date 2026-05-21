#!/usr/bin/env python3
"""Quality checks for the GlowPick Indoor Tanning Bed Lotions article."""
import re
from pathlib import Path

HTML = Path("/projects/sandbox/repo1/best-indoor-tanning-bed-lotions-2026-article-v1.html").read_text()
TABLE_HTML = Path("/projects/sandbox/repo1/table-only.html").read_text()
FAQ_HTML = Path("/projects/sandbox/repo1/faq-only.html").read_text()

ASINS = [
    "B00076XR3O", "B0FJPG6TXH", "B0CJYBLCNT", "B0058E3XJI", "B08MVJ5Y8Y",
    "B08CNJ5BG7", "B0CTBF3WLS", "B0CKNHF944", "B08G1LDFL8", "B09MG4B2XB",
]

checks = []

def add(name, ok, detail=""):
    icon = "OK" if ok else "FAIL"
    checks.append((ok, name, detail))
    print(f"[{icon}] {name}{(' -- ' + detail) if detail else ''}")

def strip_entities(s):
    return re.sub(r'&#\d+;', '', s)


# 1. WP blocks (post-comments-form + comments)
pcf = HTML.count("<!-- wp:post-comments-form /-->")
wpc = HTML.count("<!-- wp:comments /-->")
add("WP blocks: post-comments-form + comments", pcf == 1 and wpc == 1, f"pcf:{pcf}, comments:{wpc}")

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
    f"total:{buy_buttons}, after Our Take:{buy_after_take}")

# 4. Table images clickable with affiliate link (10/10)
clickable_imgs = len(re.findall(
    r'<a href="https://www\.amazon\.com/dp/[^"]*tag=delightfulyou-20"[^>]*>\s*<img class="dyu-table-img"',
    HTML))
add("Table images clickable with affiliate link: 10/10", clickable_imgs == 10, f"found {clickable_imgs}")

# 5. Table ratings: decimal stars + review count format
rating_format = len(re.findall(r'<span class="dyu-stars">[^<]+</span>\s*\d\.\d', HTML))
review_count_format = len(re.findall(r'class="dyu-review-count">[\d,]+\s+reviews</span>', HTML))
add("Table ratings: decimal + review count", rating_format == 10 and review_count_format == 10,
    f"ratings:{rating_format}, review-counts:{review_count_format}")

# 6. Badge = remark only (no number in badge)
badges = re.findall(r'<span class="dyu-rank-badge">([^<]+)</span>', HTML)
no_number_in_badge = all(not re.search(r'\b\d+\b', strip_entities(b)) for b in badges)
add("Badge = remark only (no number)", len(badges) == 10 and no_number_in_badge,
    f"badges:{len(badges)}")

# 7. Number in h4: True (10/10)
h4_with_number = len(re.findall(r'<h4>\d+\.\s', HTML))
add("Number in h4: True (10/10)", h4_with_number == 10, f"found {h4_with_number}")

# 8. Product order: Best Overall at #1
first_badge = badges[0] if badges else ""
add("Product order: Best Overall at #1", "Best Overall" in first_badge, f"#1 badge: {first_badge}")

# 9. No inline onclick anywhere
onclick_count = len(re.findall(r'\bonclick\s*=', HTML, re.IGNORECASE))
add("No inline onclick anywhere", onclick_count == 0, f"found {onclick_count}")

# 10. TOC arrows/symbols: False
toc_button = re.search(r'<button class="dyu-toc-toggle"[^>]*>(.+?)</button>', HTML, re.DOTALL)
toc_text = toc_button.group(1) if toc_button else ""
arrow_chars = re.findall(r'[\u25B6\u25BC\u25BA\u2192\u2193\u25BD\u25B2+\-]', toc_text)
add("TOC arrows/symbols: False", len(arrow_chars) == 0 and "&#x25" not in toc_text)

# 11. Verdict section: False
verdict_count = len(re.findall(r'<h4[^>]*>[^<]*verdict[^<]*</h4>', HTML, re.IGNORECASE))
add("Verdict section: False", verdict_count == 0)

# 12. Sticky columns 1+2: True
sticky1 = "td:nth-child(1) { position: sticky" in HTML
sticky2 = "td:nth-child(2) { position: sticky" in HTML
add("Sticky columns 1+2: True", sticky1 and sticky2)

# 13. No ::after fade gradient
fade = re.search(r'\.dyu-table-wrapper[^{]*::after', HTML)
add("No ::after fade gradient: True", fade is None)

# 14. Scroll hint centered above table (article only)
scroll_hint = re.search(r'<p class="dyu-scroll-hint"[^>]*>.*?</p>\s*<div class="dyu-table-wrapper">', HTML, re.DOTALL)
add("Scroll hint centered above table: True", scroll_hint is not None)

# 15. Gold border ONLY on .dyu-hostinger-wrap
gold_borders = re.findall(r'border:[^;]*#d4a843', HTML)
gold_block_no_border = ".dyu-gold-block { border: none" in HTML
add("Gold border only on .dyu-hostinger-wrap: True", len(gold_borders) == 1 and gold_block_no_border)

# 16. .dyu-gold-block border:none
add(".dyu-gold-block border:none: True", ".dyu-gold-block { border: none" in HTML)


# 17. Hostinger block format: multiple_product_list + list_with_description
hostinger_blocks = re.findall(r'<!-- wp:hostinger-affiliate-plugin/block .+? /-->', HTML)
correct_format = sum(
    1 for b in hostinger_blocks
    if '"display_type":"multiple_product_list"' in b and '"list_layout":"list_with_description"' in b
)
add("Hostinger format: multiple_product_list + list_with_description",
    correct_format == 10, f"{correct_format}/10")

# 18. All 10 ASINs present in links
asins_in_html = sum(1 for a in ASINS if a in HTML)
add("All 10 ASINs present", asins_in_html == 10, f"{asins_in_html}/10")

# 19. Affiliate tag on all Amazon links (images + buttons)
buy_links = re.findall(r'href="(https://www\.amazon\.com/dp/[^"]+)"[^>]*target="_blank"[^>]*rel="nofollow', HTML)
all_tagged = all("tag=delightfulyou-20" in u for u in buy_links)
add("Affiliate tag delightfulyou-20 on all Amazon links", all_tagged and len(buy_links) >= 20,
    f"links:{len(buy_links)}, all tagged:{all_tagged}")

# 20. rel="nofollow sponsored noopener" on all Amazon links
nofollow_count = HTML.count('rel="nofollow sponsored noopener"')
add('rel="nofollow sponsored noopener" on all', nofollow_count >= 20, f"count:{nofollow_count}")

# 21. Author popup: hover + click trigger, white card, red name, outlined buttons
hover_trigger = ".dyu-author-name-btn:hover .dyu-author-popup" in HTML
click_trigger = ".dyu-author-name-btn.active .dyu-author-popup" in HTML
red_name = ".dyu-author-popup-name { font-weight: 700; color: #c0392b" in HTML
outlined_btn = "border: 1.5px solid" in HTML
add("Author popup: hover+click, white, red name, outlined", hover_trigger and click_trigger and red_name and outlined_btn)

# 22. Evidence Based: inside author block, right-aligned, teal on hover
evidence_in_author = re.search(r'<div class="dyu-author-block">\s*<div class="dyu-evidence-wrapper">', HTML)
teal_hover = ".dyu-evidence-wrapper:hover .dyu-evidence-btn { background: #148f77" in HTML
add("Evidence Based: inside author, right-aligned, teal hover",
    evidence_in_author is not None and teal_hover)

# 23. Disclosure inside Evidence Based tooltip ONLY
disclosure_in_tooltip = "Amazon affiliate links" in HTML
bottom_section = HTML[-2000:]
bottom_disclosure = "affiliate" in bottom_section.lower() and "disclosure" in bottom_section.lower()
add("Disclosure: inside tooltip only", disclosure_in_tooltip and not bottom_disclosure)

# 24. No Last Updated date
no_last_updated = not re.search(r'last\s+updated', HTML, re.IGNORECASE)
add("No Last Updated date", no_last_updated)

# 25. No standalone disclosure paragraph at bottom
add("No standalone disclosure paragraph at bottom", not bottom_disclosure)

# 26. GlowPick in blue helpful box
helpful_box = re.search(r'<div class="dyu-helpful-box">.+?</div>', HTML, re.DOTALL)
hb_text = helpful_box.group(0) if helpful_box else ""
add("GlowPick (not DelightfulYou.com) in blue box", "GlowPick" in hb_text and "DelightfulYou.com" not in hb_text)

# 27. table-only.html: full-width, no scroll, no scroll-hint
table_no_scroll = "overflow-x: visible" in TABLE_HTML
table_no_hint = '<p class="dyu-scroll-hint"' not in TABLE_HTML
table_full_width = "max-width: 100%" in TABLE_HTML
add("table-only.html: full-width, no scroll, no hint", table_no_scroll and table_no_hint and table_full_width)

# 28. faq-only.html: styled, all 6 FAQs
faq_qs = len(re.findall(r'class="dyu-faq-q"', FAQ_HTML))
faq_styled = "dyu-article" in FAQ_HTML
add("faq-only.html: styled, 6 FAQs", faq_qs == 6 and faq_styled, f"questions:{faq_qs}")

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
