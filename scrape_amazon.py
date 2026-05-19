#!/usr/bin/env python3
"""Scrape price / rating / review-count for the 10 ASINs."""
import re
import json
import subprocess
import time

ASINS = [
    "B0FKC23886",  # Jergens Shea Fusion Vanilla Crush
    "B08KT2Z93D",  # eos Shea Better Vanilla Cashmere
    "B0CRQYQBZ4",  # eos Cashmere Whipped Oil Body Butter
    "B08KQ9RNMD",  # THISWORKS In The Zone
    "B00TTD9BRC",  # CeraVe Moisturizing Cream
    "B01HTJTV4U",  # Vaseline Cocoa Radiant 3-pack
    "B001459IEE",  # Aveeno Daily Moisturizing
    "B07DJPC8JB",  # Neutrogena Hydro Boost
    "B0009F3O8Q",  # Palmer's Cocoa Butter
    "B0BVPH918S",  # Saltair Body Lotion
]

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"


def fetch(asin: str) -> str:
    out = subprocess.run(
        [
            "curl", "-sL",
            "-A", UA,
            "-H", "Accept-Language: en-US,en;q=0.9",
            "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            f"https://www.amazon.com/dp/{asin}",
        ],
        capture_output=True, text=True, timeout=30,
    )
    return out.stdout


def parse(asin: str, html: str) -> dict:
    # Title (mostly already known from user input, but useful as sanity check)
    title_m = re.search(r'<span id="productTitle"[^>]*>\s*([^<]+?)\s*</span>', html)
    title = title_m.group(1).strip() if title_m else ""

    # Rating: find the FIRST occurrence inside acrPopover or near productTitle
    # Pattern: averageCustomerReviews block
    rating = None
    m = re.search(r'id="acrPopover"[^>]*title="([0-9.]+) out of 5 stars"', html)
    if m:
        rating = m.group(1)
    if not rating:
        m = re.search(r'data-hook="rating-out-of-text"[^>]*>([0-9.]+) out of 5 stars', html)
        if m:
            rating = m.group(1)
    if not rating:
        m = re.search(r'<span class="a-icon-alt">([0-9.]+) out of 5 stars</span>', html)
        if m:
            rating = m.group(1)

    # Review count - look for the global review count near the rating
    review_count = None
    m = re.search(r'id="acrCustomerReviewText"[^>]*>([\d,]+)\s+rating', html)
    if m:
        review_count = m.group(1)
    if not review_count:
        m = re.search(r'data-hook="total-review-count"[^>]*>\s*([\d,]+)', html)
        if m:
            review_count = m.group(1)

    # Price - several patterns
    price = None
    # Pattern: a-price with a-offscreen
    for m in re.finditer(r'<span class="a-offscreen">\$([0-9]+\.[0-9]{2})</span>', html):
        price = m.group(1)
        break
    if not price:
        m = re.search(r'"priceAmount":\s*([0-9.]+)', html)
        if m:
            price = m.group(1)
    if not price:
        whole = re.search(r'a-price-whole[^>]*>\s*([0-9]+)', html)
        frac = re.search(r'a-price-fraction[^>]*>\s*([0-9]+)', html)
        if whole:
            price = whole.group(1) + "." + (frac.group(1) if frac else "00")

    return {
        "asin": asin,
        "title": title[:80],
        "rating": rating,
        "reviews": review_count,
        "price": price,
    }


def main():
    results = []
    for asin in ASINS:
        print(f"Fetching {asin}...", flush=True)
        html = fetch(asin)
        # Save for debugging
        with open(f"/tmp/{asin}.html", "w") as f:
            f.write(html)
        data = parse(asin, html)
        print(f"  {data}", flush=True)
        results.append(data)
        time.sleep(1.5)  # be polite

    with open("/tmp/amazon_data.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nSaved to /tmp/amazon_data.json")


if __name__ == "__main__":
    main()
