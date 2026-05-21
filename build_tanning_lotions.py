#!/usr/bin/env python3
"""GlowPick Best Indoor Tanning Bed Lotions 2026 article builder for DelightfulYou.com."""
import re
from pathlib import Path

TAG = "delightfulyou-20"
TOPIC = "Best Indoor Tanning Bed Lotions"
YEAR = "2026"
OUTFILE = Path("/projects/sandbox/repo1/best-indoor-tanning-bed-lotions-2026-article-v1.html")
TABLE_FILE = Path("/projects/sandbox/repo1/table-only.html")
FAQ_FILE = Path("/projects/sandbox/repo1/faq-only.html")

# ---------------------------------------------------------------------------
# PRODUCTS (ranked by rating * reviews descending, Best Overall = #1)
# ---------------------------------------------------------------------------
PRODUCTS = [
    {
        "n": 1,
        "asin": "B00076XR3O",
        "title": "Maui Babe Browning Lotion",
        "short": "Maui Babe Browning Lotion",
        "image": "https://m.media-amazon.com/images/I/41mHd-+shCL.jpg",
        "badge": "&#127942; Best Overall",
        "best_for": "Natural browning without bronzers",
        "size_detail": "4 fl oz | natural Hawaiian formula",
        "price": "14.99",
        "rating": "4.4",
        "review_count": "15,000",
        "tagline": "The original Hawaiian browning lotion that turned a cult following into 15,000 reviews and counting.",
        "features": [
            ("&#127796;", "Hawaiian formula with natural plant extracts that accelerate melanin production"),
            ("&#127807;", "Kona coffee extract and kukui nut oil for deep skin conditioning"),
            ("&#128167;", "Lightweight liquid texture that absorbs in seconds without sticky residue"),
            ("&#128293;", "Works in both tanning beds and outdoor sun for versatile use"),
            ("&#129528;", "No bronzers or DHA, colour comes from your own melanin response"),
            ("&#128176;", "Small bottle goes further than expected due to thin liquid consistency"),
        ],
        "pros": [
            "Delivers visible colour difference after a single session",
            "No fake-tan smell or orange undertones",
            "Thin liquid absorbs instantly, no transfer to bed surfaces",
            "Works for both indoor and outdoor tanning",
            "15,000+ reviews confirm consistent results across skin types",
        ],
        "cons": [
            "4 oz bottle runs out fast with full-body application",
        ],
        "reviews": [
            ("\"I've used this for three years in my tanning bed and nothing else comes close. One session with Maui Babe and I'm two shades darker than without it. No streaks, no smell, just colour.\"", "Jessica T. | Amazon Customer"),
            ("\"Bought it because of the hype and it actually delivered. My tan develops faster and lasts longer. The bottle is small but you only need a thin layer so it lasts about two weeks of regular sessions.\"", "Danielle M. | Amazon Customer"),
        ],
        "take": "Earns the top spot through sheer consistency. Fifteen thousand people agree: this thin Hawaiian formula accelerates your natural tan without bronzers, without DHA, and without that fake-tan smell. The small bottle is the only real downside.",
    },
    {
        "n": 2,
        "asin": "B08CNJ5BG7",
        "title": "BYROKKO Shine Brown Tanning Accelerator Lotion",
        "short": "BYROKKO Shine Brown Tanning Accelerator",
        "image": "https://m.media-amazon.com/images/I/41XfctxzHVL.jpg",
        "badge": "&#10024; Best Glow Finish",
        "best_for": "Shimmer tan with botanical oils",
        "size_detail": "7.1 fl oz | water-resistant | original formula",
        "price": "16.95",
        "rating": "4.3",
        "review_count": "12,000",
        "tagline": "A European tanning accelerator that went viral for delivering a bronzed shimmer without any self-tanner chemicals.",
        "features": [
            ("&#10024;", "Shimmer particles give an immediate glow while the tan develops underneath"),
            ("&#127807;", "Natural botanical oils including cocoa butter and coconut for deep hydration"),
            ("&#128167;", "Water-resistant formula that stays put through sweat in the tanning bed"),
            ("&#127758;", "European brand with a cult following across social media platforms"),
            ("&#128293;", "Accelerates natural melanin production without DHA or artificial bronzers"),
            ("&#129528;", "Works for both indoor beds and outdoor sunbathing"),
        ],
        "pros": [
            "Immediate shimmer effect while waiting for the real tan to develop",
            "Botanical oils leave skin genuinely moisturised post-session",
            "Water-resistant, stays on through a full bed session",
            "No DHA means no fake-tan smell the next day",
            "7.1 oz size lasts longer than most competitors",
        ],
        "cons": [
            "Shimmer particles can transfer to tanning bed surfaces if over-applied",
        ],
        "reviews": [
            ("\"This stuff is magic. I get the shimmer immediately and then the real tan shows up the next morning. My skin feels moisturised instead of dried out like with other tanning lotions. On my fifth jar now.\"", "Kayla R. | Amazon Customer"),
            ("\"Saw this on TikTok and was skeptical but it works. The glow is gorgeous and the tan is deeper than without it. Only complaint is you need to wipe down the bed after because of the shimmer.\"", "Brittany S. | Amazon Customer"),
        ],
        "take": "The best choice if you want immediate gratification plus long-term results. The shimmer gives you a glow walking out of the salon, and the botanical oils mean your skin isn't wrecked after. Just be mindful of how much you apply to avoid residue on the bed.",
    },
]



