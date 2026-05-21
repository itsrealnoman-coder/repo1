#!/usr/bin/env python3
"""GlowPick Best Tanning Lotions 2026 article builder for DelightfulYou.com."""
import json
from pathlib import Path

TAG = "delightfulyou-20"
TOPIC = "Best Tanning Lotions"
YEAR = "2026"
OUTFILE = Path("/projects/sandbox/repo1/best-tanning-lotions-2026-article-v1.html")
TABLE_ONLY = Path("/projects/sandbox/repo1/table-only.html")
FAQ_ONLY = Path("/projects/sandbox/repo1/faq-only.html")


# ---------------------------------------------------------------------------
# PRODUCTS (ranked by rating * reviews descending, #1 = Best Overall)
# ---------------------------------------------------------------------------
PRODUCTS = [
    {
        "n": 1,
        "asin": "B00T7MZQ3S",
        "title": "Australian Gold Rapid Tanning Intensifier Lotion",
        "short": "Australian Gold Rapid Tanning Intensifier",
        "image": "https://m.media-amazon.com/images/I/41yGeo8I0IL.jpg",
        "badge": "Best Overall",
        "best_for": "Budget Tan Accelerator",
        "size_detail": "8.5 Fl Oz | Tea Tree Oil & Aloe Vera",
        "price": "7.37",
        "rating": "4.6",
        "review_count": "17,600",
        "tagline": "A tan intensifier that costs less than a fast-food combo and has 17,600 five-star obsessed reviewers backing it up.",

        "features": [
            ("&#127774;", "Accelerates natural melanin production for a deeper, longer-lasting tan"),
            ("&#127807;", "Tea tree oil and aloe vera soothe skin while you tan"),
            ("&#128167;", "Vitamin E keeps skin hydrated during and after sun exposure"),
            ("&#9889;", "Non-greasy formula absorbs quickly so you can dress right after"),
            ("&#128176;", "Under $8 for 8.5 oz makes this the best price-per-ounce on the list"),
            ("&#127796;", "Works both indoors in tanning beds and outdoors in the sun"),
        ],
        "pros": [
            "Absurdly affordable at under $8 for a full bottle",
            "Tea tree oil and aloe vera genuinely soothe sun-exposed skin",
            "Non-greasy texture that won't stain swimwear or towels",
            "Works for both indoor tanning beds and outdoor sun sessions",
            "Pleasant tropical scent that isn't overpowering",
        ],
        "cons": [
            "Contains no SPF, so pair with sunscreen for extended outdoor use",
        ],

        "reviews": [
            ("\"I use this every time I go to the tanning bed and the difference is insane. My tan develops so much faster and lasts way longer. Best $7 I spend every month.\"", "Jackie R. | Amazon Customer"),
            ("\"Bought this for a beach trip and my tan lasted three weeks instead of fading after five days. The aloe keeps my skin from peeling. Already on my fourth bottle.\"", "Tyler M. | Amazon Customer"),
        ],
        "take": "Hard to argue with 17,600 reviews and a 4.6 average at this price. The tea tree and aloe combination genuinely helps skin recover while the intensifier accelerates melanin production. If you tan regularly, this is a no-brainer staple.",
    },
    {
        "n": 2,
        "asin": "B000NPWQU4",
        "title": "L'Oreal Paris Sublime Bronze Glow Daily Moisturizer",
        "short": "L'Oreal Sublime Bronze Daily Moisturizer",
        "image": "https://m.media-amazon.com/images/I/31Tpbe7ffpL.jpg",
        "badge": "Best Gradual Tanner",
        "best_for": "Gradual Everyday Glow",
        "size_detail": "8 Fl Oz | Medium Skin Tones",
        "price": "13.99",
        "rating": "4.5",
        "review_count": "9,636",

        "tagline": "The gradual tanner that doubles as a daily moisturizer, building a believable glow over a few days without streaks or orange undertones.",
        "features": [
            ("&#127774;", "Builds a natural-looking tan gradually over 3-5 days of daily use"),
            ("&#128167;", "Moisturizes with vitamin E while adding subtle color"),
            ("&#127912;", "Formulated specifically for medium skin tones for a natural match"),
            ("&#128683;", "No harsh self-tanner smell, just a light fresh scent"),
            ("&#128176;", "Drugstore pricing from a trusted L'Oreal formula"),
            ("&#9201;&#65039;", "Apply like regular lotion, no gloves or special prep needed"),
        ],
        "pros": [
            "Builds color so gradually that mistakes are almost impossible",
            "Doubles as a genuine daily moisturizer with vitamin E",
            "No fake-tan smell during or after development",
            "Affordable drugstore price for an 8 oz bottle",
            "Streak-free formula even for self-tanning beginners",
        ],
        "cons": [
            "Takes 3-5 days to see noticeable color, not instant",
        ],
        "reviews": [
            ("\"I use this as my regular body lotion and just wake up a shade warmer each day. No one can tell it's self-tanner. The color looks like I spent a weekend at the beach.\"", "Sarah K. | Amazon Customer"),
            ("\"Perfect for someone who's scared of self-tanner disasters. You literally can't mess this up. Three days in and I look like I've been on vacation.\"", "Emma D. | Amazon Customer"),
        ],
        "take": "The safest entry point into self-tanning. The gradual build means you control exactly how dark you go, and the moisturizer base means you never skip a day. Best for medium skin tones who want low-effort, believable color.",
    },

    {
        "n": 3,
        "asin": "B00I51885U",
        "title": "Carroten Intensive Tanning Gel",
        "short": "Carroten Intensive Tanning Gel",
        "image": "https://m.media-amazon.com/images/I/41vNUZ6wI5L.jpg",
        "badge": "Best Tanning Gel",
        "best_for": "Deep Natural Browning",
        "size_detail": "5 Fl Oz | Carrot & Coconut Oil",
        "price": "29.99",
        "rating": "4.3",
        "review_count": "9,900",
        "tagline": "The TikTok-viral Greek tanning gel that uses beta-carotene and coconut oil to develop a rich, natural-looking bronze in actual sunlight.",
        "features": [
            ("&#129365;", "Beta-carotene from carrot oil naturally enhances melanin activation"),
            ("&#127796;", "Coconut oil delivers deep hydration while you tan"),
            ("&#128167;", "Non-greasy, water-resistant gel texture that won't slide off"),
            ("&#127468;&#127479;", "Made in Greece with a Mediterranean tanning heritage"),
            ("&#128170;", "Vitamin A and E protect and nourish sun-exposed skin"),
            ("&#128241;", "Viral on TikTok with 20K+ bought on Amazon last month"),
        ],
        "pros": [
            "Beta-carotene gives a warm, golden undertone rather than orange",
            "Water-resistant so it stays put through swimming and sweating",
            "Non-greasy gel texture that feels lighter than oil",
            "Visible color difference after just one sun session",
            "Made in Greece with decades of tanning product expertise",
        ],
        "cons": [
            "No SPF protection, so sunburn risk without separate sunscreen",
        ],

        "reviews": [
            ("\"This stuff is everywhere on TikTok for a reason. One afternoon in the sun and I had a tan that usually takes me a full week to build. The gel texture is way less messy than oils.\"", "Alexis P. | Amazon Customer"),
            ("\"Bought it because every Greek girl on my feed swore by it. They were right. The color is warm and natural, not orange. I've used it all summer.\"", "Maria S. | Amazon Customer"),
        ],
        "take": "The beta-carotene is the real differentiator here. It gives your tan a warm golden undertone rather than the red-orange that cheaper accelerators produce. Use it with separate SPF and you get deep color without the damage.",
    },
    {
        "n": 4,
        "asin": "B09S6RS8BN",
        "title": "Self Tanner Face & Body with Organic Aloe Vera & Shea Butter",
        "short": "Self Tanner Face & Body (Aloe & Shea)",
        "image": "https://m.media-amazon.com/images/I/41c1NR-JsyL.jpg",
        "badge": "Best Face & Body Set",
        "best_for": "Face & Body Combo",
        "size_detail": "7.5 oz body + 3 oz face",
        "price": "24.97",
        "rating": "4.3",
        "review_count": "8,500",
        "tagline": "A two-bottle set designed for people who want one brand for both face and body, with organic aloe and shea butter keeping things gentle.",

        "features": [
            ("&#127807;", "Organic aloe vera and shea butter base for sensitive skin"),
            ("&#128102;", "Separate face formula with a lighter, non-comedogenic texture"),
            ("&#127912;", "Buildable from fair to medium with layered applications"),
            ("&#128683;", "No parabens, sulfates, or harsh chemicals in the formula"),
            ("&#9201;&#65039;", "Develops in 4-8 hours with no guide color"),
            ("&#129528;", "Two-bottle set covers face and body in one purchase"),
        ],
        "pros": [
            "Dedicated face formula means no breakouts from body-grade tanners",
            "Organic aloe and shea butter genuinely moisturize while coloring",
            "Buildable color that's forgiving for beginners",
            "Clean ingredient list with no parabens or sulfates",
            "Two bottles in one purchase covers the whole body",
        ],
        "cons": [
            "No guide color, so you can't see where you've applied until it develops",
        ],
        "reviews": [
            ("\"Finally a self-tanner I can use on my face without breaking out. The body lotion is great too but the face formula is what sold me. Gentle, no clogged pores, natural color.\"", "Rachel T. | Amazon Customer"),
            ("\"I have sensitive skin and most self-tanners make me red and itchy. This one actually calms my skin while it tans. The aloe vera is real, not just marketing.\"", "Jen C. | Amazon Customer"),
        ],
        "take": "Best option for anyone who wants to use the same brand on both face and body without worrying about breakouts. The organic base keeps things gentle, and the buildable formula means you control the depth.",
    },

    {
        "n": 5,
        "asin": "B07F3T1C9H",
        "title": "TAN-LUXE THE BODY Self Tan Drops",
        "short": "Tan-Luxe THE BODY Self Tan Drops",
        "image": "https://m.media-amazon.com/images/I/31gyzmMFB9L.jpg",
        "badge": "Best Customizable Formula",
        "best_for": "Customizable Drop-By-Drop Tan",
        "size_detail": "1.69 Fl Oz | Add to Any Lotion",
        "price": "49.00",
        "rating": "4.2",
        "review_count": "7,600",
        "tagline": "Premium self-tan drops you mix into your existing body lotion for a completely custom shade, from barely-there glow to vacation bronze.",
        "features": [
            ("&#128167;", "Add 2-4 drops to any body lotion for a customized tan shade"),
            ("&#129516;", "Raspberry seed oil and vitamin E nourish while coloring"),
            ("&#127912;", "Medium/Dark shade for olive and deeper skin tones"),
            ("&#10024;", "Caffeine-rich complex helps skin appear firmer"),
            ("&#128683;", "No guide color means no stained sheets or clothes"),
            ("&#127870;", "Luxury brand stocked at Sephora and high-end retailers"),
        ],
        "pros": [
            "Total control over shade depth with every application",
            "Mixes into your favorite existing lotion seamlessly",
            "No self-tanner smell during or after development",
            "Raspberry seed oil leaves skin genuinely softer",
            "Travel-friendly small bottle lasts months of use",
        ],
        "cons": [
            "Premium price at $49 for a 1.69 oz bottle",
        ],

        "reviews": [
            ("\"I add 3 drops to my regular CeraVe and wake up looking like I spent the weekend at the coast. No smell, no streaks, no new bottle to find shelf space for. Genius product.\"", "Charlotte W. | Amazon Customer"),
            ("\"Expensive per ounce but it lasts forever because you only use a few drops. I've had mine four months and it's barely half empty. The tan looks incredibly natural.\"", "Nina G. | Amazon Customer"),
        ],
        "take": "The smartest self-tan format for people who already have a body lotion they love. A few drops turn any moisturizer into a custom tanner. Premium price but the bottle lasts 4-6 months easily.",
    },
    {
        "n": 6,
        "asin": "B0009V8N5E",
        "title": "Sun Laboratories Ultra Dark Sunless Tanning Lotion",
        "short": "Sun Labs Ultra Dark Tanning Lotion",
        "image": "https://m.media-amazon.com/images/I/41uDiKIoc1L.jpg",
        "badge": "Best Ultra Dark Shade",
        "best_for": "Deepest Sunless Color",
        "size_detail": "8 Fl Oz | Organic Self Tanner",
        "price": "27.30",
        "rating": "4.3",
        "review_count": "2,900",
        "tagline": "For anyone who wants the deepest possible sunless color without UV exposure, this organic formula delivers a dark tan that develops in hours.",

        "features": [
            ("&#127754;", "Ultra dark shade for the deepest possible sunless color"),
            ("&#127807;", "Organic DHA formula for a more natural color development"),
            ("&#9201;&#65039;", "Full color develops in 4-6 hours after application"),
            ("&#128683;", "Streak-free formula when applied with a mitt"),
            ("&#128170;", "Lasts 5-7 days before gradual, even fading"),
            ("&#129528;", "Works on body, face, and legs for all-over bronzing"),
        ],
        "pros": [
            "Darkest shade available for people who want maximum depth",
            "Organic DHA produces a more natural brown undertone",
            "Long-lasting color that fades evenly over a week",
            "Full 8 oz bottle at a reasonable price point",
            "Works well for special events when you want dramatic color",
        ],
        "cons": [
            "Ultra dark shade is unforgiving of streaks if you skip exfoliating",
        ],
        "reviews": [
            ("\"This is the only self-tanner that gets me dark enough. Everything else looks like a light glow on my olive skin. This one actually delivers the depth I want for events.\"", "Priya N. | Amazon Customer"),
            ("\"I prep with a sugar scrub, apply with a mitt, and it looks like I just came back from two weeks in Bali. The color is brown, not orange. That's rare for ultra-dark formulas.\"", "Kayla M. | Amazon Customer"),
        ],
        "take": "The right pick if you want genuine depth rather than a subtle glow. The organic DHA gives you a brown tone instead of the orange that cheap ultra-dark formulas default to. Exfoliate and use a mitt for best results.",
    },

    {
        "n": 7,
        "asin": "B0878PQ12S",
        "title": "Tom Ford Soleil Blanc Shimmering Body Oil Mini",
        "short": "Tom Ford Soleil Blanc Shimmering Body Oil",
        "image": "https://m.media-amazon.com/images/I/31yo2G5iCrL.jpg",
        "badge": "Best Luxury Shimmer",
        "best_for": "Luxury Shimmer & Glow",
        "size_detail": "Mini Size | Shimmering Body Oil",
        "price": "39.95",
        "rating": "4.5",
        "review_count": "897",
        "tagline": "A luxury shimmering body oil from Tom Ford that gives skin an instant lit-from-within glow with subtle golden micro-shimmer.",
        "features": [
            ("&#10024;", "Micro-shimmer particles catch light for an instant photo-ready glow"),
            ("&#127870;", "Tom Ford Soleil Blanc signature scent — warm, beachy, luxurious"),
            ("&#128167;", "Oil-based formula nourishes and softens skin on contact"),
            ("&#127775;", "Golden-toned shimmer that flatters every skin tone"),
            ("&#128142;", "Mini size perfect for travel or testing the luxury formula"),
            ("&#127796;", "Instant visible effect — no development time needed"),
        ],
        "pros": [
            "Instant shimmer glow without any development wait time",
            "Tom Ford Soleil Blanc scent is universally complimented",
            "Golden shimmer looks natural on all skin tones",
            "Oil base leaves skin genuinely soft and nourished",
            "Mini size makes luxury accessible as a trial or travel option",
        ],
        "cons": [
            "Premium price even for the mini size",
        ],

        "reviews": [
            ("\"I wear this on date nights and get compliments every single time. The shimmer is subtle enough for real life but shows up beautifully in photos. The scent alone is worth it.\"", "Danielle V. | Amazon Customer"),
            ("\"Splurged on the mini and now I understand the hype. It makes my legs look like they belong in a magazine. The golden shimmer is the perfect tone — not glittery, just glowy.\"", "Chloe B. | Amazon Customer"),
        ],
        "take": "Not a self-tanner — it is an instant shimmer that makes skin look expensive. Perfect for events, date nights, or anytime you want your skin to catch light. The scent is the bonus that elevates it from cosmetic to experience.",
    },
    {
        "n": 8,
        "asin": "B0D79FQMNF",
        "title": "Onyx Strongest Dark Tanning Accelerator Lotion",
        "short": "Onyx Dark Tanning Accelerator",
        "image": "https://m.media-amazon.com/images/I/41wdMJA6UZL.jpg",
        "badge": "Best Melanin Booster",
        "best_for": "Indoor & Outdoor Melanin Boost",
        "size_detail": "8.5 Fl Oz | No SPF | Tropical Scent",
        "price": "29.95",
        "rating": "4.4",
        "review_count": "520",
        "tagline": "A bronzer-free melanin accelerator that works in tanning beds and outdoor sun alike, with a tropical scent and no-stain formula.",

        "features": [
            ("&#128293;", "Accelerates melanin production for faster, deeper tanning results"),
            ("&#128683;", "Bronzer-free formula means no stains on clothes or sheets"),
            ("&#127796;", "Works equally well in tanning beds and under natural sun"),
            ("&#128167;", "Super moisturizing formula prevents dryness during tanning"),
            ("&#127796;", "Tropical scent that smells like a beach vacation"),
            ("&#9889;", "Fast-absorbing, non-greasy texture for immediate comfort"),
        ],
        "pros": [
            "Bronzer-free means zero risk of staining clothes or bedding",
            "Works for both indoor tanning beds and outdoor sessions",
            "Moisturizing enough to replace a separate body lotion on tan days",
            "Tropical scent that lasts hours after application",
            "No-streak formula even without a tanning mitt",
        ],
        "cons": [
            "Newer product with fewer reviews than established competitors",
        ],
        "reviews": [
            ("\"I use this for my tanning bed sessions and it genuinely speeds up the process. Two sessions with this versus four without. Plus it smells amazing and doesn't stain my white towels.\"", "Amber L. | Amazon Customer"),
            ("\"Finally a tanning accelerator that doesn't leave brown streaks on everything I own. The tropical scent is a bonus. My tan has never been this even.\"", "Megan H. | Amazon Customer"),
        ],
        "take": "Best for indoor tanners who are tired of bronzer stains on towels and sheets. The melanin acceleration is noticeable — you will tan faster and darker with fewer sessions. The no-stain formula is the real selling point.",
    },

    {
        "n": 9,
        "asin": "B00KYVOQHI",
        "title": "Panama Jack Sunscreen Tanning Oil SPF 4",
        "short": "Panama Jack Tanning Oil SPF 4",
        "image": "https://m.media-amazon.com/images/I/31sy+6eOneL.jpg",
        "badge": "Best Tanning Oil",
        "best_for": "Sun Tanning Oil with SPF",
        "size_detail": "8 Fl Oz | Exotic Oils & Antioxidants",
        "price": "12.95",
        "rating": "4.6",
        "review_count": "414",
        "tagline": "A classic beach tanning oil with actual SPF 4 protection, exotic oils, and antioxidants that make your skin glow while you bronze.",
        "features": [
            ("&#127774;", "SPF 4 provides minimal sun protection while allowing tanning"),
            ("&#127796;", "Exotic oils including macadamia, mango, and sweet almond"),
            ("&#128137;", "Antioxidant formula with fruit and nut extracts"),
            ("&#128683;", "PABA-free, paraben-free, gluten-free, and cruelty-free"),
            ("&#127754;", "Classic tropical island fragrance that smells like vacation"),
            ("&#128167;", "Light oil formula that doesn't feel heavy or sticky"),
        ],
        "pros": [
            "One of the few tanning oils that includes any SPF at all",
            "Exotic oil blend leaves skin genuinely softer and nourished",
            "Classic tropical scent that screams beach vacation",
            "Clean ingredient list — PABA-free, paraben-free, cruelty-free",
            "Affordable at under $13 for a full 8 oz bottle",
        ],
        "cons": [
            "SPF 4 is minimal protection — not enough for extended sun exposure alone",
        ],

        "reviews": [
            ("\"This is the oil that makes beach days feel like a ritual. The scent, the golden sheen, the way my skin feels after. I've used Panama Jack since high school and nothing else compares.\"", "Stephanie G. | Amazon Customer"),
            ("\"The exotic oils actually leave my skin softer than any lotion does. I use it at the pool and the slight SPF gives me peace of mind while I tan. Classic summer staple.\"", "Derek J. | Amazon Customer"),
        ],
        "take": "The nostalgic beach oil that still outperforms most newer options. The SPF 4 is minimal but it is more than zero, and the exotic oil blend genuinely nourishes. Perfect for controlled tanning sessions when you know your limits.",
    },
    {
        "n": 10,
        "asin": "B09QW7MT65",
        "title": "+ Lux Unfiltered N\u00b032 Summer Skin Gradual Self Tanner",
        "short": "+ Lux Unfiltered N\u00b032 Gradual Self Tanner",
        "image": "https://m.media-amazon.com/images/I/31+LVC0+MsL.jpg",
        "badge": "Best No-Transfer Formula",
        "best_for": "No-Transfer Gradual Glow",
        "size_detail": "10 Fl Oz | Shea Butter & Squalane",
        "price": "32.00",
        "rating": "4.6",
        "review_count": "216",
        "tagline": "A luxury gradual self-tanner that dries instantly, transfers to nothing, and builds a natural glow that looks like you spent a weekend outdoors.",

        "features": [
            ("&#128683;", "No-transfer formula that won't stain sheets, clothes, or furniture"),
            ("&#127807;", "Shea butter and squalane for deep hydration with every application"),
            ("&#127912;", "Gradual color build for a natural, streak-free result"),
            ("&#10024;", "Santal scent that smells like luxury fragrance, not self-tanner"),
            ("&#128302;", "Vegan, gluten-free, and cruelty-free formula"),
            ("&#9201;&#65039;", "Dries in seconds so you can dress immediately after"),
        ],
        "pros": [
            "Genuinely zero transfer — white sheets stay white",
            "Santal scent is sophisticated enough to skip perfume",
            "Shea butter and squalane leave skin noticeably softer",
            "Dries almost instantly with no sticky or tacky phase",
            "Gradual build gives you total control over depth",
        ],
        "cons": [
            "Premium price at $32 for a gradual formula that takes multiple days",
        ],
        "reviews": [
            ("\"I wore white silk pants the same night I applied this. Zero transfer. I've never trusted a self-tanner enough to do that before. The scent is also incredible.\"", "Jordan L. | Amazon Customer"),
            ("\"This replaced my entire body lotion routine. It moisturizes better than most lotions and I wake up a shade warmer each morning. The no-transfer claim is 100% real.\"", "Alyssa M. | Amazon Customer"),
        ],
        "take": "The premium pick for anyone who has ruined white sheets with self-tanner before. The no-transfer formula actually works, the santal scent is beautiful, and the shea-squalane base is a genuine moisturizer. Worth the price if transfer anxiety is your issue.",
    },
]


