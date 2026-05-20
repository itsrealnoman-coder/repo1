# GLOWPICK AMAZON AFFILIATE ARTICLE — MASTER BUILD PROMPT (v2)

You are building a GlowPick Amazon affiliate article for DelightfulYou.com.
Follow EVERY instruction below exactly. No deviations. No extra sections. No AI-style writing.

---

## SITE DETAILS
- Site: DelightfulYou.com | Brand: GlowPick | Affiliate tag: delightfulyou-20
- Platform: WordPress (Gutenberg / Hostinger affiliate plugin)
- Year: 2026

---

## WORKFLOW RULES
1. Do NOT start until ALL 10 Hostinger affiliate blocks are provided by the user.
2. Check all 10 ASINs for duplicates — alert user if any found, wait for replacement.
3. Fetch live price, rating, and review count from Amazon for each ASIN using curl scraper.
4. Auto-rank products: "Best Overall" badge = #1, remaining sorted by (rating × review_count) descending. Renumber 1–10.
5. Build using a Python script. Save output to /mnt/user-data/outputs/[topic]-article-v1.html
6. Also generate two standalone screenshot files:
   - `table-only.html` — full-width comparison table (no scroll, for Pinterest)
   - `faq-only.html` — styled FAQ section (for Pinterest)
7. After build, run quality checks (listed at the bottom of this prompt).

---

## ARTICLE STRUCTURE — STRICT ORDER (do not add, remove or reorder anything)