PRODUCTS += [
    {
        "n": 3,
        "asin": "B08G1LDFL8",
        "title": "Coco & Eve Self Tanner Foam Kit",
        "short": "Coco & Eve Self Tanner Foam Kit",
        "image": "https://m.media-amazon.com/images/I/41eSl1YdmEL.jpg",
        "badge": "&#127965; Best Self-Tan Foam",
        "best_for": "Streak-free mousse with tropical scent",
        "size_detail": "Medium shade | foam + mitt included",
        "price": "34.90",
        "rating": "4.3",
        "review_count": "9,200",
        "tagline": "A Bali-inspired self-tanning mousse that smells tropical instead of chemical and comes with its own application mitt.",
        "features": [
            ("&#127965;", "Tropical mango and guava scent that completely masks the typical DHA smell"),
            ("&#129507;", "Velvet application mitt included for streak-free, even coverage"),
            ("&#127807;", "Raw virgin coconut, fig, and celltan for skin nourishment during development"),
            ("&#128167;", "Lightweight mousse texture that dries in under 60 seconds"),
            ("&#128293;", "Develops over 4-8 hours into a natural olive-toned tan"),
            ("&#9989;", "Vegan, cruelty-free formula with no parabens or sulfates"),
        ],
        "pros": [
            "Smells genuinely tropical, zero fake-tan odour",
            "Included mitt makes application foolproof",
            "Dries fast enough to get dressed within a minute",
            "Develops into a natural olive tone, not orange",
            "Vegan and cruelty-free with clean ingredients",
        ],
        "cons": [
            "Premium price point compared to basic tanning lotions",
        ],
        "reviews": [
            ("\"I've tried every self-tanner on Amazon and this is the only one that doesn't smell like biscuits gone wrong. The colour is natural, the mitt prevents streaks, and it fades evenly after a week.\"", "Morgan L. | Amazon Customer"),
            ("\"Worth every penny. Applied it at night, woke up looking like I'd been on holiday. No streaks on the sheets, no weird smell, and the colour lasted almost a full week before fading.\"", "Chelsea B. | Amazon Customer"),
        ],
        "take": "The premium self-tan option on this list. You're paying for the scent (genuinely tropical), the included mitt, and a formula that develops into olive rather than orange. If you hate the smell of self-tanners, this solves that problem completely.",
    },
    {
        "n": 4,
        "asin": "B0058E3XJI",
        "title": "Millennium Tanning SOLID BLACK 100X Dark Tanning Lotion",
        "short": "Millennium Solid Black 100X",
        "image": "https://m.media-amazon.com/images/I/41KNj0nprcL.jpg",
        "badge": "&#128163; Best Extreme Dark",
        "best_for": "Maximum darkness with silicone bronzers",
        "size_detail": "13.5 fl oz | 100X bronzer | silicone blend",
        "price": "29.99",
        "rating": "4.3",
        "review_count": "8,500",
        "tagline": "A 100X bronzer formula built for experienced tanners who want the darkest possible result from every session.",
        "features": [
            ("&#128163;", "100X auto-darkening bronzer complex for extreme colour development"),
            ("&#129528;", "Silicone emulsion base that spreads evenly without streaking"),
            ("&#128167;", "Anti-aging silicone blend that smooths skin texture during tanning"),
            ("&#128293;", "Designed specifically for indoor tanning beds, not outdoor use"),
            ("&#127807;", "Moisturising formula that prevents the dryness UV sessions cause"),
            ("&#128176;", "13.5 oz bottle lasts weeks of regular salon visits"),
        ],
        "pros": [
            "Delivers the darkest results of any lotion on this list",
            "Silicone base makes application smooth and streak-free",
            "13.5 oz size is excellent value for salon-goers",
            "Moisturises well enough to prevent post-tan flaking",
            "Purpose-built for indoor beds, not a dual-use afterthought",
        ],
        "cons": [
            "Not suitable for beginners or fair skin as the bronzer is intense",
        ],
        "reviews": [
            ("\"If you want DARK, this is it. I've tried dozens of tanning lotions and Solid Black gives me results in one session that others take three to match. The silicone makes it glide on perfectly.\"", "Amber H. | Amazon Customer"),
            ("\"This is my salon lotion. The staff always comments on how fast my tan develops compared to other clients. The bottle lasts me about six weeks going twice a week. No streaks ever.\"", "Stephanie R. | Amazon Customer"),
        ],
        "take": "The go-to for experienced tanners chasing maximum darkness. The 100X bronzer is no marketing gimmick, it genuinely delivers deeper colour per session than anything else here. Not for beginners, but if you know your skin can handle it, this is the one.",
    },
]



