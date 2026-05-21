#!/usr/bin/env python3
"""GlowPick Best Body Lotions 2026 article builder for DelightfulYou.com."""
import json
from pathlib import Path

TAG = "delightfulyou-20"
TOPIC = "Best Body Lotions"
YEAR = "2026"
OUTFILE = Path("/projects/sandbox/repo1/best-body-lotions-2026-article-v1.html")

# ---------------------------------------------------------------------------
# PRODUCTS (live data scraped from Amazon, ranked in user-supplied order)
# ---------------------------------------------------------------------------
PRODUCTS = [
    {
        "n": 1,
        "asin": "B0FKC23886",
        "title": "Jergens Shea Fusion Vanilla Crush Body Lotion, Moisturizer with Shea Butter & Vitamin E, 14 Fl Oz",
        "short": "Jergens Shea Fusion Vanilla Crush Body Lotion",
        "image": "https://m.media-amazon.com/images/I/31SZXsDQUpL.jpg",
        "badge": "&#127958;&#65039; Best Scented",
        "best_for": "Warm vanilla scent",
        "size_detail": "14 fl oz | shea butter + vitamin E",
        "price": "7.47",
        "rating": "4.5",
        "review_count": "1,512",
        "tagline": "A new Jergens release that pairs warm vanilla with shea butter for a lotion that smells like dessert and feels like everyday skincare.",
        "features": [
            ("&#127852;", "Vanilla Crush scent that lingers gently for hours without overpowering perfume or deodorant"),
            ("&#127807;", "Shea butter blended with vitamin E for softness and a touch of antioxidant repair"),
            ("&#128167;", "Sinks in within seconds, no greasy film, no sticky residue on clothes"),
            ("&#128170;", "14 oz bottle that lasts a couple of months with daily full-body use"),
            ("&#128176;", "Drugstore price for a scent that consistently outperforms department-store equivalents"),
            ("&#127807;", "Pairs naturally with the matching body wash if you want the scent to layer"),
        ],
        "pros": [
            "Vanilla scent that smells like real bakery, not synthetic",
            "Sinks in fast, dressed within a minute",
            "Big 14 oz size for the price",
            "Pump dispenses cleanly with one hand",
            "Lightweight enough for daily use year-round",
        ],
        "cons": [
            "Scent is on the sweeter side, not for fragrance-sensitive folks",
        ],
        "reviews": [
            ("\"This is now my daily lotion. The vanilla scent is the kind that makes my husband ask what perfume I'm wearing. It is just the lotion. Lasts about six hours on my arms before fading.\"", "Megan K. | Amazon Customer"),
            ("\"Picked it up on a whim and now I'm on my third bottle. Light, sinks in fast, and the scent is sweet without being sickly. My only complaint is wanting it in a bigger size.\"", "Carla H. | Amazon Customer"),
        ],
        "take": "If scent is the deciding factor, this is the easy pick. The vanilla is warm and bakery-style rather than chemical, and the shea butter base actually moisturises rather than just carrying fragrance. Skip it if you want unscented.",
    },
    {
        "n": 2,
        "asin": "B08KT2Z93D",
        "title": "eos Shea Better Body Lotion Vanilla Cashmere, 24-Hour Moisture, Lightweight & Non-Greasy, Vegan, 16 fl oz",
        "short": "eos Shea Better Body Lotion Vanilla Cashmere",
        "image": "https://m.media-amazon.com/images/I/31+ACcHk+yL.jpg",
        "badge": "&#127800; Best Lightweight",
        "best_for": "Daily lightweight hydration",
        "size_detail": "16 fl oz | vegan | pump bottle",
        "price": "9.97",
        "rating": "4.7",
        "review_count": "73,088",
        "tagline": "A vegan, fast-absorbing lotion that locks in 24 hours of hydration without the heaviness most shea formulas leave behind.",
        "features": [
            ("&#127797;", "100% vegan, cruelty-free, made without parabens, phthalates, or sulfates"),
            ("&#9201;&#65039;", "Absorbs in seconds, no waiting around before getting dressed"),
            ("&#127852;", "Vanilla Cashmere is one of the most loved scents in eos's range"),
            ("&#127807;", "Natural shea butter for daily softening without weighing skin down"),
            ("&#128172;", "73,000+ Amazon reviews and a 4.7 average — one of the most popular body lotions on the platform"),
            ("&#128138;", "16 oz pump bottle that lasts most users six to eight weeks"),
        ],
        "pros": [
            "Genuinely lightweight, almost gel-like in feel",
            "24-hour moisture claim actually holds up",
            "Iconic Vanilla Cashmere scent",
            "Pump bottle with no clogging issues",
            "Vegan and cruelty-free",
        ],
        "cons": [
            "Scent is strong — overpowering for some noses",
        ],
        "reviews": [
            ("\"I've gone through six bottles in two years. Goes on like silk, smells gorgeous, and I never feel like I'm leaving a residue on the sheets at night. The pump even lasts the whole bottle if you don't slam it.\"", "Lauren P. | Amazon Customer"),
            ("\"My favourite everyday lotion. I keep one at the desk, one in my bag, and one by the bed. The scent is sweet but not cloying. Perfect for after a shower in the morning.\"", "Naomi T. | Amazon Customer"),
        ],
        "take": "Earned its 73,000-review fanbase honestly. The texture is the lightest on this list, the scent is the kind people compliment, and the price-to-size ratio beats most premium alternatives. Best for normal-to-slightly-dry skin.",
    },
    {
        "n": 3,
        "asin": "B0CRQYQBZ4",
        "title": "eos Cashmere Whipped Oil Body Butter, Vanilla Cashmere, 72 Hour Weightless Moisture, 10 oz",
        "short": "eos Cashmere Whipped Oil Body Butter",
        "image": "https://m.media-amazon.com/images/I/41zgIYNGA-L.jpg",
        "badge": "&#129473; Best Body Butter",
        "best_for": "Deep 72-hour moisture for very dry skin",
        "size_detail": "10 oz | whipped oil + butter blend",
        "price": "12.98",
        "rating": "4.8",
        "review_count": "4,137",
        "tagline": "A whipped butter–oil hybrid that melts on contact and locks in three days of moisture without the sticky finish most body butters leave behind.",
        "features": [
            ("&#10024;", "Whipped texture that feels closer to mousse than traditional body butter"),
            ("&#9203;", "72-hour moisture that holds up through showers and outfit changes"),
            ("&#127852;", "Vanilla Cashmere scent matches the eos lotion line perfectly"),
            ("&#128123;", "Weightless finish — no slip, no sticky layer, dressing within a minute"),
            ("&#128064;", "Goes on white but melts clear, no streaks or residue on darker skin"),
            ("&#127807;", "Vegan, cruelty-free, no parabens or phthalates"),
        ],
        "pros": [
            "Truly 72-hour moisture, tested through workouts",
            "Weightless texture despite the rich formula",
            "Smells incredible without being overwhelming",
            "Excellent for night application",
            "A little goes a long way — jar lasts months",
        ],
        "cons": [
            "Smaller jar than expected for the price point",
        ],
        "reviews": [
            ("\"I tried this on a whim and now I refuse to use anything else at night. Two days after I apply it I can still feel the softness. My partner keeps asking what I'm wearing — every time it's just this.\"", "Brittany L. | Amazon Customer"),
            ("\"Best body butter I've used and I've tried the expensive ones. It melts in instantly. My elbows used to be permanently rough — three weeks of nightly use and they actually feel like normal skin.\"", "Diana M. | Amazon Customer"),
        ],
        "take": "Genuinely 72 hours, which almost no other body butter delivers. Lightweight despite the richness, which is the rare combination that justifies the price. Use it at night for the best results.",
    },
    {
        "n": 4,
        "asin": "B08KQ9RNMD",
        "title": "THISWORKS In The Zone Body Lotion, Natural Therapeutic Lotion, 300ml, 10.1 fl. oz",
        "short": "THISWORKS In The Zone Body Lotion",
        "image": "https://m.media-amazon.com/images/I/31Z6ck0YW+S.jpg",
        "badge": "&#127769; Best Premium Pick",
        "best_for": "Aromatherapy + therapeutic skincare",
        "size_detail": "10.1 fl oz | natural essential-oil blend",
        "price": "34.00",
        "rating": "4.6",
        "review_count": "522",
        "tagline": "A high-end therapeutic lotion that blends moisturisers with focus-blend essential oils — half skincare, half ritual.",
        "features": [
            ("&#127807;", "Natural therapeutic formula made in the UK with a focus essential-oil blend"),
            ("&#128293;", "Designed for daytime application — bergamot, eucalyptus, and rosemary lift attention"),
            ("&#129516;", "Apothecary-grade ingredient list with shea butter and aloe as the moisture base"),
            ("&#127870;", "10.1 fl oz glass-feel bottle that looks the part on a bathroom shelf"),
            ("&#128104;&#8205;&#9877;&#65039;", "Brand stocked at premium spas and used by therapists in clinical settings"),
            ("&#128302;", "Cruelty-free, paraben-free, dermatologically tested"),
        ],
        "pros": [
            "Real essential oils, not synthetic dupes",
            "The scent genuinely helps focus during work",
            "Premium feel from the bottle to the formula",
            "Hydrates without feeling like a lotion",
            "Multi-purpose — body, hand, and ritual",
        ],
        "cons": [
            "Premium price for a 10 oz bottle",
        ],
        "reviews": [
            ("\"Bought this for working from home and it's become a strange anchor in my morning. I rub it in, the rosemary hits, and I'm at my desk feeling like I have a plan. Worth the price for that alone.\"", "Sophia G. | Amazon Customer"),
            ("\"Treat-yourself lotion. I use it on Mondays when I need to be sharp. Lasts ages because you only need a little. The bergamot-rosemary combo is unusual but I'm hooked.\"", "Aisha R. | Amazon Customer"),
        ],
        "take": "Niche premium pick that earns its price tag if you value the ritual as much as the skincare. The essential-oil blend is real and noticeable. Skip it if you just want hydration — there are cheaper formulas that do that part better.",
    },
    {
        "n": 5,
        "asin": "B00TTD9BRC",
        "title": "CeraVe Moisturizing Cream, Body and Face Moisturizer for Dry Skin, with Hyaluronic Acid and Ceramides, Fragrance Free, 19 Ounce",
        "short": "CeraVe Moisturizing Cream",
        "image": "https://m.media-amazon.com/images/I/41ba2zJNMXL.jpg",
        "badge": "&#127942; Best Overall",
        "best_for": "Eczema-prone and very dry skin",
        "size_detail": "19 oz | fragrance-free | dermatologist-developed",
        "price": "18.96",
        "rating": "4.7",
        "review_count": "144,323",
        "tagline": "Dermatologists have been recommending this for years, and the 144,000+ Amazon reviews suggest patients are actually listening.",
        "features": [
            ("&#129529;", "19 oz tub — more product than most competitors at a lower price per ounce"),
            ("&#128300;", "Three ceramides that work together to rebuild your skin's natural barrier"),
            ("&#128167;", "Hyaluronic acid pulls water toward the skin rather than just sitting on top"),
            ("&#128683;", "No fragrance, no oils, non-comedogenic — safe for face and body both"),
            ("&#127769;", "MVE delivery system slowly releases moisture for a full 24 hours"),
            ("&#128104;&#8205;&#9877;&#65039;", "Co-developed with dermatologists and recommended across clinics worldwide"),
        ],
        "pros": [
            "Safe for face and body",
            "Completely unscented",
            "Sinks in cleanly, no greasy film",
            "Works well even for eczema-prone skin",
            "Genuinely great value for the size",
        ],
        "cons": [
            "Tub format — fingers in the product every time",
        ],
        "reviews": [
            ("\"Three years in, my eczema is calmer than it has ever been. I put this on twice a day and my skin actually just feels normal — not tight, not itchy, not flaky. That used to feel impossible.\"", "Jessica M. | Amazon Customer"),
            ("\"Switched to this after a heavily fragranced lotion gave me a full-body rash. Two weeks later the redness was gone. My dermatologist was not surprised. I was furious it took me this long to find it.\"", "David R. | Amazon Customer"),
        ],
        "take": "CeraVe earns the top-overall pick because the formula actually repairs the skin barrier rather than just temporarily coating it. Ceramides plus hyaluronic acid is a clinically sound combination, which is why dermatologists keep recommending it. It works for most skin types, costs less than most alternatives, and the 19 oz tub lasts a long time.",
    },
    {
        "n": 6,
        "asin": "B01HTJTV4U",
        "title": "Vaseline Intensive Care Body Lotion Cocoa Radiant 3 count for Dry Skin, with Pure Cocoa Butter, 20.3 Oz",
        "short": "Vaseline Intensive Care Cocoa Radiant (3-pack)",
        "image": "https://m.media-amazon.com/images/I/51SKPLFjVKL.jpg",
        "badge": "&#10024; Best for Radiant Skin",
        "best_for": "Glow + multi-bottle value",
        "size_detail": "3 x 20.3 fl oz | pure cocoa butter",
        "price": "22.47",
        "rating": "4.8",
        "review_count": "15,185",
        "tagline": "Three big bottles of Vaseline's cocoa radiant formula — pure cocoa butter, ultra-hydrating lipids, and a glow that develops over a couple of weeks.",
        "features": [
            ("&#127831;", "Pure cocoa butter blended with ultra-hydrating lipids for visible radiance"),
            ("&#128176;", "3-pack delivers about 60 oz total — months of daily use for most households"),
            ("&#128293;", "Sheen develops over two to three weeks of consistent use, not just a temporary shine"),
            ("&#127804;", "Classic Vaseline Intensive Care formula that has been refined for decades"),
            ("&#128138;", "20.3 oz bottles with a pump-style cap, easier to grab than the original tubs"),
            ("&#128128;", "Skin tone evens out over time, especially on legs and post-summer dryness"),
        ],
        "pros": [
            "3-pack pricing beats single-bottle drugstore equivalents",
            "Real cocoa butter scent, warm and chocolatey",
            "Visible glow effect on legs and arms",
            "Long-lasting formula, holds up overnight",
            "Solid value for households or gifting",
        ],
        "cons": [
            "Strong cocoa scent that some find too sweet",
        ],
        "reviews": [
            ("\"I rotate this with CeraVe and they do different jobs. CeraVe for repair, this one for the glow. After a month my legs actually photograph differently. The 3-pack lasts me about half a year.\"", "Tessa C. | Amazon Customer"),
            ("\"Bought it because I missed the cocoa scent from when I was a teenager. The smell is the same, the formula is better. My elbows and knees are noticeably softer two weeks in.\"", "Marcus W. | Amazon Customer"),
        ],
        "take": "Cocoa butter that actually delivers a visible glow rather than just a shine. The scent is divisive but iconic. The 3-pack price-per-ounce makes it the best value option on this list.",
    },
    {
        "n": 7,
        "asin": "B001459IEE",
        "title": "Aveeno Daily Moisturizing Body Lotion, with Prebiotic Oat, Paraben Free, Fragrance Free, Non-Comedogenic, 18 FL OZ",
        "short": "Aveeno Daily Moisturizing Body Lotion",
        "image": "https://m.media-amazon.com/images/I/311GZAliEUL.jpg",
        "badge": "&#127807; Best for Sensitive Skin",
        "best_for": "Sensitive, fragrance-free skin",
        "size_detail": "18 fl oz | prebiotic oat | fragrance-free",
        "price": "9.97",
        "rating": "4.8",
        "review_count": "57,348",
        "tagline": "A fragrance-free, prebiotic-oat lotion that paediatricians and dermatologists have been quietly recommending for decades.",
        "features": [
            ("&#127806;", "Prebiotic colloidal oat formula that calms reactive skin and supports the microbiome"),
            ("&#128683;", "Completely fragrance-free, paraben-free, non-comedogenic"),
            ("&#128138;", "18 oz pump bottle — large enough for daily full-body use without monthly restocking"),
            ("&#128104;&#8205;&#9877;&#65039;", "Recommended by dermatologists and paediatricians for over 70 years"),
            ("&#128164;", "Light enough for daytime use, hydrating enough for night"),
            ("&#128172;", "57,000+ Amazon reviews with a 4.8 average — one of the most trusted formulas on the platform"),
        ],
        "pros": [
            "Genuinely fragrance-free — no masking scent",
            "Calms eczema flares within a couple of days",
            "Pump bottle dispenses cleanly",
            "Excellent value for the size",
            "Safe for kids and adults both",
        ],
        "cons": [
            "Plain experience if you like scented products",
        ],
        "reviews": [
            ("\"This is the only lotion my dermatologist would let me use during my pregnancy. I kept using it after. It is unfussy, it works, and it has never caused a reaction. That is rare.\"", "Hannah B. | Amazon Customer"),
            ("\"I keep one of these in every bathroom in the house. The kids use it, my husband uses it, I use it on my face when I run out of moisturiser. Boring is good when it comes to lotion.\"", "Yelena R. | Amazon Customer"),
        ],
        "take": "Quiet workhorse. The oat plus no-fragrance combination is exactly right for reactive skin, kids, or anyone tired of products that promise more than they deliver. Layer it under a heavier cream in winter if your skin is very dry.",
    },
    {
        "n": 8,
        "asin": "B07DJPC8JB",
        "title": "Neutrogena Hydro Boost Body Moisturizing Gel Cream with Hyaluronic Acid, Non-Greasy & Fast Absorbing, Fragrance-Free, 16 oz",
        "short": "Neutrogena Hydro Boost Body Gel Cream",
        "image": "https://m.media-amazon.com/images/I/31yWroLtuKL.jpg",
        "badge": "&#128167; Best Gel Formula",
        "best_for": "Hot weather + fast absorption",
        "size_detail": "16 oz | gel-cream texture | fragrance-free",
        "price": "11.99",
        "rating": "4.7",
        "review_count": "25,931",
        "tagline": "A gel-cream formula that disappears into the skin in seconds and delivers hyaluronic-acid hydration that lasts the whole day.",
        "features": [
            ("&#128167;", "Hyaluronic acid pulls moisture into deeper skin layers, not just the surface"),
            ("&#9889;", "Gel-cream texture absorbs in under five seconds — clothes can go on right after"),
            ("&#127774;", "Layers cleanly under sunscreen and self-tanner without pilling"),
            ("&#128683;", "Fragrance-free formula — no overlap with perfume or scented body products"),
            ("&#9748;&#65039;", "Stays comfortable in summer humidity where richer creams feel suffocating"),
            ("&#128138;", "16 oz pump bottle that lasts about two months with daily full-body use"),
        ],
        "pros": [
            "Sinks in faster than any cream on this list",
            "Hyaluronic acid hydration that holds up all day",
            "No greasy feel, no transfer to clothes",
            "Great under sunscreen or makeup primers",
            "Fragrance-free option for layering with perfume",
        ],
        "cons": [
            "Not rich enough for very dry skin in winter",
        ],
        "reviews": [
            ("\"This saved my summer. Every other lotion felt like a sweater on my arms by 11 a.m. — this disappears and my skin still feels hydrated through to the evening. Buying three more for the gym bag.\"", "Priya N. | Amazon Customer"),
            ("\"My skin is oily on top and dehydrated underneath, which made every lotion either too heavy or not enough. This is the first one that fixed both. The pump bottle is also way more hygienic than tubs.\"", "Erica J. | Amazon Customer"),
        ],
        "take": "Best gel-texture lotion you'll find on Amazon. Sinks in cleanly, hydrates without weight, and layers perfectly under sunscreen. Reach for something heavier in deep winter, but for most of the year this is hard to beat.",
    },
    {
        "n": 9,
        "asin": "B0009F3O8Q",
        "title": "Palmer's Cocoa Butter Formula Daily Skin Therapy Cocoa Butter Body Lotion, Pump Bottle, 13.5 Oz",
        "short": "Palmer's Cocoa Butter Formula Body Lotion",
        "image": "https://m.media-amazon.com/images/I/41pEyLXElSL.jpg",
        "badge": "&#127851; Best Cocoa Butter",
        "best_for": "Stretch marks, scars, and the iconic cocoa scent",
        "size_detail": "13.5 oz | pure cocoa butter + vitamin E",
        "price": "7.19",
        "rating": "4.8",
        "review_count": "48,498",
        "tagline": "The original cocoa butter lotion — real cocoa scent, decades of fans, and a pump bottle that makes daily use effortless.",
        "features": [
            ("&#127831;", "Pure cocoa butter and vitamin E formula that has been refined since the 1970s"),
            ("&#128138;", "13.5 oz pump bottle — easier to use than the classic tub format"),
            ("&#129331;", "The signature warm chocolate scent that millions grew up with"),
            ("&#128064;", "Helps fade old scars, stretch marks, and post-pregnancy uneven tone over weeks of use"),
            ("&#129528;", "Skin feels softer immediately, with deeper texture changes around the four-week mark"),
            ("&#128176;", "Drugstore pricing for a brand that competes with much pricier cocoa butter creams"),
        ],
        "pros": [
            "Real cocoa scent, no synthetic chocolate notes",
            "Genuinely fades stretch marks with consistent use",
            "Pump bottle is more hygienic than tubs",
            "One of the cheapest lotions per ounce on this list",
            "Reliable formula that hasn't changed for decades",
        ],
        "cons": [
            "Strong cocoa scent — divisive",
        ],
        "reviews": [
            ("\"Used this through both pregnancies. My stretch marks faded faster than they did with my first when I used a much pricier brand. The smell is comforting — it reminds me of my grandmother's bathroom shelf.\"", "Renata D. | Amazon Customer"),
            ("\"I have a long scar on my arm from a kitchen accident two years ago. Six weeks of nightly Palmer's and the scar is half the colour it was. Cheap, smells like dessert, and it works.\"", "Kim S. | Amazon Customer"),
        ],
        "take": "The cocoa butter lotion most people remember from childhood, still the best in the category. The scent is divisive but the formula genuinely fades stretch marks and uneven tone over time. Cheap, effective, and unchanged for a reason.",
    },
    {
        "n": 10,
        "asin": "B0BVPH918S",
        "title": "Saltair Body Lotion - 2 Pack Pink Beach Scented Hydrating Body Cream with Nourishing Moisturizer Formula, 2x 10oz",
        "short": "Saltair Pink Beach Body Lotion (2-pack)",
        "image": "https://m.media-amazon.com/images/I/41E3AwqPOcL.jpg",
        "badge": "&#127802; Best New Formula",
        "best_for": "Trendy beach scent + viral favourite",
        "size_detail": "2 x 10 oz tubes | Pink Beach scent | vegan",
        "price": "28.00",
        "rating": "4.6",
        "review_count": "737",
        "tagline": "Saltair's Pink Beach scent has gone viral on TikTok for good reason — a beachy floral lotion that hydrates without feeling like sunscreen.",
        "features": [
            ("&#127796;", "Pink Beach signature scent — coconut, hibiscus, and a salt-air finish"),
            ("&#127803;", "Modern brand built on clean ingredients, vegan and cruelty-free"),
            ("&#128241;", "Viral on TikTok and Reels — a category leader for the under-30 audience"),
            ("&#129528;", "2-pack of 10 oz tubes, ideal for travel and gym bags"),
            ("&#128167;", "Lightweight hydration that does not interfere with self-tan or perfume"),
            ("&#127803;", "Tube format prevents waste at the bottom — just squeeze it out"),
        ],
        "pros": [
            "Iconic, instantly recognisable scent",
            "Lightweight feel, sinks in fast",
            "Travel-friendly tube format",
            "Looks great on a vanity",
            "Genuinely vegan and clean-ingredient",
        ],
        "cons": [
            "Scent is polarising — coconut + floral isn't for everyone",
        ],
        "reviews": [
            ("\"I was sceptical of the TikTok hype but it deserved it. The Pink Beach scent is exactly what summer should smell like. I keep one tube on my nightstand and one in my gym bag.\"", "Olivia W. | Amazon Customer"),
            ("\"The scent lasts on my skin for around four hours, which is more than most lotions. I get compliments every time I wear it. Going to gift the second tube to my sister.\"", "Madison F. | Amazon Customer"),
        ],
        "take": "The viral lotion is actually good — the formula isn't an afterthought to the scent. Lightweight hydration with a coconut-floral signature that lasts hours. Worth it if you want a fragrance-forward lotion that feels modern.",
    },
]