1. HTML comment header: `<!-- DelightfulYou.com | [Topic] 2026 | tag: delightfulyou-20 -->`
2. Full `<style>` CSS block (copy exactly from SECTION A below)
3. `<script>` JS block (copy exactly from SECTION B below)
4. `<div class="dyu-article">` opens
5. Author block with Evidence Based button inside (copy structure from SECTION C, replace author names per category)
6. Intro — 2 short human-written paragraphs (no AI hooks, no filler, direct and interesting)
7. Collapsible TOC (button text-only, no arrows or symbols)
8. `<h4 id="comparison-table">` heading
9. Scroll hint paragraph (centered, #aaa, ↔ symbol)
10. Comparison table (copy structure from SECTION D)
11. `<hr class="dyu-divider">`
12. `<h4>In-Depth Product Reviews</h4>`
13. 10 product sections — each follows SECTION E template exactly
14. `<hr class="dyu-divider">`
15. FAQ — 6 questions (copy structure from SECTION F)
16. Blue helpful box — brand name = GlowPick always (copy from SECTION G)
17. `<hr class="dyu-divider">`
18. Comment prompt paragraph (casual, first-person, human)
19. `<!-- wp:post-comments-form /-->`
20. `<!-- wp:comments /-->`
21. `</div>` closes .dyu-article

---

## SECTION A — FULL CSS (copy verbatim, change nothing)

```css

/* ===== BASE ===== */
.dyu-article { font-family: Georgia, 'Times New Roman', serif; color: #2c2c2c; max-width: 860px; margin: 0 auto; line-height: 1.75; position: relative; }
.dyu-article h4 { font-family: 'Palatino Linotype', Palatino, serif; color: #1a1a1a; border-bottom: 2px solid #ddd; padding-bottom: 6px; margin-top: 2em; }
.dyu-article h5 { font-family: 'Palatino Linotype', Palatino, serif; color: #154360; margin-top: 1.2em; }
.dyu-article p { margin: 0.9em 0; }
.dyu-article ul { padding-left: 1.4em; }
.dyu-article li { margin-bottom: 0.4em; }

/* ===== EVIDENCE BASED BUTTON ===== */
.dyu-evidence-wrapper { position: relative; display: flex; justify-content: flex-end; margin: 0 0 0.8em; z-index: 10; }
.dyu-evidence-btn { border: 1.5px solid #888; border-radius: 4px; padding: 5px 13px; font-size: 0.82em; font-family: Arial, sans-serif; background: #fff; color: #444; cursor: default; transition: background 0.2s, color 0.2s, border-color 0.2s; white-space: nowrap; }
.dyu-evidence-wrapper:hover .dyu-evidence-btn { background: #148f77; color: #fff; border-color: #148f77; }
.dyu-evidence-tooltip { display: none; position: absolute; right: 0; top: 110%; background: #fff; border: 1px solid #ccc; border-radius: 7px; box-shadow: 0 6px 22px rgba(0,0,0,0.13); padding: 16px 18px; width: 320px; font-family: Arial, sans-serif; font-size: 0.84em; line-height: 1.65; color: #333; z-index: 200; }
.dyu-evidence-tooltip p { margin: 0 0 0.7em; }
.dyu-evidence-tooltip p:last-child { margin: 0; }
.dyu-evidence-tooltip::before { content: ''; position: absolute; top: -7px; right: 18px; width: 12px; height: 12px; background: #fff; border-left: 1px solid #ccc; border-top: 1px solid #ccc; transform: rotate(45deg); }
.dyu-evidence-wrapper:hover .dyu-evidence-tooltip { display: block; }

/* ===== EDITORIAL TEAM ===== */
.dyu-author-block { margin: 0 0 1.4em; font-family: Arial, sans-serif; border-bottom: 1px solid #e8e8e8; padding-bottom: 1em; }
.dyu-author-row { display: flex; align-items: center; gap: 5px; margin: 0.28em 0; font-size: 0.87em; color: #555; }
.dyu-author-role-label { color: #555; white-space: nowrap; flex-shrink: 0; }
.dyu-author-name-btn { color: #c0392b; font-weight: 600; background: none; border: none; padding: 0; cursor: pointer; font-size: inherit; font-family: inherit; position: relative; display: inline-block; line-height: inherit; }
.dyu-author-name-btn:hover { text-decoration: underline; color: #922b21; }
.dyu-author-popup { visibility: hidden; opacity: 0; pointer-events: none; position: absolute; left: 0; top: calc(100% + 8px); background: #fff; border: 1px solid #e4e4e4; border-radius: 10px; box-shadow: 0 8px 26px rgba(0,0,0,0.12); padding: 15px 16px; min-width: 260px; max-width: 310px; z-index: 300; text-align: left; white-space: normal; transition: opacity 0.15s ease, visibility 0.15s ease; }
.dyu-author-popup::before { content: ''; position: absolute; top: -6px; left: 18px; width: 10px; height: 10px; background: #fff; border-left: 1px solid #e4e4e4; border-top: 1px solid #e4e4e4; transform: rotate(45deg); }
.dyu-author-name-btn:hover .dyu-author-popup,
.dyu-author-name-btn:focus-within .dyu-author-popup,
.dyu-author-name-btn.active .dyu-author-popup { visibility: visible; opacity: 1; pointer-events: auto; }
.dyu-author-popup-name { font-weight: 700; color: #c0392b; font-size: 1em; display: block; margin-bottom: 1px; }
.dyu-author-popup-title { color: #c0392b; font-size: 0.85em; display: block; margin-bottom: 8px; }
.dyu-author-popup-cred { color: #555; font-size: 0.84em; display: block; border-top: 1px solid #f0f0f0; padding-top: 9px; margin-bottom: 10px; line-height: 1.55; }
.dyu-author-popup-links { display: flex; gap: 7px; }
.dyu-author-popup-link { display: inline-flex; align-items: center; gap: 4px; border-radius: 4px; padding: 4px 11px; font-size: 0.82em; text-decoration: none; font-weight: 600; border: 1.5px solid; transition: background 0.15s, color 0.15s; }
.dyu-author-popup-link.li { color: #0077b5; border-color: #0077b5; background: #fff; }
.dyu-author-popup-link.li:hover { background: #0077b5; color: #fff; }
.dyu-author-popup-link.web { color: #555; border-color: #999; background: #fff; }
.dyu-author-popup-link.web:hover { background: #555; color: #fff; }
@media (max-width: 480px) {
  .dyu-author-popup { min-width: min(250px, 82vw); max-width: min(300px, 88vw); }
}

/* ===== DIVIDER ===== */
.dyu-divider { border: none; border-top: 2px dashed #aed6f1; margin: 2.5em 0; }

/* ===== TOC ===== */
.dyu-toc-toggle { display: block; width: 100%; background: linear-gradient(90deg, #1abc9c, #148f77); color: #fff; border: none; border-radius: 8px; padding: 11px 20px; font-size: 1em; font-family: Arial, sans-serif; font-weight: 700; cursor: pointer; text-align: left; margin: 1.5em 0 0; }
.dyu-toc-content { display: none; background: #f9f9f9; border: 1px solid #ddd; border-radius: 0 0 8px 8px; padding: 14px 20px; margin-bottom: 1.5em; }
.dyu-toc-content.open { display: block; }
.dyu-toc-content ol { margin: 0; padding-left: 1.3em; }
.dyu-toc-content li { margin-bottom: 0.35em; }
.dyu-toc-content a { color: #148f77; text-decoration: none; }
.dyu-toc-content a:hover { text-decoration: underline; }

/* ===== TABLE ===== */
.dyu-table-wrapper { overflow-x: auto; border-radius: 10px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); margin: 0.5em 0 1.5em; }
.dyu-compare-table { width: 100%; min-width: 1050px; border-collapse: collapse; font-family: Arial, sans-serif; font-size: 0.88em; }
.dyu-compare-table thead tr { background: linear-gradient(90deg, #1abc9c, #148f77); color: #fff; }
.dyu-compare-table th { padding: 11px 10px; text-align: left; white-space: nowrap; }
.dyu-compare-table td { padding: 10px 10px; vertical-align: middle; }
.dyu-compare-table th:nth-child(1) { position: sticky; left: 0; z-index: 3; background: linear-gradient(90deg, #1abc9c, #148f77); }
.dyu-compare-table th:nth-child(2) { position: sticky; left: 36px; z-index: 3; background: linear-gradient(90deg, #1abc9c, #148f77); box-shadow: 2px 0 5px rgba(0,0,0,0.1); }
.dyu-compare-table td:nth-child(1) { position: sticky; left: 0; z-index: 2; }
.dyu-compare-table td:nth-child(2) { position: sticky; left: 36px; z-index: 2; box-shadow: 2px 0 5px rgba(0,0,0,0.08); }
.dyu-compare-table tbody tr:nth-child(1) td { background: #fff9f0; }
.dyu-compare-table tbody tr:nth-child(2) td { background: #f0f9f5; }
.dyu-compare-table tbody tr:nth-child(3) td { background: #f5f0ff; }
.dyu-compare-table tbody tr:nth-child(4) td { background: #fff0f5; }
.dyu-compare-table tbody tr:nth-child(5) td { background: #f0f8ff; }
.dyu-compare-table tbody tr:nth-child(6) td { background: #fffaf0; }
.dyu-compare-table tbody tr:nth-child(7) td { background: #f5fff0; }
.dyu-compare-table tbody tr:nth-child(8) td { background: #fff5f0; }
.dyu-compare-table tbody tr:nth-child(9) td { background: #f0fff5; }
.dyu-compare-table tbody tr:nth-child(10) td { background: #f8f0ff; }
.dyu-compare-table tbody tr:nth-child(1) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(1) td:nth-child(2){background:#fff9f0;}
.dyu-compare-table tbody tr:nth-child(2) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(2) td:nth-child(2){background:#f0f9f5;}
.dyu-compare-table tbody tr:nth-child(3) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(3) td:nth-child(2){background:#f5f0ff;}
.dyu-compare-table tbody tr:nth-child(4) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(4) td:nth-child(2){background:#fff0f5;}
.dyu-compare-table tbody tr:nth-child(5) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(5) td:nth-child(2){background:#f0f8ff;}
.dyu-compare-table tbody tr:nth-child(6) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(6) td:nth-child(2){background:#fffaf0;}
.dyu-compare-table tbody tr:nth-child(7) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(7) td:nth-child(2){background:#f5fff0;}
.dyu-compare-table tbody tr:nth-child(8) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(8) td:nth-child(2){background:#fff5f0;}
.dyu-compare-table tbody tr:nth-child(9) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(9) td:nth-child(2){background:#f0fff5;}
.dyu-compare-table tbody tr:nth-child(10) td:nth-child(1),.dyu-compare-table tbody tr:nth-child(10) td:nth-child(2){background:#f8f0ff;}
.dyu-table-img { width: 56px; height: 56px; object-fit: contain; border-radius: 6px; }
.dyu-stars { color: #f5a623; font-size: 1em; }
.dyu-review-count { font-size: 0.8em; color: #777; display: block; margin-top: 2px; }
.dyu-btn-amazon { display: inline-block; background: linear-gradient(to bottom, #f7dfa5, #f0c14b); border: 1px solid #a88734; border-radius: 4px; padding: 6px 13px; font-size: 0.82em; font-weight: 700; color: #111; text-decoration: none; white-space: nowrap; }
.dyu-btn-amazon:hover { background: linear-gradient(to bottom, #f0c14b, #e8b429); }

/* ===== SCROLL HINT ===== */
.dyu-scroll-hint { font-family: Arial, sans-serif; font-size: 0.76em; color: #aaa; text-align: center; margin: 0 0 0.5em; letter-spacing: 0.01em; }

/* ===== BADGE ===== */
.dyu-rank-badge { display: inline-block; background: linear-gradient(135deg, #1abc9c, #148f77); color: #fff; font-size: 0.72em; font-weight: 700; border-radius: 20px; padding: 3px 12px; margin-bottom: 2px; font-family: Arial, sans-serif; }
.dyu-rank-badge + h4 { margin-top: 0.1em !important; }

/* ===== HOSTINGER WRAP ===== */
.dyu-hostinger-wrap { border: 2px solid #d4a843; border-radius: 10px; box-shadow: 0 3px 14px rgba(212,168,67,0.18); padding: 10px; margin: 0.5em 0 1em; }
.dyu-hostinger-wrap .ha-price-wrapper,
.dyu-hostinger-wrap [class*="price-wrapper"],
.dyu-hostinger-wrap [class*="product-footer"] { display: flex !important; align-items: center !important; gap: 14px !important; flex-wrap: nowrap !important; }
.dyu-hostinger-wrap [class*="price"] { font-size: 1.1em !important; white-space: nowrap !important; }
.dyu-hostinger-wrap [class*="buy-button"],
.dyu-hostinger-wrap a[class*="button"] { padding: 7px 16px !important; font-size: 0.88em !important; white-space: nowrap !important; }

/* ===== GOLD BLOCK ===== */
.dyu-gold-block { border: none; padding: 4px 0; margin: 0.8em 0; }

/* ===== PROS CONS ===== */
.dyu-pros-cons { display: flex; gap: 14px; margin: 1em 0; flex-wrap: wrap; }
.dyu-pros, .dyu-cons { flex: 1; min-width: 200px; background: #f8f8f8; border-radius: 6px; padding: 10px 14px; }
.dyu-pros { border-top: 3px solid #27ae60; }
.dyu-cons { border-top: 3px solid #e74c3c; }
.dyu-pros h6, .dyu-cons h6 { margin: 0 0 7px; font-family: Arial, sans-serif; font-size: 0.88em; text-transform: uppercase; letter-spacing: 0.04em; }
.dyu-pros h6 { color: #27ae60; }
.dyu-cons h6 { color: #e74c3c; }
.dyu-pros ul, .dyu-cons ul { margin: 0; padding-left: 1.2em; font-size: 0.9em; }

/* ===== REVIEWS ===== */
.dyu-review-block { background: #fafafa; border-left: 3px solid #1abc9c; border-radius: 5px; padding: 10px 14px; margin: 0.7em 0; font-size: 0.92em; }
.dyu-review-author { font-size: 0.82em; color: #555; margin-top: 5px; }

/* ===== OUR TAKE ===== */
.dyu-our-take { background: transparent; border-left: 3px solid #c0392b; padding: 8px 14px; margin: 1em 0; border-radius: 4px; font-size: 0.95em; }
.dyu-our-take strong { color: #c0392b; }

/* ===== FAQ ===== */
.dyu-faq-item { margin-bottom: 1.4em; }
.dyu-faq-q { font-family: 'Palatino Linotype', Palatino, serif; font-weight: 700; color: #154360; font-size: 1.02em; margin-bottom: 0.35em; }

/* ===== BLUE BOX ===== */
.dyu-helpful-box { background: #e8f4fd; border: 1px solid #aed6f1; border-radius: 8px; padding: 18px 22px; margin: 2em 0; }
.dyu-helpful-box p { margin: 0.4em 0; font-family: Arial, sans-serif; font-size: 0.95em; }
.dyu-helpful-box strong { color: #1a5276; }

* { box-sizing: border-box; }
.dyu-article { width: 100%; max-width: 860px; }
@media (max-width: 580px) {
  .dyu-article { padding: 0 4px; }
  .dyu-pros-cons { flex-direction: column; }
  .dyu-evidence-tooltip { width: min(280px, 90vw); right: 0; }
  .dyu-author-popup { min-width: min(220px, 80vw); max-width: min(280px, 85vw); }
  .dyu-table-wrapper { margin-left: -4px; margin-right: -4px; }
}

```

---

## SECTION D — COMPARISON TABLE (updated: clickable images)

Table row template — NOTE: image is wrapped in affiliate `<a>` tag:
```html
<tr>
  <td><strong>1</strong></td>
  <td><a href="https://www.amazon.com/dp/[ASIN]?tag=delightfulyou-20" target="_blank" rel="nofollow sponsored noopener"><img class="dyu-table-img" src="[IMAGE_URL]" alt="[ALT]" loading="lazy"></a></td>
  <td><strong>[Product Name]</strong><br><small>[size | key detail]</small></td>
  <td>[Best For]</td>
  <td>$[price]</td>
  <td><span class="dyu-stars">★★★★</span> 4.X<span class="dyu-review-count">X,XXX reviews</span></td>
  <td><a class="dyu-btn-amazon" href="https://www.amazon.com/dp/[ASIN]?tag=delightfulyou-20" target="_blank" rel="nofollow sponsored noopener">Buy on Amazon</a></td>
</tr>
```

---

## OUTPUT DELIVERABLES — 3 FILES REQUIRED

After every build, deliver these 3 files:

### FILE 1: Main Article
`best-[topic]-2026-article-v1.html`
- Complete WordPress-ready article
- Table is scrollable (mobile-friendly, min-width: 1050px, overflow-x: auto)
- Scroll hint present

### FILE 2: Table Screenshot HTML
`table-only.html`
- Full `<!DOCTYPE html>` page
- Contains ONLY the comparison table (no other article sections)
- CSS overrides for screenshot:
  - `.dyu-article { max-width: 100%; }`
  - `.dyu-compare-table { min-width: unset !important; width: 100% !important; font-size: 0.82em; }`
  - `.dyu-compare-table th, .dyu-compare-table td { padding: 8px 6px; white-space: normal; }`
  - `.dyu-table-wrapper { overflow-x: visible !important; }`
- NO scroll hint text
- Result: entire table visible on one page without scrolling

### FILE 3: FAQ Screenshot HTML
`faq-only.html`
- Full `<!DOCTYPE html>` page
- Contains ONLY the FAQ section (all 6 questions)
- Full article CSS included
- Wrapped in `<div class="dyu-article">`
- Result: styled FAQ ready for screenshot

---

## QUALITY CHECKS — run after every build

```
✅ WP blocks: 10/10 (post-comments-form + comments)
✅ Product sections: 10/10
✅ Buy on Amazon buttons: 10/10 (table ONLY — none after Our Take)
✅ Table images clickable with affiliate link: True (10/10)
✅ Table ratings: decimal stars + review count format
✅ Badge = remark only (no number in badge)
✅ Number in h4: True (10/10)
✅ Product order: Best Overall at #1, rest sorted by rating×reviews
✅ No inline onclick anywhere
✅ TOC arrows/symbols: False
✅ Verdict section: False
✅ Sticky columns 1+2: True
✅ No ::after fade gradient: True
✅ Scroll hint centered above table: True (article only)
✅ Gold border ONLY on .dyu-hostinger-wrap: True
✅ .dyu-gold-block border:none: True
✅ Hostinger block format: multiple_product_list + list_with_description
✅ All 10 ASINs present in links
✅ Affiliate tag delightfulyou-20 on all Amazon links (images + buttons)
✅ rel="nofollow sponsored noopener" on all Amazon links
✅ Author popup: hover + click trigger, white card, red name, outlined buttons
✅ Evidence Based button: inside author block, right-aligned, teal on hover
✅ Disclosure: inside Evidence Based tooltip ONLY (not at bottom of article)
✅ No Last Updated date
✅ No standalone disclosure paragraph at bottom
✅ GlowPick (not DelightfulYou.com) in blue helpful box
✅ table-only.html generated: full-width, no scroll, no scroll-hint
✅ faq-only.html generated: styled, all 6 FAQs
```

---

(Keep all other sections B, C, E, F, G, writing rules, badge remarks, and author lists from the original prompt — they remain unchanged.)