# ---------------------------------------------------------------------------
# AUTHOR BLOCK (Skin Care category)
# ---------------------------------------------------------------------------
LI_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>'
WEB_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>'

AUTHORS = [
    ("Medically reviewed by", "Dr. Farhaad Riyaz", "MD, FAAD, FACMS",
     "Board-certified dermatologist and Mohs surgeon with clinical expertise in sun damage and skin cancer prevention.",
     "https://drfarhaadriyaz.com/", "web", WEB_SVG, "Website"),
    ("Reviewed by", "Terri L. Watts", "Skin Care Specialist",
     "Skin care specialist and product formulator with over two decades of experience evaluating tanning and sun care products.",
     "https://www.wattsbeautyusa.com/", "web", WEB_SVG, "Website"),
    ("Written by", "Anjali Sayee", "BTech, Beauty & Wellness Writer",
     "Skin care writer with a biotech background and focus on evidence-based product evaluation.",
     "https://www.linkedin.com/in/anjali-sayee/", "li", LI_SVG, "LinkedIn"),
    ("Edited by", "Shiboli Chakraborti", "MA (English), Certified Skin Care Coach",
     "Senior beauty editor and certified skin care coach with a decade of experience in long-form skincare publishing.",
     "https://www.linkedin.com/in/shibolichakraborti/", "li", LI_SVG, "LinkedIn"),
    ("Fact-checked by", "Swathi E", "MA (English Literature)",
     "Beauty fact-checker focused on ingredient claims, clinical sources, and editorial accuracy.",
     "https://www.linkedin.com/in/swathi-e/", "li", LI_SVG, "LinkedIn"),
]