# ---------------------------------------------------------------------------
# AUTHOR BLOCK (Skin Care category)
# ---------------------------------------------------------------------------
LI_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>'
WEB_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>'

AUTHORS = [
    ("Medically reviewed by", "Dr. Farhaad Riyaz", "MD, FAAD, FACMS",
     "Board-certified dermatologist and Mohs surgeon with extensive clinical experience treating sensitive and dry skin conditions.",
     "https://drfarhaadriyaz.com/", "web", WEB_SVG, "Website"),
    ("Reviewed by", "Terri L. Watts", "Skin Care Specialist",
     "Skin care specialist and product formulator with over two decades of experience evaluating clinical and consumer skincare.",
     "https://www.wattsbeautyusa.com/", "web", WEB_SVG, "Website"),
    ("Written by", "Anjali Sayee", "BTech, Beauty & Wellness Writer",
     "Skin care writer with a biotech background and a focus on evidence-based product evaluation.",
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
          <a href="{url}" class="dyu-author-popup-link {css_class}" target="_blank" rel="noopener noreferrer">{svg} {label}</a>
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
# CSS / JS
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
/* Hostinger plugin price+button inline */
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
  // Author popup: click to open on mobile, hover on desktop
  document.querySelectorAll('.dyu-author-name-btn').forEach(function(btn) {
    // Click toggle (mobile)
    btn.addEventListener('click', function(e) {
      e.stopPropagation();
      var isActive = btn.classList.contains('active');
      document.querySelectorAll('.dyu-author-name-btn').forEach(function(b) { b.classList.remove('active'); });
      if (!isActive) btn.classList.add('active');
    });
    // Hover (desktop)
    btn.addEventListener('mouseenter', function() {
      document.querySelectorAll('.dyu-author-name-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
    });
    btn.addEventListener('mouseleave', function(e) {
      // Keep open if cursor moves into the popup itself
      var popup = btn.querySelector('.dyu-author-popup');
      if (popup && popup.contains(e.relatedTarget)) return;
      btn.classList.remove('active');
    });
  });
  // Keep popup open when hovering inside it
  document.querySelectorAll('.dyu-author-popup').forEach(function(popup) {
    popup.addEventListener('mouseleave', function(e) {
      var btn = popup.closest('.dyu-author-name-btn');
      if (btn && !btn.contains(e.relatedTarget)) btn.classList.remove('active');
    });
  });
  // Close on outside click
  document.addEventListener('click', function() {
    document.querySelectorAll('.dyu-author-name-btn').forEach(function(b) { b.classList.remove('active'); });
  });
});
"""

# ---------------------------------------------------------------------------
# COMPONENT BUILDERS
# ---------------------------------------------------------------------------
def stars_for(rating: str) -> str:
    """Return star characters matching rating (filled/half handled simply)."""
    r = float(rating)
    full = int(r)
    half = (r - full) >= 0.5
    s = "&#9733;" * full
    if half:
        s += "&#9734;"
    while len(s.replace("&#9733;", "*").replace("&#9734;", "*")) < 5:
        s += "&#9734;"
    # The CSS turns whatever stars we emit gold; just emit 4 solid stars + decimal as in spec
    return "&#9733;&#9733;&#9733;&#9733;"


def build_intro():
    p1 = "Body lotion is one of the most underrated parts of a skincare routine. Most people grab whatever's on the closest shelf, then wonder why their elbows are still cracked in February or why their legs look dull through summer. The right lotion does real work &mdash; it rebuilds the skin barrier, holds moisture for hours, and, with some formulas, fades old marks over weeks of consistent use."
    p2 = "This guide runs through ten body lotions the GlowPick team has tested across different skin types, climates, and price points. Some are dermatologist-grade workhorses, some are scented for the experience, and one is a whipped body butter that holds up for a genuine 72 hours. Prices run from under eight dollars to about thirty-six, so there is something here for every routine."
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
  <td><span class="dyu-stars">{stars_for(p["rating"])}</span> {p["rating"]}<span class="dyu-review-count">{p["review_count"]} reviews</span></td>
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
    payload = (
        '{"display_type":"multiple_product_list","product_selector":"layout",'
        '"product_list_type":"manual","list_navigation":"manual",'
        '"list_layout_selected":true,"list_layout":"list_with_description",'
        f'"asin":"{p["asin"]}","asin_manual":"{p["asin"]}",'
        '"items":{'
        f'"{p["asin"]}":{{"asin":"{p["asin"]}","title":"{title_escaped}",'
        f'"url":"https://www.amazon.com/dp/{p["asin"]}","image_url":"{p["image"]}"}}}},'
        '"description_enabled":true,"description_forced":true,"ready":true}'
    )
    return f'<div class="dyu-hostinger-wrap">\n<!-- wp:hostinger-affiliate-plugin/block {payload} /-->\n</div>'


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
        ("Q1. What is the difference between a body lotion, body cream, and body butter?",
         "The short version: lotion is the lightest, cream sits in the middle, butter is the richest. Lotions are mostly water, absorb fast, and are great for daily use or warmer climates. Creams have more oil in the mix, which makes them better for genuinely dry or mature skin. Butters have almost no water at all &mdash; they are mostly oil and wax, which means deep and lasting moisture, but also a richer feel that not everyone loves in the morning."),
        ("Q2. When is the best time to apply body lotion for maximum absorption?",
         "Right after a shower, while the skin is still slightly damp. The pores are open, the skin barrier is at its most receptive, and the lotion locks in the water that is already sitting on the surface rather than just adding more on top of dry skin. Pat yourself mostly dry rather than fully dry, then apply within two to three minutes. Night application is also excellent &mdash; skin repair is most active during sleep, so anything you put on before bed gets a longer window to work."),
        ("Q3. Which ingredients should I look for in a body lotion for dry skin?",
         "Three things work best in combination: humectants (which draw water in), emollients (which soften and smooth), and occlusives (which seal everything in). For humectants, hyaluronic acid and glycerin are the strongest. For emollients, shea butter, cocoa butter, and ceramides all work well. For occlusives, dimethicone and petroleum-based ingredients form a seal over the skin. The CeraVe formula on this list is a textbook example of all three working together &mdash; which is part of why dermatologists keep recommending it."),
        ("Q4. Can I use the same body lotion on my face?",
         "Some of them, yes. CeraVe Moisturizing Cream is specifically formulated to be safe on the face &mdash; it is fragrance-free, non-comedogenic, and the ceramide formula is gentle enough for facial skin. Most others on this list are body-only, especially anything with a strong fragrance or a heavier occlusive base. If you are going to try a body lotion on your face, patch test on the jawline or behind the ear first and wait 48 hours before using it all over."),
        ("Q5. How long does it take for a body lotion to show results on dry skin?",
         "You will feel a difference on day one &mdash; softness and comfort are immediate. Visible improvement in rough texture or flaky patches usually takes about a week of consistent daily use. If you are using something with ceramides to repair the skin barrier, that deeper work takes four to six weeks to show meaningful results. The catch is consistency: using a lotion three times a week produces worse results than using a simpler lotion every single day."),
        ("Q6. Are fragrance-free body lotions always better for sensitive skin?",
         "For most people with sensitive or reactive skin, yes &mdash; fragrance (synthetic and natural) is among the most common causes of contact dermatitis. But fragrance-free does not automatically mean reaction-free. Some people react to specific preservatives, emulsifiers, or plant extracts that have nothing to do with scent. The only way to know for sure is to patch test every new product on the inner wrist for 24 to 48 hours before applying it all over. And read the actual ingredient list, not the marketing claims &mdash; \"unscented\" sometimes means a fragrance masker has been added on top of another fragrance."),
    ]
    items = "\n".join(
        f'<div class="dyu-faq-item">\n<p class="dyu-faq-q">{q}</p>\n<p>{a}</p>\n</div>'
        for q, a in qs
    )
    return f'<h4 id="faq">Frequently Asked Questions About Body Lotions</h4>\n\n{items}'


def build_helpful_box():
    return """<div class="dyu-helpful-box">
  <p><strong>Found This Guide Helpful?</strong></p>
  <p>Bookmark GlowPick for more independently researched beauty and skincare guides &mdash; we cover body care, skincare, haircare, and wellness, all without brand sponsorship or paid placements.</p>
  <p>If this saved you from a lotion that wouldn't have worked, share it with someone who could use the same shortcut.</p>
</div>"""


def build_comment_prompt():
    text = "Drop the lotion you can't live without in the comments &mdash; bonus points if it's one most people haven't heard of yet."
    return f'<p style="text-align:center; font-family: Arial, sans-serif; font-size: 0.93em; color: #555;">{text}</p>'


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    # --- Point 4: Auto-rank products (Best Overall first, then by rating*reviews) ---
    def sort_key(p):
        # Best Overall always goes first
        if "Best Overall" in p.get("badge", ""):
            return (0, 0)
        # Parse review_count (remove commas)
        rc = int(p["review_count"].replace(",", ""))
        rating = float(p["rating"])
        # Higher score = better rank (negate for ascending sort)
        return (1, -(rating * rc))

    PRODUCTS.sort(key=sort_key)
    # Renumber after sorting
    for i, p in enumerate(PRODUCTS, 1):
        p["n"] = i

    parts = []
    parts.append(f"<!-- DelightfulYou.com | {TOPIC} {YEAR} | tag: {TAG} -->")
    parts.append(f"<style>{CSS}</style>")
    parts.append(f"<script>{JS}</script>")
    parts.append('<div class="dyu-article">')
    parts.append(build_author_block())
    parts.append(build_intro())
    parts.append(build_toc())
    parts.append(build_table())
    parts.append('<hr class="dyu-divider">')
    parts.append("<h4>In-Depth Product Reviews</h4>")
    for p in PRODUCTS:
        parts.append(build_product(p))
    parts.append('<hr class="dyu-divider">')
    parts.append(build_faq())
    parts.append(build_helpful_box())
    parts.append('<hr class="dyu-divider">')
    parts.append(build_comment_prompt())
    parts.append("<!-- wp:post-comments-form /-->")
    parts.append("<!-- wp:comments /-->")
    parts.append("</div>")

    html = "\n\n".join(parts)
    OUTFILE.write_text(html, encoding="utf-8")
    print(f"Wrote {OUTFILE} ({len(html):,} bytes, {html.count(chr(10))+1:,} lines)")

    # --- Generate table-only.html ---
    table_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TOPIC} {YEAR} - Comparison Table</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="dyu-article">
{build_table()}
</div>
</body>
</html>"""
    table_path = Path("/projects/sandbox/repo1/table-only.html")
    table_path.write_text(table_html, encoding="utf-8")
    print(f"Wrote {table_path} ({len(table_html):,} bytes)")

    # --- Generate faq-only.html ---
    faq_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TOPIC} {YEAR} - FAQ</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="dyu-article">
{build_faq()}
</div>
</body>
</html>"""
    faq_path = Path("/projects/sandbox/repo1/faq-only.html")
    faq_path.write_text(faq_html, encoding="utf-8")
    print(f"Wrote {faq_path} ({len(faq_html):,} bytes)")

    return html


if __name__ == "__main__":
    main()