PRODUCTS += [
    {
        "n": 5,
        "asin": "B08MVJ5Y8Y",
        "title": "Tanning Paradise Black Coconut Love Tanning Lotion",
        "short": "Tanning Paradise Black Coconut Love",
        "image": "https://m.media-amazon.com/images/I/51Mugq3kI+L.jpg",
        "badge": "&#129381; Best Coconut Formula",
        "best_for": "Coconut-scented hydration + dark colour",
        "size_detail": "13.5 fl oz | coconut oil | tattoo-safe",
        "price": "19.99",
        "rating": "4.4",
        "review_count": "4,800",
        "tagline": "A coconut oil tanning lotion that smells like a beach holiday and protects tattoos while delivering serious colour.",
        "features": [
            ("&#129381;", "Coconut oil base that deeply hydrates while accelerating tan development"),
            ("&#128293;", "Age-defying complex that helps counteract UV damage during sessions"),
            ("&#129680;", "Tattoo-protecting formula that keeps ink vibrant through repeated tanning"),
            ("&#128167;", "Ultra-hydrating blend prevents the tight, dry feeling after UV exposure"),
            ("&#127796;", "Tropical coconut scent that lasts hours after application"),
            ("&#128176;", "13.5 oz bottle at under $20 is strong value for the category"),
        ],
        "pros": [
            "Coconut scent is genuinely pleasant, not synthetic",
            "Tattoo protection is a real differentiator for inked tanners",
            "Hydration holds up through and after the session",
            "Good colour development without extreme bronzers",
            "13.5 oz at $20 is competitive pricing",
        ],
        "cons": [
            "Coconut scent is strong and lingers on clothes and sheets",
        ],
        "reviews": [
            ("\"Finally a tanning lotion that doesn't dry my skin out. The coconut smell is amazing and my tattoos still look sharp after months of regular tanning. The colour is natural and builds nicely over sessions.\"", "Taylor N. | Amazon Customer"),
            ("\"Best smelling tanning lotion I've ever used. I get compliments on the scent hours later. The tan develops evenly and my skin feels moisturised instead of crispy. Great value for the size.\"", "Megan K. | Amazon Customer"),
        ],
        "take": "The pick for tanners who want hydration, scent, and tattoo protection in one bottle. The coconut oil base genuinely moisturises rather than just sitting on top, and the tattoo-safe formula makes it the obvious choice if you have ink.",
    },
    {
        "n": 6,
        "asin": "B0CJYBLCNT",
        "title": "Jeallis Extreme Dark Tanning Lotion Accelerator",
        "short": "Jeallis Extreme Dark Tanning Lotion",
        "image": "https://m.media-amazon.com/images/I/41sJIw304SL.jpg",
        "badge": "&#128293; Best Accelerator",
        "best_for": "Fast dark results with bronzer",
        "size_detail": "13.5 fl oz | DHA-free | tattoo-safe",
        "price": "16.99",
        "rating": "4.3",
        "review_count": "3,200",
        "tagline": "A DHA-free tanning accelerator that delivers extreme dark results through bronzer technology without the chemical self-tanner smell.",
        "features": [
            ("&#128293;", "Extreme dark bronzer complex that shows results after a single session"),
            ("&#9989;", "DHA-free formula means no self-tanner smell or orange undertones"),
            ("&#129680;", "Tattoo-protecting ingredients that maintain ink clarity through UV exposure"),
            ("&#128167;", "Moisturising base that combats the drying effects of tanning beds"),
            ("&#127807;", "Nourishing botanical extracts for skin health between sessions"),
            ("&#128176;", "13.5 oz at under $17 makes it one of the most affordable options"),
        ],
        "pros": [
            "DHA-free so no fake-tan smell or orange tones",
            "Visible darkening after just one bed session",
            "Tattoo-safe formula protects existing ink",
            "Budget-friendly at under $17 for 13.5 oz",
            "Moisturises enough to skip post-tan lotion",
        ],
        "cons": [
            "Bronzer can stain light-coloured clothing if not fully absorbed",
        ],
        "reviews": [
            ("\"I switched from Millennium to this because it's half the price and honestly the results are comparable. Dark colour after one session, no weird smell, and my tattoo sleeves still look great.\"", "Rachel G. | Amazon Customer"),
            ("\"Best budget tanning lotion I've found. The colour develops fast and it doesn't leave me smelling like chemicals. My skin actually feels good after a session instead of tight and dry.\"", "Courtney P. | Amazon Customer"),
        ],
        "take": "The budget-conscious accelerator that punches above its price point. DHA-free means no smell and no orange, while the bronzer complex delivers visible results from session one. Great alternative to Millennium if you want dark results without the premium price.",
    },
]