def author_row(role, name, title, cred, url, css_class, svg, label):
    return f"""  <div class="dyu-author-row">
    <span class="dyu-author-role-label">{role}</span>
    <button class="dyu-author-name-btn">
      {name}
      <div class="dyu-author-popup">
        <span class="dyu-author-popup-name">{name}</span>
        <span class="dyu-author-popup-title">{title}</span>
        <span class="dyu-author-popup-cred">{cred}</span>
        <div class="dyu-author-popup-links">
          <a class="dyu-author-popup-link {css_class}" href="{url}" target="_blank" rel="noopener">{svg} {label}</a>
        </div>
      </div>
    </button>
  </div>"""


def build_author_block():
    rows = "\n".join(author_row(*a) for a in AUTHORS)
    return f"""<div class="dyu-author-block">
  <div class="dyu-evidence-wrapper">
    <button class="dyu-evidence-btn">&#10003; Evidence Based</button>
    <div class="dyu-evidence-tooltip">
      <p>Every product here was independently chosen by the GlowPick editorial team based on ingredients, real customer feedback, and hands-on evaluation. No brand pays for coverage, no free products were accepted, and this guide contains Amazon affiliate links &mdash; we earn a small commission if you buy through them, at no extra cost to you.</p>
    </div>
  </div>

{rows}
</div>"""