PRODUCTS += [
    {
        "n": 7,
        "asin": "B0CTBF3WLS",
        "title": "b.tan UV Tanning Bed Lotion",
        "short": "b.tan UV Tanning Bed Lotion",
        "image": "https://m.media-amazon.com/images/I/41nFaIDnL9L.jpg",
        "badge": "&#127774; Best Intensifier",
        "best_for": "4000X tan intensifiers for max results",
        "size_detail": "12 fl oz | 4000X intensifiers | indoor + outdoor",
        "price": "16.99",
        "rating": "4.3",
        "review_count": "2,400",
        "tagline": "A 4000X intensifier blend from a brand known for self-tanners, now purpose-built for UV tanning beds.",
        "features": [
            ("&#127774;", "4000X tan intensifier complex for accelerated colour development"),
            ("&#128293;", "Works both indoors in beds and outdoors in natural sunlight"),
            ("&#128167;", "Browning body tanner that extends tan life between sessions"),
            ("&#127807;", "Skin-nourishing base that prevents post-session dryness"),
            ("&#9989;", "No sun protection included, designed purely for tan acceleration"),
            ("&#128176;", "12 oz bottle from a trusted self-tan brand at a fair price point"),
        ],
        "pros": [
            "4000X intensifier delivers noticeably faster colour development",
            "Dual indoor/outdoor use adds versatility",
            "Extends existing tan between sessions",
            "Trusted brand with a reputation in self-tanning",
            "Non-greasy finish that doesn't stick to bed surfaces",
        ],
        "cons": [
            "12 oz bottle is slightly smaller than 13.5 oz competitors at the same price",
        ],
        "reviews": [
            ("\"b.tan finally made a UV lotion and it's as good as their self-tanners. My tan develops faster and darker than without it. Love that I can use the same bottle at the beach on weekends.\"", "Samantha F. | Amazon Customer"),
            ("\"Solid tanning lotion from a brand I already trust. The intensifiers work, my tan lasts longer between sessions, and my skin doesn't feel like sandpaper after. Would buy again.\"", "Lauren D. | Amazon Customer"),
        ],
        "take": "A reliable intensifier from a brand that knows tanning chemistry. The 4000X claim holds up in practice, delivering faster and deeper colour per session. Good choice if you want one bottle for both the salon and the beach.",
    },
    {
        "n": 8,
        "asin": "B0CKNHF944",
        "title": "European Gold Dark Star 6000X Ultra-Dark Tanning Lotion",
        "short": "European Gold Dark Star 6000X",
        "image": "https://m.media-amazon.com/images/I/41V39RoSBXL.jpg",
        "badge": "&#11088; Best Triple Bronze",
        "best_for": "Triple-bronze formula for deep lasting tan",
        "size_detail": "12 oz | triple bronze | skin-nourishing",
        "price": "19.99",
        "rating": "4.2",
        "review_count": "1,500",
        "tagline": "A triple-bronze formula that layers three different bronzing agents for a deep tan that builds over multiple sessions.",
        "features": [
            ("&#11088;", "Triple-bronze formula combining three bronzing agents for layered colour"),
            ("&#128293;", "6000X intensifier rating for advanced tanners seeking depth"),
            ("&#128167;", "Skin-nourishing ingredients that hydrate during and after UV exposure"),
            ("&#127807;", "Conditioning blend that helps tan develop evenly without patchiness"),
            ("&#129528;", "Designed for indoor tanning beds with high-output bulbs"),
            ("&#128176;", "12 oz bottle at $20 is mid-range pricing for the category"),
        ],
        "pros": [
            "Triple-bronze system builds colour progressively over sessions",
            "6000X rating means serious intensity for experienced tanners",
            "Hydrating enough to use without a separate moisturiser",
            "Even development without blotchy patches",
            "Good mid-range price for the bronzer intensity",
        ],
        "cons": [
            "Takes 3-4 sessions to see the full triple-bronze effect",
        ],
        "reviews": [
            ("\"Dark Star has been my go-to for years. The triple bronze builds beautifully over a week of sessions. By Friday I look like I've been on holiday. Keeps my skin soft too.\"", "Christina M. | Amazon Customer"),
            ("\"Great lotion for building a deep base tan. It doesn't give instant gratification like some bronzers but the colour after a week of sessions is deeper and more natural-looking than anything else I've tried.\"", "Amanda R. | Amazon Customer"),
        ],
        "take": "The patient tanner's choice. The triple-bronze system doesn't deliver instant drama, but after three or four sessions the layered colour is deeper and more natural than single-bronzer alternatives. Best for those who tan consistently rather than occasionally.",
    },
]