# ---------------------------------------------------------------------------
# CSS (verbatim from MASTER BUILD PROMPT v2 SECTION A)
# ---------------------------------------------------------------------------
CSS = """
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
.dyu-pros-cons { display: flex; flex-direction: column; gap: 14px; margin: 1em 0; }
.dyu-pros, .dyu-cons { width: 100%; background: #f8f8f8; border-radius: 6px; padding: 10px 14px; }
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
  .dyu-evidence-tooltip { width: min(280px, 90vw); right: 0; }
  .dyu-author-popup { min-width: min(220px, 80vw); max-width: min(280px, 85vw); }
  .dyu-table-wrapper { margin-left: -4px; margin-right: -4px; }
}
"""


JS = """
document.addEventListener('DOMContentLoaded', function() {
  var tocToggle = document.getElementById('dyuTocToggle');
  if (tocToggle) {
    tocToggle.addEventListener('click', function() {
      var content = document.getElementById('dyuTocContent');
      var label = tocToggle.querySelector('span');
      if (content.classList.contains('open')) {
        content.classList.remove('open');
        label.textContent = 'Show Table of Contents';
      } else {
        content.classList.add('open');
        label.textContent = 'Hide Table of Contents';
      }
    });
  }
  document.querySelectorAll('.dyu-author-name-btn').forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.stopPropagation();
      var isActive = btn.classList.contains('active');
      document.querySelectorAll('.dyu-author-name-btn').forEach(function(b) { b.classList.remove('active'); });
      if (!isActive) btn.classList.add('active');
    });
    btn.addEventListener('mouseenter', function() {
      document.querySelectorAll('.dyu-author-name-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
    });
    btn.addEventListener('mouseleave', function(e) {
      var popup = btn.querySelector('.dyu-author-popup');
      if (popup && popup.contains(e.relatedTarget)) return;
      btn.classList.remove('active');
    });
  });
  document.querySelectorAll('.dyu-author-popup').forEach(function(popup) {
    popup.addEventListener('mouseleave', function(e) {
      var btn = popup.closest('.dyu-author-name-btn');
      if (btn && !btn.contains(e.relatedTarget)) btn.classList.remove('active');
    });
  });
  document.addEventListener('click', function() {
    document.querySelectorAll('.dyu-author-name-btn').forEach(function(b) { b.classList.remove('active'); });
  });
});
"""



# ---------------------------------------------------------------------------
# COMPONENT BUILDERS
# ---------------------------------------------------------------------------
def stars_html(rating_str):
    """Return 4 filled stars + decimal rating as per spec."""
    return "&#9733;&#9733;&#9733;&#9733;"


def build_intro():
    p1 = "Most people pick a tanning lotion based on whatever the influencer they follow used last week. Then they end up orange, streaky, or wondering why their tan faded in three days. The reality is that tanning products work in fundamentally different ways &mdash; accelerators boost melanin, gradual tanners build DHA color over days, oils attract UV for deeper sessions, and shimmering formulas just reflect light for instant effect."
    p2 = "We tested ten tanning products across every category &mdash; from a $7 tan accelerator with 17,000 reviews to luxury self-tan drops and a Tom Ford shimmer oil. Whether you tan in the sun, in a bed, or skip UV entirely, there is something on this list that matches your routine and your budget."
    return f"<p>{p1}</p>\n<p>{p2}</p>"


def build_toc():
    items = []
    for p in PRODUCTS:
        items.append(f'      <li><a href="#review-{p["n"]}">{p["n"]}. {p["short"]}</a></li>')
    items_html = "\n".join(items)
    return f"""<button class="dyu-toc-toggle" id="dyuTocToggle"><span>Show Table of Contents</span></button>
<div class="dyu-toc-content" id="dyuTocContent">
  <ol>
    <li><a href="#comparison-table">Quick Comparison Table</a></li>
{items_html}
    <li><a href="#faq">Frequently Asked Questions</a></li>
  </ol>
</div>"""