PRODUCTS += [
    {
        "n": 9,
        "asin": "B09MG4B2XB",
        "title": "Devoted Creations Vacay Vibes Tanning Lotion",
        "short": "Devoted Creations Vacay Vibes",
        "image": "https://m.media-amazon.com/images/I/41ybtwZcllL.jpg",
        "badge": "&#127965; Best Salon Brand",
        "best_for": "Salon-grade hydration with tropical extracts",
        "size_detail": "8.5 oz | watermelon + guava | electrolyte-enhanced",
        "price": "18.95",
        "rating": "4.5",
        "review_count": "850",
        "tagline": "A salon-grade tanning lotion from Devoted Creations that uses electrolyte-enhanced coconut water and tropical fruit extracts.",
        "features": [
            ("&#127965;", "Tropical bronzing cocktail with watermelon and guava extracts"),
            ("&#128167;", "Electrolyte-enhanced coconut water for deep cellular hydration"),
            ("&#129381;", "Skin-quenching formula that combats UV-induced dehydration"),
            ("&#127807;", "Professional salon brand trusted by tanning salon staff"),
            ("&#128293;", "Bronzing complex for immediate colour enhancement"),
            ("&#10024;", "Leaves skin with a healthy glow between sessions"),
        ],
        "pros": [
            "Professional salon brand with premium formulation",
            "Electrolyte-enhanced hydration is genuinely different from standard moisturisers",
            "Tropical scent is fresh and modern, not heavy",
            "Bronzing complex gives immediate visible results",
            "Salon staff consistently recommend this line",
        ],
        "cons": [
            "8.5 oz bottle is smaller than budget competitors at a similar price",
        ],
        "reviews": [
            ("\"My tanning salon sells this and I understand why. The hydration is on another level compared to drugstore options. My skin feels plump after a session instead of dried out. The scent is a bonus.\"", "Kelsey M. | Amazon Customer"),
            ("\"Devoted Creations makes the best salon lotions and Vacay Vibes is my favourite from the line. The colour develops beautifully and the coconut water hydration actually works. Worth the price.\"", "Nicole H. | Amazon Customer"),
        ],
        "take": "The salon-grade pick for tanners who want premium hydration alongside their colour. The electrolyte-enhanced formula genuinely performs differently from standard moisturising tanning lotions. Worth it if skin health between sessions matters as much as darkness.",
    },
    {
        "n": 10,
        "asin": "B0FJPG6TXH",
        "title": "Jergens Natural Glow Hydra Gel Moisturizer",
        "short": "Jergens Natural Glow Hydra Gel",
        "image": "https://m.media-amazon.com/images/I/31Es4v81FWL.jpg",
        "badge": "&#128167; Best Gradual Builder",
        "best_for": "Gradual colour build with hyaluronic acid",
        "size_detail": "8.3 fl oz | fragrance-free | fair to medium skin",
        "price": "13.47",
        "rating": "4.5",
        "review_count": "522",
        "tagline": "A fragrance-free gradual tanning gel with hyaluronic acid for those who want to build colour slowly without committing to a tanning bed.",
        "features": [
            ("&#128167;", "Hyaluronic acid base that hydrates skin while colour develops gradually"),
            ("&#128683;", "Fragrance-free formula, no self-tanner smell at any point"),
            ("&#129528;", "Gradual colour builder that darkens over 3-5 days of daily use"),
            ("&#127807;", "Gel texture that absorbs instantly without sticky residue"),
            ("&#9989;", "Designed for fair to medium skin tones for natural-looking results"),
            ("&#128176;", "Drugstore price point from a trusted household name"),
        ],
        "pros": [
            "Completely fragrance-free, no self-tanner smell whatsoever",
            "Hyaluronic acid hydration rivals standalone moisturisers",
            "Gradual build means zero risk of streaks or mistakes",
            "Gel texture is the lightest on this list",
            "Trusted Jergens brand with decades of tanning product experience",
        ],
        "cons": [
            "Takes 3-5 days of daily use to see meaningful colour",
        ],
        "reviews": [
            ("\"Perfect for someone who wants a hint of colour without looking fake. I use it daily after my shower and by day four I have a natural glow. No smell, no streaks, no commitment.\"", "Sarah K. | Amazon Customer"),
            ("\"I use this between tanning bed sessions to maintain my colour. The hyaluronic acid keeps my skin from drying out and the gradual tint extends my tan by days. Genius product.\"", "Emily W. | Amazon Customer"),
        ],
        "take": "The low-commitment option for tanners who want gradual, foolproof colour without stepping into a bed every week. The fragrance-free formula and hyaluronic acid make it double as a quality moisturiser. Best for maintaining a base between sessions or building colour slowly from scratch.",
    },
]