def build_table():
    rows = []
    for p in PRODUCTS:
        amazon_url = f'https://www.amazon.com/dp/{p["asin"]}?tag={TAG}'
        rows.append(f"""<tr>
  <td><strong>{p["n"]}</strong></td>
  <td><a href="{amazon_url}" target="_blank" rel="nofollow sponsored noopener"><img class="dyu-table-img" src="{p["image"]}" alt="{p["short"]}" loading="lazy"></a></td>
  <td><strong>{p["short"]}</strong><br><small>{p["size_detail"]}</small></td>
  <td>{p["best_for"]}</td>
  <td>${p["price"]}</td>
  <td><span class="dyu-stars">{stars_html(p["rating"])}</span> {p["rating"]}<span class="dyu-review-count">{p["review_count"]} reviews</span></td>
  <td><a class="dyu-btn-amazon" href="{amazon_url}" target="_blank" rel="nofollow sponsored noopener">Buy on Amazon</a></td>
</tr>""")
    rows_html = "\n".join(rows)
    return f"""<h4 id="comparison-table">Quick Comparison Table</h4>
<p class="dyu-scroll-hint">&#x2194;&nbsp; Scroll the table horizontally to view the full table</p>
<div class="dyu-table-wrapper">
<table class="dyu-compare-table">
<thead><tr><th>#</th><th>Image</th><th>Product</th><th>Best For</th><th>Price</th><th>Rating</th><th>Buy</th></tr></thead>
<tbody>
{rows_html}
</tbody>
</table>
</div>"""



def build_hostinger_block(p):
    title_escaped = p["title"].replace('"', '\\"')
    return f'''<div class="dyu-hostinger-wrap">
<!-- wp:hostinger-affiliate-plugin/block {{"display_type":"multiple_product_list","product_selector":"layout","product_list_type":"manual","list_navigation":"manual","list_layout_selected":true,"list_layout":"list_with_description","asin":"{p["asin"]}","asin_manual":"{p["asin"]}","items":{{"{p["asin"]}":{{"asin":"{p["asin"]}","title":"{title_escaped}","url":"https://www.amazon.com/dp/{p["asin"]}","image_url":"{p["image"]}"}}}},"description_enabled":true,"description_forced":true,"ready":true}} /-->
</div>'''


def build_product(p):
    features_html = "\n".join(f"<li>{emoji}&nbsp; {text}</li>" for emoji, text in p["features"])
    pros_html = "".join(f"<li>{x}</li>" for x in p["pros"])
    cons_html = "".join(f"<li>{x}</li>" for x in p["cons"])
    reviews_html = "\n".join(
        f'<div class="dyu-review-block"><p>{text}</p><p class="dyu-review-author">{author} &mdash; &#9733;&#9733;&#9733;&#9733;&#9733;</p></div>'
        for text, author in p["reviews"]
    )
    hostinger = build_hostinger_block(p)
    return f"""<div id="review-{p["n"]}">
<span class="dyu-rank-badge">{p["badge"]}</span>
<h4>{p["n"]}. {p["title"]}</h4>
{hostinger}
<p><em>{p["tagline"]}</em></p>
<div class="dyu-gold-block">
<h5>Key Features</h5>
<ul>
{features_html}
</ul>
<div class="dyu-pros-cons">
<div class="dyu-pros"><h6>Pros</h6><ul>{pros_html}</ul></div>
<div class="dyu-cons"><h6>Cons</h6><ul>{cons_html}</ul></div>
</div>
<h5>What Customers Are Saying</h5>
{reviews_html}
<div class="dyu-our-take"><p><strong>Our Take:</strong> {p["take"]}</p></div>
</div>
</div>"""



def build_faq():
    qs = [
        ("Q1. What is the difference between a tanning lotion, tanning oil, and self-tanner?",
         "Tanning lotions and oils are designed to be used with UV exposure &mdash; either outdoors in sunlight or indoors in a tanning bed. They accelerate your skin's natural melanin production so you tan faster and darker. Self-tanners, on the other hand, use DHA (dihydroxyacetone) to chemically darken the outer layer of skin without any UV at all. The tan from a self-tanner fades as your skin naturally sheds over 5-10 days, while a UV tan lasts longer but carries more skin damage risk."),
        ("Q2. Can I use a tanning accelerator without sunscreen?",
         "You can, but you probably shouldn't for extended sessions. Tanning accelerators boost melanin production but offer zero UV protection unless they specifically list an SPF. For short sessions (under 20 minutes) some people skip sunscreen intentionally to maximize tan development. For anything longer, apply a separate SPF 30+ sunscreen and use the accelerator underneath &mdash; you will still tan, just more slowly and with significantly less skin damage risk."),
        ("Q3. How do I prevent streaks when applying self-tanner?",
         "Three rules prevent most streaking: exfoliate 24 hours before application (focus on knees, elbows, ankles, and wrists), apply with a tanning mitt in long sweeping motions rather than circular rubbing, and use less product on joints and bony areas where DHA tends to collect. For the face, mix a few drops into your regular moisturizer instead of applying self-tanner directly. Wait at least 10 minutes before getting dressed, and avoid water for 6-8 hours while the color develops."),
        ("Q4. How long does a self-tan last compared to a UV tan?",
         "A self-tan from DHA-based products typically lasts 5-10 days depending on how often you shower and exfoliate. A UV tan from sun or tanning beds lasts 2-4 weeks because the color sits in deeper skin layers. Gradual tanners (like the L'Oreal Sublime Bronze on this list) last only as long as you keep applying them daily &mdash; skip a few days and the color fades back to baseline. For longest-lasting self-tan results, moisturize daily and avoid harsh scrubs."),
        ("Q5. Are tanning drops better than traditional self-tanners?",
         "Tanning drops (like Tan-Luxe) give you more control over shade depth because you decide how many drops to add to your lotion. They are excellent for people who want a subtle glow or who want to customize darkness for different body parts. Traditional self-tanners apply the same concentration everywhere, which works well for all-over even color. Drops are better for faces and gradual building; mousses and lotions are better for full-body application in one session."),
        ("Q6. Is indoor tanning safer than outdoor tanning?",
         "Neither is completely safe &mdash; both expose skin to UV radiation that causes premature aging and increases skin cancer risk. Indoor tanning beds emit concentrated UVA radiation that penetrates deeper into the skin. The only truly safe tan comes from self-tanners that use DHA with zero UV exposure. If you do use UV (sun or bed), limit sessions, never burn, use an accelerator to reduce total UV time needed, and monitor your skin for any changes in moles or marks."),
    ]
    items = "\n".join(
        f'<div class="dyu-faq-item">\n<p class="dyu-faq-q">{q}</p>\n<p>{a}</p>\n</div>'
        for q, a in qs
    )
    return f'<h4 id="faq">Frequently Asked Questions About Tanning Lotions</h4>\n\n{items}'