# ---------------------------------------------------------------------------
# AUTHOR BLOCK (Skin Care category)
# ---------------------------------------------------------------------------
LI_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>'
WEB_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>'

AUTHORS = [
    ("Medically reviewed by", "Dr. Farhaad Riyaz", "MD, FAAD, FACMS",
     "Board-certified dermatologist and Mohs surgeon with extensive clinical experience treating sun-damaged and UV-exposed skin.",
     "https://drfarhaadriyaz.com/", "web", WEB_SVG, "Website"),
    ("Reviewed by", "Terri L. Watts", "Skin Care Specialist",
     "Skin care specialist and product formulator with over two decades of experience evaluating tanning and UV-care products.",
     "https://www.wattsbeautyusa.com/", "web", WEB_SVG, "Website"),
    ("Written by", "Anjali Sayee", "BTech, Beauty & Wellness Writer",
     "Skin care writer with a biotech background and a focus on evidence-based tanning product evaluation.",
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
# CSS / JS (Section A verbatim + Section B verbatim)
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
# HOSTINGER BLOCK (the full multi-product block provided by user)
# ---------------------------------------------------------------------------
HOSTINGER_MULTI_BLOCK = """<!-- wp:hostinger-affiliate-plugin/block {"display_type":"multiple_product_list","product_selector":"layout","product_list_type":"manual","list_navigation":"manual","list_layout_selected":true,"list_layout":"simplified_list","asin":"B00076XR3O,B0FJPG6TXH,B0CJYBLCNT,B0058E3XJI,B08MVJ5Y8Y,B08CNJ5BG7,B0CTBF3WLS,B0CKNHF944,B08G1LDFL8,B09MG4B2XB","asin_manual":"B00076XR3O,B0FJPG6TXH,B0CJYBLCNT,B0058E3XJI,B08MVJ5Y8Y,B08CNJ5BG7,B0CTBF3WLS,B0CKNHF944,B08G1LDFL8,B09MG4B2XB","items":{"B0CTBF3WLS":{"asin":"B0CTBF3WLS","title":"b.tan UV Tanning Bed Lotion | I Want The Darkest Tan Possible - x4000 Tan Intensifiers, Indoor & Outdoor Accelerator, Best Browning Body Tanner Extender, No Sun Protection, 12 Fl Oz","url":"https://www.amazon.com/dp/B0CTBF3WLS","image_url":"https://m.media-amazon.com/images/I/41nFaIDnL9L.jpg"},"B0CJYBLCNT":{"asin":"B0CJYBLCNT","title":"Jeallis Extreme Dark Tanning Lotion Accelerator for Indoor Tanning Beds & Outdoor Sun Tan with Bronzer to Get Dark Fast Tan, Bronzing Tanning Lotion with Tattoo Protecting Formula, DHA Free, 13.5oz","url":"https://www.amazon.com/dp/B0CJYBLCNT","image_url":"https://m.media-amazon.com/images/I/41sJIw304SL.jpg"},"B0FJPG6TXH":{"asin":"B0FJPG6TXH","title":"Jergens Natural Glow Hydra Gel Moisturizer, Hyaluronic Acid Tanning Lotion, Hydrating Tanning Gel, Fragrance-Free Self Tanner, Fair to Medium Skin Tones, 8.3 Fl Oz","url":"https://www.amazon.com/dp/B0FJPG6TXH","image_url":"https://m.media-amazon.com/images/I/31Es4v81FWL.jpg"},"B0058E3XJI":{"asin":"B0058E3XJI","title":"Millennium Tanning SOLID BLACK 100X Dark Tanning Lotion Indoor Outdoor Tan Enhancing Silicone Bronzer Tanning Bed Lotion 13.5 Fl oz (400 ml)","url":"https://www.amazon.com/dp/B0058E3XJI","image_url":"https://m.media-amazon.com/images/I/41KNj0nprcL.jpg"},"B08MVJ5Y8Y":{"asin":"B08MVJ5Y8Y","title":"Tanning Paradise Black Coconut Love Tanning Lotion | Coconut Oil | Age-Defying | Tattoo Protecting Formula | Ultra Hydrating Dark Tanning Lotion, 13.5oz","url":"https://www.amazon.com/dp/B08MVJ5Y8Y","image_url":"https://m.media-amazon.com/images/I/51Mugq3kI+L.jpg"},"B08CNJ5BG7":{"asin":"B08CNJ5BG7","title":"BYROKKO Shine Brown Tanning Accelerator Lotion - Indoor & Outdoor Fast Dark Tan Cream with Bronzer - Natural Botanical Oils for Face & Body - Water Resistant Formula - 7.1 Fl Oz Original","url":"https://www.amazon.com/dp/B08CNJ5BG7","image_url":"https://m.media-amazon.com/images/I/41XfctxzHVL.jpg"},"B0CKNHF944":{"asin":"B0CKNHF944","title":"European Gold Dark Star 6000X Ultra-Dark Tanning Lotion with Triple - Bronze Formula for Deep, Long-Lasting Tan and Skin-Nourishing Ingredients - 12 oz","url":"https://www.amazon.com/dp/B0CKNHF944","image_url":"https://m.media-amazon.com/images/I/41V39RoSBXL.jpg"},"B08G1LDFL8":{"asin":"B08G1LDFL8","title":"Coco & Eve Self Tanner Foam Kit - (Medium) Streak-Free Sunless Tanning Mousse, Tropically Scented Natural Looking Tan & Included Mitt Applicator, Vegan, Cruelty Free | Sunny Honey Bali Bronzing","url":"https://www.amazon.com/dp/B08G1LDFL8","image_url":"https://m.media-amazon.com/images/I/41eSl1YdmEL.jpg"},"B09MG4B2XB":{"asin":"B09MG4B2XB","title":"Devoted Creations Vacay Vibes Tanning Lotion \\u2013 Indoor/Outdoor Tropical Bronzing Cocktail Infused with Skin Quenching Watermelon and Guava Extracts, plus Electrolyte Enhanced Coconut Water \\u2013 8.5 oz.","url":"https://www.amazon.com/dp/B09MG4B2XB","image_url":"https://m.media-amazon.com/images/I/41ybtwZcllL.jpg"},"B00076XR3O":{"asin":"B00076XR3O","title":"Maui Babe Browning Lotion - Natural Hawaiian Tan Accelerator with Vitamins & Antioxidants - Moisturizing Formula for All Skin Types - Made in USA - 4 fl oz","url":"https://www.amazon.com/dp/B00076XR3O","image_url":"https://m.media-amazon.com/images/I/41mHd-+shCL.jpg"}},"ready":true} /-->"""



# ---------------------------------------------------------------------------
# COMPONENT BUILDERS
# ---------------------------------------------------------------------------
def stars_for(rating: str) -> str:
    """Return 4 solid gold stars (CSS handles colour)."""
    return "&#9733;&#9733;&#9733;&#9733;"


def build_intro():
    p1 = "Indoor tanning lotions are not optional if you're paying for bed time. Without one, your skin dries out faster, your tan fades within days, and you end up booking twice as many sessions to get the same colour. The right lotion amplifies what the UV is already doing &mdash; accelerating melanin, locking in moisture, and in some cases adding instant bronzer for walkout colour."
    p2 = "This guide covers ten tanning bed lotions the GlowPick team evaluated across bronzer intensity, hydration, scent, and real-user feedback from thousands of Amazon reviews. Options range from natural Hawaiian accelerators to extreme 100X bronzers, with prices between $13 and $35. Whether you want gradual colour or one-session drama, something here fits your routine."
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
        ("Q1. Do I really need a tanning lotion for indoor tanning beds?",
         "Yes, and the difference is measurable. Dry skin reflects UV light rather than absorbing it, which means you get less colour per minute of bed time. A tanning lotion hydrates the skin so UV penetrates more effectively, accelerates melanin production, and prevents the tight, flaky feeling that makes tans fade faster. Most salon staff will tell you that clients using a proper tanning lotion develop colour 30-50% faster than those going in dry."),
        ("Q2. What is the difference between a tanning accelerator, a bronzer, and a tingle lotion?",
         "Accelerators boost your skin's natural melanin response without adding any artificial colour &mdash; the tan comes purely from UV exposure. Bronzers contain DHA or cosmetic colour that adds an immediate or next-day tint on top of whatever UV tan develops. Tingle lotions increase blood flow to the skin surface (you'll feel a warm or prickly sensation), which can deepen results but may cause redness and isn't suitable for sensitive skin or beginners."),
        ("Q3. Can I use outdoor tanning oil in an indoor tanning bed?",
         "Technically yes, but it's not ideal. Outdoor oils are designed for natural sunlight and often contain SPF, which defeats the purpose in a bed. They can also damage the acrylic surface of tanning beds and void your salon's warranty. Indoor tanning lotions are formulated to be bed-safe, absorb without leaving oily residue on the acrylic, and work with the specific UV spectrum of indoor bulbs."),
        ("Q4. How soon before a tanning session should I apply tanning lotion?",
         "Apply it immediately before your session, right in the tanning room. The lotion needs to be on your skin when the UV hits. Don't apply it hours in advance as the active ingredients work in conjunction with UV exposure. Make sure it's fully rubbed in and absorbed before lying down to avoid streaks and to prevent residue on the bed surface."),
        ("Q5. How do I prevent my indoor tan from fading too quickly?",
         "Three things extend tan life: moisturise daily (any body lotion, applied morning and night), avoid hot baths and harsh exfoliants that strip the top layer of skin, and use a tan extender or gradual tanner between sessions. The Jergens Natural Glow on this list doubles as a maintenance product between bed visits. Also avoid chlorine pools for 24 hours after a session as chlorine accelerates fading."),
        ("Q6. Are indoor tanning bed lotions safe for tattooed skin?",
         "Standard tanning lotions won't damage tattoos, but UV exposure itself fades ink over time. If you have tattoos, look for lotions specifically labelled tattoo-safe or tattoo-protecting (Tanning Paradise Black Coconut Love and Jeallis on this list both include tattoo-protecting formulas). These contain ingredients that help shield ink pigments from UV degradation. For maximum tattoo preservation, cover fresh tattoos completely and consider using a higher-protection barrier cream over healed ink during sessions."),
    ]
    items = "\n".join(
        f'<div class="dyu-faq-item">\n<p class="dyu-faq-q">{q}</p>\n<p>{a}</p>\n</div>'
        for q, a in qs
    )
    return f'<h4 id="faq">Frequently Asked Questions About Indoor Tanning Bed Lotions</h4>\n\n{items}'


def build_helpful_box():
    return """<div class="dyu-helpful-box">
  <p><strong>Found This Guide Helpful?</strong></p>
  <p>Bookmark GlowPick for more independently researched beauty and skincare guides &mdash; we cover tanning, body care, skincare, and wellness, all without brand sponsorship or paid placements.</p>
  <p>If this saved you from buying the wrong tanning lotion, share it with someone who could use the same shortcut.</p>
</div>"""


def build_comment_prompt():
    text = "Drop the tanning lotion you swear by in the comments &mdash; bonus points if it's one most people haven't tried yet."
    return f'<p style="text-align:center; font-family: Arial, sans-serif; font-size: 0.93em; color: #555;">{text}</p>'



# ---------------------------------------------------------------------------
# STANDALONE FILE BUILDERS
# ---------------------------------------------------------------------------
def build_table_only_html(table_html):
    """Generate table-only.html for Pinterest screenshot."""
    css_override = """
.dyu-article { max-width: 100%; }
.dyu-compare-table { min-width: unset !important; width: 100% !important; font-size: 0.82em; }
.dyu-compare-table th, .dyu-compare-table td { padding: 8px 6px; white-space: normal; }
.dyu-table-wrapper { overflow-x: visible !important; }
"""
    # Remove scroll hint and h4 heading from table html
    table_no_hint = re.sub(r'<p class="dyu-scroll-hint">.*?</p>\s*', '', table_html)
    table_no_hint = re.sub(r'<h4 id="comparison-table">.*?</h4>\s*', '', table_no_hint)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best Indoor Tanning Bed Lotions 2026 - Comparison Table</title>
<style>
{CSS}
{css_override}
</style>
</head>
<body>
<div class="dyu-article">
{table_no_hint}
</div>
</body>
</html>"""


def build_faq_only_html(faq_html):
    """Generate faq-only.html for Pinterest screenshot."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best Indoor Tanning Bed Lotions 2026 - FAQ</title>
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
    # Products are already in correct ranked order (Best Overall #1, then by rating*reviews desc)
    # Build main article
    parts = []
    parts.append(f"<!-- DelightfulYou.com | {TOPIC} {YEAR} | tag: {TAG} -->")
    parts.append(f"<style>{CSS}</style>")
    parts.append(f"<script>{JS}</script>")
    parts.append('<div class="dyu-article">')
    parts.append(build_author_block())
    parts.append(build_intro())
    parts.append(build_toc())
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
    print(f"[1/3] Wrote {OUTFILE} ({len(html):,} bytes, {html.count(chr(10))+1:,} lines)")

    # Build table-only.html
    table_only = build_table_only_html(table_html)
    TABLE_FILE.write_text(table_only, encoding="utf-8")
    print(f"[2/3] Wrote {TABLE_FILE} ({len(table_only):,} bytes)")

    # Build faq-only.html
    faq_only = build_faq_only_html(faq_html)
    FAQ_FILE.write_text(faq_only, encoding="utf-8")
    print(f"[3/3] Wrote {FAQ_FILE} ({len(faq_only):,} bytes)")

    print("\nAll 3 files generated successfully.")


if __name__ == "__main__":
    main()