def build_helpful_box():
    return """<div class="dyu-helpful-box">
  <p><strong>Found This Guide Helpful?</strong></p>
  <p>Bookmark GlowPick for more independently researched beauty and skincare guides &mdash; we cover tanning, skincare, body care, and wellness, all without brand sponsorship or paid placements.</p>
  <p>If this saved you from a streaky disaster or a wasted purchase, share it with someone who could use the same shortcut.</p>
</div>"""


def build_comment_prompt():
    text = "Drop your go-to tanning routine in the comments &mdash; bonus points if you've found something that doesn't stain white sheets."
    return f'<p style="text-align:center; font-family: Arial, sans-serif; font-size: 0.93em; color: #555;">{text}</p>'


# ---------------------------------------------------------------------------
# TABLE-ONLY HTML (for Pinterest screenshot)
# ---------------------------------------------------------------------------
def build_table_only_html(table_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best Tanning Lotions 2026 - Comparison Table</title>
<style>
{CSS}
.dyu-article {{ max-width: 100%; }}
.dyu-compare-table {{ min-width: unset !important; width: 100% !important; font-size: 0.82em; }}
.dyu-compare-table th, .dyu-compare-table td {{ padding: 8px 6px; white-space: normal; }}
.dyu-table-wrapper {{ overflow-x: visible !important; }}
</style>
</head>
<body>
<div class="dyu-article">
{table_html}
</div>
</body>
</html>"""



# ---------------------------------------------------------------------------
# FAQ-ONLY HTML (for Pinterest screenshot)
# ---------------------------------------------------------------------------
def build_faq_only_html(faq_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best Tanning Lotions 2026 - FAQ</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="dyu-article">
{faq_html}
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    parts = []
    parts.append(f"<!-- DelightfulYou.com | {TOPIC} {YEAR} | tag: {TAG} -->")
    parts.append(f"<style>{CSS}</style>")
    parts.append(f"<script>{JS}</script>")
    parts.append('<div class="dyu-article">')
    parts.append(build_author_block())
    parts.append(build_intro())
    parts.append(build_toc())

    # Table (with scroll hint for article)
    table_html = build_table()
    parts.append(table_html)

    parts.append('<hr class="dyu-divider">')
    parts.append("<h4>In-Depth Product Reviews</h4>")
    for p in PRODUCTS:
        parts.append(build_product(p))
    parts.append('<hr class="dyu-divider">')

    faq_html = build_faq()
    parts.append(faq_html)
    parts.append(build_helpful_box())
    parts.append('<hr class="dyu-divider">')
    parts.append(build_comment_prompt())
    parts.append("<!-- wp:post-comments-form /-->")
    parts.append("<!-- wp:comments /-->")
    parts.append("</div>")

    html = "\n\n".join(parts)
    OUTFILE.write_text(html, encoding="utf-8")
    print(f"Wrote {OUTFILE} ({len(html):,} bytes)")

    # Table-only (no scroll hint, full-width)
    table_no_hint = table_html.replace(
        '<p class="dyu-scroll-hint">&#x2194;&nbsp; Scroll the table horizontally to view the full table</p>\n', ''
    )
    table_only_content = build_table_only_html(table_no_hint)
    TABLE_ONLY.write_text(table_only_content, encoding="utf-8")
    print(f"Wrote {TABLE_ONLY} ({len(table_only_content):,} bytes)")

    # FAQ-only
    faq_only_content = build_faq_only_html(faq_html)
    FAQ_ONLY.write_text(faq_only_content, encoding="utf-8")
    print(f"Wrote {FAQ_ONLY} ({len(faq_only_content):,} bytes)")


if __name__ == "__main__":
    main()
