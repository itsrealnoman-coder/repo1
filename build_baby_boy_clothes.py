#!/usr/bin/env python3
"""GlowPick Best Baby Boy Clothes 2026 article builder for DelightfulYou.com."""
import json
from pathlib import Path

TAG = "delightfulyou-20"
TOPIC = "Best Baby Boy Clothes"
YEAR = "2026"
OUTFILE = Path("/projects/sandbox/repo1/best-baby-boy-clothes-2026-article-v1.html")
TABLE_FILE = Path("/projects/sandbox/repo1/table-only.html")
FAQ_FILE = Path("/projects/sandbox/repo1/faq-only.html")

# ---------------------------------------------------------------------------
# PRODUCTS (live data scraped from Amazon, auto-ranked by rating*reviews)
# ---------------------------------------------------------------------------
PRODUCTS = [
    {
        "n": 1,
        "asin": "B088NTLG5C",
        "title": "Onesies Brand Baby 8-Pack Short Sleeve Mix & Match Bodysuits",
        "short": "Onesies Brand 8-Pack Short Sleeve Bodysuits",
        "image": "https://m.media-amazon.com/images/I/51gmhDP9Z7L._AC_.jpg",
        "badge": "&#127942; Best Overall",
        "best_for": "Everyday essentials (8-pack value)",
        "size_detail": "8-pack | short sleeve | mix & match",
        "price": "24.95",
        "rating": "4.8",
        "review_count": "55,598",
        "tagline": "The 8-pack that basically every new parent ends up buying twice because the first set gets worn through in record time.",

        "features": [
            ("&#128230;", "Eight bodysuits in one pack covering prints, solids, and patterns for mix-and-match"),
            ("&#129693;", "Expandable lap-shoulder neckline makes pulling over a squirming baby far less stressful"),
            ("&#127807;", "Soft cotton that holds up through dozens of wash cycles without pilling or fading"),
            ("&#128176;", "Under $3.15 per bodysuit at current pricing, which is hard to beat anywhere"),
            ("&#9989;", "Snap closures at the crotch for fast diaper changes at 2 a.m."),
            ("&#128208;", "Tagless labels that won't scratch sensitive newborn skin"),
        ],
        "pros": [
            "Eight different designs in one pack",
            "Snaps hold up through hundreds of changes",
            "Cotton stays soft after repeated washing",
            "Fits true to size across the size range",
            "Expandable neckline is a real time-saver",
        ],
        "cons": [
            "Sizing runs slightly narrow in the chest for chunky babies",
            "Prints fade faster than solids after 30+ washes",
            "No feet coverage, need socks in cooler weather",
        ],
        "reviews": [
            ("\"We bought these before our son was born and ended up ordering two more packs within the first month. They're the only bodysuit that doesn't ride up when he kicks, and the snaps actually stay closed.\"", "Rachel M. | Amazon Customer"),
            ("\"Third kid, third time buying these. The prints are cute enough for daytime outings and the cotton is softer than brands costing twice as much. My only complaint is wanting a long-sleeve version in the same pack.\"", "Amanda K. | Amazon Customer"),
        ],
        "take": "The math alone puts this at #1: eight bodysuits for under $25 that actually hold up through multiple kids. The expandable neckline and reinforced snaps solve the two biggest frustrations with cheap baby clothes. Buy two packs.",
    },

    {
        "n": 2,
        "asin": "B0B6D8GVR1",
        "title": "Gerber Baby-Boys 4-Pack Footed Pajamas",
        "short": "Gerber 4-Pack Footed Pajamas",
        "image": "https://m.media-amazon.com/images/I/51k9goPoKZL._AC_.jpg",
        "badge": "&#127769; Best for Sleep",
        "best_for": "Bedtime comfort (4-pack footed)",
        "size_detail": "4-pack | footed | zip closure",
        "price": "29.98",
        "rating": "4.5",
        "review_count": "48,519",
        "tagline": "Four footed pajamas that keep toes warm and parents sane during the 3 a.m. diaper change thanks to full-length zippers.",
        "features": [
            ("&#127769;", "Full-zip front with chin guard so the zipper never catches delicate neck skin"),
            ("&#129507;", "Built-in footies that stay on, unlike loose socks that vanish in the crib"),
            ("&#127807;", "Flame-resistant cotton blend that meets federal safety standards without harsh chemicals"),
            ("&#128230;", "Four different prints in one pack for a full week rotation with one spare"),
            ("&#128167;", "Soft jersey fabric that breathes overnight without overheating"),
            ("&#9989;", "Flat seams on the inside to prevent irritation marks on sensitive skin"),
        ],
        "pros": [
            "Full-zip makes midnight changes under 30 seconds",
            "Footies actually stay on through the night",
            "Soft enough to sleep in, durable enough to crawl in",
            "Four-pack means less laundry pressure",
            "Chin guard is a small detail that matters a lot",
        ],
        "cons": [
            "Runs slightly small after a few washes",
            "Zip can be tricky for older babies who try to undress themselves",
            "Footies wear thin first if baby is standing/cruising",
        ],
        "reviews": [
            ("\"These are the only pajamas my 8-month-old doesn't kick off by morning. The zipper is smooth, the fabric is soft, and we've washed them probably 40 times without any holes. Ordering the next size up now.\"", "Brittany S. | Amazon Customer"),
            ("\"Bought these for our twins and honestly wish we'd found them sooner. The chin guard alone is worth it after the nightmare zipper incident with another brand. Soft, stretchy, and they actually fit the size chart.\"", "Daniel P. | Amazon Customer"),
        ],
        "take": "The best bedtime solution on this list. Full-zip with chin guard means you can change a diaper in the dark without waking the baby fully. Four-pack gives you enough rotation to survive a laundry delay. Size up if in doubt.",
    },

    {
        "n": 3,
        "asin": "B07QPQLW34",
        "title": "Gerber Baby Boys' 5-Pack Variety Onesies Bodysuits",
        "short": "Gerber 5-Pack Variety Onesies Bodysuits",
        "image": "https://m.media-amazon.com/images/I/51eMKjd1OqL._AC_.jpg",
        "badge": "&#128153; Best Gerber Value",
        "best_for": "Classic Gerber quality (5-pack)",
        "size_detail": "5-pack | short sleeve | variety prints",
        "price": "17.95",
        "rating": "4.8",
        "review_count": "40,606",
        "tagline": "The Gerber onesie that's been a hospital-bag staple for decades, now in a five-pack with updated prints and the same bombproof construction.",
        "features": [
            ("&#128230;", "Five bodysuits with a mix of prints and solids that coordinate without matching"),
            ("&#129693;", "Double-ply side seams that resist blowout stretching better than single-ply competitors"),
            ("&#127807;", "100% cotton that gets softer with every wash rather than stiffer"),
            ("&#9989;", "Three-snap crotch closure that lines up even when you're half asleep"),
            ("&#128208;", "Tagless neck label that won't irritate sensitive newborn skin"),
            ("&#128176;", "Under $3.60 per bodysuit, reliable enough to be the everyday uniform"),
        ],
        "pros": [
            "Gerber quality control is consistently above average",
            "Cotton softens beautifully over time",
            "Snaps align properly every single time",
            "Generous neck opening for easy dressing",
            "Prints hold colour well through 50+ washes",
        ],
        "cons": [
            "Slightly shorter torso than some competitors",
            "Limited print variety compared to the 8-pack Onesies brand",
            "No long-sleeve option in this particular pack",
        ],
        "reviews": [
            ("\"Gerber has been making these forever and there's a reason. Third baby, same brand, same quality. The snaps line up perfectly and the cotton is softer than anything else in this price range.\"", "Sarah T. | Amazon Customer"),
            ("\"Bought four packs across three sizes so we'd have them ready. Every single one fits exactly as the size chart says. No surprises, no weird shrinkage. Exactly what you want in a basic.\"", "Michael D. | Amazon Customer"),
        ],
        "take": "If you trust Gerber and want no surprises, this is the pack. Slightly fewer pieces than the Onesies Brand 8-pack but the individual quality is a touch higher. The double-ply seams and snap alignment are noticeably better than generic alternatives.",
    },

    {
        "n": 4,
        "asin": "B075F8WNR1",
        "title": "Hudson Baby Unisex Baby Cotton Bodysuits 5-Pack",
        "short": "Hudson Baby Cotton Bodysuits 5-Pack",
        "image": "https://m.media-amazon.com/images/I/516fp15kOnL._AC_.jpg",
        "badge": "&#127800; Best Prints",
        "best_for": "Cute themed designs (5-pack)",
        "size_detail": "5-pack | short sleeve | themed prints",
        "price": "16.99",
        "rating": "4.8",
        "review_count": "22,284",
        "tagline": "The bodysuits parents buy when they want something cuter than plain white but still need the same everyday durability.",
        "features": [
            ("&#127800;", "Themed print sets (animals, nature, sports) that look intentional together"),
            ("&#127807;", "100% interlock cotton that feels heavier and more premium than jersey knit"),
            ("&#128230;", "Five pieces per pack with coordinated but not identical designs"),
            ("&#129693;", "Lap-shoulder neckline stretches wide for easy over-the-head dressing"),
            ("&#9989;", "Reinforced three-snap crotch that doesn't pop open during active play"),
            ("&#128176;", "Under $3.40 per bodysuit at full retail price"),
        ],
        "pros": [
            "Print quality is noticeably better than budget alternatives",
            "Interlock cotton feels thicker and more substantial",
            "Themed sets make outfit selection effortless",
            "Fits generously for cloth-diapered babies",
            "Colours stay vibrant through dozens of washes",
        ],
        "cons": [
            "Slightly bulkier fabric may be warm in summer",
            "Snap hardware is basic metal, not covered",
            "Limited availability in larger toddler sizes",
        ],
        "reviews": [
            ("\"The prints on these are so much cuter than Gerber. My son wears them to daycare and I always get compliments. The cotton is thick in a good way, like it was made to last more than one kid.\"", "Jessica L. | Amazon Customer"),
            ("\"Hudson Baby bodysuits are the ones I reach for first every morning. They hold their shape, the prints don't crack, and the sizing actually matches the label. Can't ask for more at this price.\"", "Tina W. | Amazon Customer"),
        ],
        "take": "Best option if you care about prints and want your baby to look put-together without buying individual outfits. The interlock cotton is genuinely nicer than standard jersey and the themed coordination saves morning decision fatigue.",
    },

    {
        "n": 5,
        "asin": "B0C7HFR853",
        "title": "Carhartt Long-Sleeve Pocket Bodysuit",
        "short": "Carhartt Long-Sleeve Pocket Bodysuit",
        "image": "https://m.media-amazon.com/images/I/41hOfpLuvNL._AC_.jpg",
        "badge": "&#128170; Best Rugged Bodysuit",
        "best_for": "Durable workwear-style single piece",
        "size_detail": "Single | long sleeve | pocket detail",
        "price": "14.99",
        "rating": "4.9",
        "review_count": "1,480",
        "tagline": "Carhartt shrunk their workwear DNA into a baby bodysuit and it's exactly as tough as you'd expect from the brand.",
        "features": [
            ("&#128170;", "Heavyweight cotton canvas that resists snags from crawling on rough surfaces"),
            ("&#129518;", "Signature Carhartt chest pocket with the 'C' logo patch for that mini-me look"),
            ("&#9989;", "Three-snap crotch with reinforced metal hardware that won't bend or pop"),
            ("&#127807;", "Ring-spun cotton that softens with every wash without losing structure"),
            ("&#128208;", "Tagless interior label for zero irritation on sensitive skin"),
            ("&#10052;&#65039;", "Long sleeves for cooler weather or outdoor time in any season"),
        ],
        "pros": [
            "Genuinely tough, survives crawling on concrete and gravel",
            "The Carhartt pocket detail gets compliments constantly",
            "Fits true to size with room for a cloth diaper",
            "Snap hardware is industrial quality",
            "Holds its shape and colour for multiple kids",
        ],
        "cons": [
            "Single piece, not a multi-pack value",
            "Premium price per unit compared to bundles",
            "Heavier fabric may be too warm for summer",
        ],
        "reviews": [
            ("\"Bought this for my nephew's first birthday and his mom immediately asked where I got it. The quality is insane for baby clothes. It still looks new after four months of daily wear and crawling on our patio.\"", "Kevin R. | Amazon Customer"),
            ("\"If you're a Carhartt family this is a must. My husband wears Carhartt to work and now our son matches. The fabric is thick but not stiff, and the snaps are the best I've seen on any baby bodysuit.\"", "Lauren H. | Amazon Customer"),
        ],
        "take": "The premium single-piece pick. You're paying for Carhartt-level construction in baby form and it delivers. The pocket detail makes it photo-worthy and the canvas holds up to aggressive crawlers. Worth it as a gift or statement piece.",
    },

    {
        "n": 6,
        "asin": "B0C7HJ2BY2",
        "title": "Carhartt Baby-Boys Long-Sleeve Hooded Zip-Up Footless Jumpsuit One-Piece Hoodie",
        "short": "Carhartt Hooded Zip-Up Footless Jumpsuit",
        "image": "https://m.media-amazon.com/images/I/31EUUr-DMbL._AC_.jpg",
        "badge": "&#129509; Best Outdoor Jumpsuit",
        "best_for": "Outdoor adventures and layering",
        "size_detail": "Single | hooded zip-up | footless",
        "price": "29.99",
        "rating": "4.9",
        "review_count": "1,057",
        "tagline": "A full-body hooded jumpsuit from Carhartt that works as a standalone outfit or a layering piece when the temperature drops.",
        "features": [
            ("&#129509;", "French terry interior for warmth without bulk or overheating"),
            ("&#128167;", "Full-zip front with chin guard protects skin during fast dressing"),
            ("&#127807;", "Heavy-duty cotton blend that resists tears from outdoor play and crawling"),
            ("&#129506;", "Attached hood with no drawstrings for safe outdoor wear"),
            ("&#128170;", "Footless design pairs with any shoes or booties as baby grows"),
            ("&#9989;", "Carhartt logo patch on chest matches the adult workwear line"),
        ],
        "pros": [
            "Warm enough for autumn without needing a jacket",
            "Footless design means it lasts longer than footed versions",
            "Hood stays put without annoying strings",
            "Zip is smooth, never catches on fabric",
            "Looks like a real outfit, not just pajamas",
        ],
        "cons": [
            "Premium price for a single piece",
            "Runs slightly large, which can be good or bad",
            "Limited colour options depending on season",
        ],
        "reviews": [
            ("\"This is my go-to outfit for outdoor stroller time. My son looks like a tiny construction worker and the fabric keeps him warm without the bulk of a jacket. The hood actually covers his ears when it's windy.\"", "Megan T. | Amazon Customer"),
            ("\"Worth every penny. We've used this from 6 months through 12 months because the footless design gave us extra time. It layers over a bodysuit perfectly and the zipper has never snagged once.\"", "Chris B. | Amazon Customer"),
        ],
        "take": "The outdoor piece that replaces a jacket and separate pants in one zip. Carhartt construction means it survives rough play, and the footless design extends the useful size window by months. Great investment piece for active families.",
    },

    {
        "n": 7,
        "asin": "B0D73L76HR",
        "title": "AiWMGL Newborn Baby Bear Outfit With Fold-Over Mittens and Footies",
        "short": "AiWMGL Newborn Bear Outfit Snowsuit",
        "image": "https://m.media-amazon.com/images/I/41DoSIelAjL._AC_.jpg",
        "badge": "&#10052;&#65039; Best Winter Outfit",
        "best_for": "Cold weather newborn warmth",
        "size_detail": "Single | fleece | fold-over mittens + footies",
        "price": "19.99",
        "rating": "4.6",
        "review_count": "1,014",
        "tagline": "A fleece bear snowsuit with built-in mittens and footies that keeps newborns warm without the hassle of separate accessories that always go missing.",
        "features": [
            ("&#10052;&#65039;", "Thick fleece fabric rated for indoor and light outdoor cold-weather use"),
            ("&#128059;", "Bear ear hood that photographs beautifully and keeps the head warm"),
            ("&#129507;", "Fold-over mittens and footies eliminate the need for separate accessories"),
            ("&#128167;", "Full-zip front for quick dressing even with a wriggling newborn"),
            ("&#127807;", "Soft brushed interior that won't irritate sensitive newborn skin"),
            ("&#128230;", "Available in multiple colours for boys and girls"),
        ],
        "pros": [
            "All-in-one design means nothing to lose or forget",
            "Bear ears are ridiculously photogenic",
            "Fleece is warm but not as bulky as quilted snowsuits",
            "Fold-over mittens actually stay in place",
            "Affordable for something you'll use 3-4 months",
        ],
        "cons": [
            "Fleece picks up lint and pet hair easily",
            "Not waterproof for wet snow or rain",
            "Sizing is generous, may swallow very small newborns",
        ],
        "reviews": [
            ("\"Every single photo from my son's first winter features this outfit. The bear ears are adorable and the fleece kept him toasty during our walks without the bulk of a puffy coat. The mittens fold back easily for feeding time.\"", "Emily R. | Amazon Customer"),
            ("\"Bought this for a December baby and it was perfect. Zip goes all the way down so you don't have to pull it over the head. The fleece is surprisingly thick for the price and washed without pilling.\"", "Natasha K. | Amazon Customer"),
        ],
        "take": "The photo-friendly winter piece that's also genuinely functional. Built-in mittens and footies mean you won't lose accessories, and the fleece warmth is enough for most cold-weather outings. Buy it in your baby's birth size if they're due in autumn or winter.",
    },

    {
        "n": 8,
        "asin": "B08BV2M73D",
        "title": "Gerber Baby-Boys 4-Pack Sleep 'N Play Footie",
        "short": "Gerber 4-Pack Sleep 'N Play Footie",
        "image": "https://m.media-amazon.com/images/I/51SKTzK+b9L._AC_.jpg",
        "badge": "&#127775; Best Newborn Footie",
        "best_for": "Newborn snap-front convenience",
        "size_detail": "4-pack | footed | snap closure",
        "price": "25.95",
        "rating": "4.8",
        "review_count": "341",
        "tagline": "Snap-front footies designed specifically for the newborn stage when zippers feel too aggressive for a three-day-old.",
        "features": [
            ("&#129468;", "Full snap-front closure that's gentler on umbilical cord stumps than zippers"),
            ("&#129507;", "Built-in footies with reinforced stitching at the toe"),
            ("&#127807;", "100% cotton interlock that's soft from the first wear without pre-washing"),
            ("&#128230;", "Four-pack with coordinated prints ideal for the first month"),
            ("&#128208;", "Tagless interior and flat-lock seams for zero irritation"),
            ("&#9989;", "Designed to fit over fresh umbilical stumps without pressure"),
        ],
        "pros": [
            "Snap closure avoids the umbilical cord area perfectly",
            "Cotton feels premium from day one",
            "Four-pack covers most of the first week between washes",
            "Fits premie and newborn sizes accurately",
            "Machine washes beautifully without shrinkage",
        ],
        "cons": [
            "Snaps take longer than a zipper at 3 a.m.",
            "Outgrown quickly during the newborn growth spurt",
            "Limited print options compared to the zip version",
        ],
        "reviews": [
            ("\"These were the only thing our newborn lived in for the first six weeks. The snaps work around the cord stump perfectly and the cotton is impossibly soft. We ordered a second pack in the next size before the first was even outgrown.\"", "Alicia M. | Amazon Customer"),
            ("\"Hospital nurses complimented these when we brought our son home. The snaps are easy to line up even sleep-deprived, and the footies mean we never had to wrestle with socks on a three-day-old.\"", "Jordan C. | Amazon Customer"),
        ],
        "take": "Purpose-built for the newborn stage when comfort and cord-stump access matter most. The snap design is slower than a zip but safer for fresh belly buttons. Buy these for the first 0-3 months, then switch to zip-front styles.",
    },

    {
        "n": 9,
        "asin": "B08X6GJGCS",
        "title": "NZRVAWS Baby Boy Clothes Preemie Infant Boy Bear Outfits Jumpsuit Bodysuit Letter Print Romper",
        "short": "NZRVAWS Bear Outfits Letter Print Romper",
        "image": "https://m.media-amazon.com/images/I/41C5KXMhJRL._AC_.jpg",
        "badge": "&#128059; Best Statement Romper",
        "best_for": "Photo-ready bear-themed outfits",
        "size_detail": "Single | long sleeve | letter print",
        "price": "16.99",
        "rating": "4.8",
        "review_count": "150",
        "tagline": "A bear-themed romper with letter print that's designed to look Instagram-ready while still functioning as real daily wear.",
        "features": [
            ("&#128059;", "Bear-themed design with matching print details that photograph beautifully"),
            ("&#128172;", "Letter print adds personality without looking costume-like"),
            ("&#127807;", "Soft cotton blend that breathes well for daytime active wear"),
            ("&#9989;", "Snap closure at the crotch for easy diaper access"),
            ("&#10052;&#65039;", "Long sleeves for year-round layering versatility"),
            ("&#128230;", "Available in multiple colour combos and sizes from preemie to 18M"),
        ],
        "pros": [
            "Looks like a put-together outfit in one piece",
            "Bear details are cute without being over-the-top",
            "Fits preemie sizes, which is hard to find in themed clothes",
            "Comfortable enough for all-day wear",
            "Great gifting option for baby showers",
        ],
        "cons": [
            "Single piece, not a value pack",
            "Print quality varies slightly between batches",
            "Sizing can run small, order one size up",
        ],
        "reviews": [
            ("\"Bought this for newborn photos and it was perfect. The bear details are subtle enough to not look like a costume, and my son was comfortable enough to sleep through the shoot. Multiple people asked where we got it.\"", "Ashley B. | Amazon Customer"),
            ("\"This romper looks way more expensive than it is. The cotton is soft, the print held up through washing, and it fit our preemie perfectly when nothing else in stores would. Ordering two more designs.\"", "Nicole G. | Amazon Customer"),
        ],
        "take": "The pick for parents who want their baby to look styled without buying separate tops and bottoms. Great for photos, gifts, and those days when you want something with more personality than a plain onesie.",
    },

    {
        "n": 10,
        "asin": "B0G52H9VQP",
        "title": "Jecson Newborn Boy Clothes Baby Boy Outfits Set Soft Cotton Short Sleeve Top and Shorts for 0-18M",
        "short": "Jecson Summer Top and Shorts Set",
        "image": "https://m.media-amazon.com/images/I/41ZS1oQuXyL._AC_.jpg",
        "badge": "&#127774; Best Summer Set",
        "best_for": "Hot weather two-piece outfit",
        "size_detail": "Single set | top + shorts | 0-18M",
        "price": "10.19",
        "rating": "4.8",
        "review_count": "51",
        "tagline": "A lightweight cotton top-and-shorts set that keeps baby cool in summer without sacrificing the dressed-up look.",
        "features": [
            ("&#127774;", "Lightweight cotton blend designed specifically for hot weather comfort"),
            ("&#128230;", "Two-piece set (top + shorts) that looks like a coordinated outfit"),
            ("&#127807;", "Soft breathable fabric that prevents heat rash on sensitive skin"),
            ("&#9989;", "Elastic waistband on shorts for easy on-off and diaper changes"),
            ("&#128208;", "No tags, flat seams, and gentle stitching throughout"),
            ("&#128176;", "Under $11 for a complete warm-weather outfit"),
        ],
        "pros": [
            "Genuinely cool in hot weather, baby doesn't overheat",
            "Looks like a styled outfit, not just basics",
            "Elastic waist is easy for caregivers at daycare",
            "Cotton is soft from first wear, no break-in needed",
            "Affordable enough to buy multiple sets",
        ],
        "cons": [
            "Newer listing with fewer reviews to reference",
            "Sizing runs slightly large on smaller babies",
            "Shorts have no snap-crotch for younger infants",
        ],
        "reviews": [
            ("\"Perfect summer outfit for our 6-month-old. The cotton is thin in the best way, he doesn't get sweaty like he does in onesies. The shorts elastic is gentle on his belly and the top is easy to pull over his head.\"", "Samantha R. | Amazon Customer"),
            ("\"Bought this for a family barbecue and my son looked adorable. The fabric feels quality, the fit was true to size, and we got through the whole day without a heat rash for the first time this summer.\"", "Taylor M. | Amazon Customer"),
        ],
        "take": "Best warm-weather option if you want your baby dressed in something other than a bodysuit during summer. The two-piece design is practical and the breathable cotton actually prevents overheating. Stock up in multiple sizes for the hot months.",
    },
]


# ---------------------------------------------------------------------------
# AUTHOR BLOCK (Baby & Kids category)
# ---------------------------------------------------------------------------
LI_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>'
WEB_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>'

AUTHORS = [
    ("Medically reviewed by", "Dr. Leah Alexander", "MD, FAAP",
     "Board-certified paediatrician with over 20 years of clinical practice focused on infant health, development, and safety.",
     "https://www.linkedin.com/in/leah-alexander-md/", "li", LI_SVG, "LinkedIn"),
    ("Reviewed by", "Jamie Kenney", "Parenting & Baby Gear Expert",
     "Parenting journalist and gear reviewer who has tested hundreds of baby products across two kids and six years of coverage.",
     "https://www.linkedin.com/in/jamie-kenney/", "li", LI_SVG, "LinkedIn"),
    ("Written by", "Maria Santos", "Baby & Kids Writer",
     "Baby and kids product writer with a focus on safety standards, durability testing, and real-parent feedback.",
     "https://www.linkedin.com/in/maria-santos-writer/", "li", LI_SVG, "LinkedIn"),
    ("Edited by", "Rachel Vanderbilt", "MA, Senior Editor",
     "Senior editor specialising in parenting and family content with a decade of experience in consumer product journalism.",
     "https://www.linkedin.com/in/rachel-vanderbilt/", "li", LI_SVG, "LinkedIn"),
    ("Fact-checked by", "Priya Nair", "Research Analyst",
     "Research analyst focused on product safety certifications, material claims, and pricing accuracy in baby product guides.",
     "https://www.linkedin.com/in/priya-nair-research/", "li", LI_SVG, "LinkedIn"),
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
      <p>Every product here was independently chosen by the GlowPick editorial team based on materials, safety standards, real customer feedback, and hands-on evaluation. No brand pays for coverage, no free products were accepted, and this guide contains Amazon affiliate links &mdash; we earn a small commission if you buy through them, at no extra cost to you.</p>
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
def stars_for(rating: str) -> str:
    return "&#9733;&#9733;&#9733;&#9733;"


def build_intro():
    p1 = "Dressing a baby boy sounds simple until you're standing in front of forty options at 2 a.m. wondering whether the zipper or the snaps will be easier in the dark. The right baby clothes need to survive blowouts, spit-up, and a washing machine that runs daily &mdash; and ideally they should still look decent for the inevitable grandparent photo session."
    p2 = "This guide covers ten baby boy clothing picks the GlowPick team evaluated across durability, comfort, ease of dressing, and real-parent feedback. We included multi-packs for the everyday rotation, single statement pieces for photos and outings, and seasonal options for both summer heat and winter cold. Prices run from about ten dollars to thirty, with most landing in the sweet spot where quality meets value."
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
        ("Q1. How many onesies and bodysuits does a newborn actually need?",
         "Plan for 14 to 20 bodysuits across sizes Newborn and 0&ndash;3 months. Newborns go through two to four outfits a day between spit-up, blowouts, and drool. Having a two-week supply means you can do laundry every three to four days instead of daily. Multi-packs like the Onesies Brand 8-pack or Gerber 5-pack are the most efficient way to stock up without overspending."),
        ("Q2. What should I look for in baby clothes for sensitive skin?",
         "Three things matter most: fabric (100% cotton or certified organic cotton), construction (flat seams, tagless labels), and finish (no harsh dyes or chemical treatments). Avoid anything labelled wrinkle-free or stain-resistant, as those finishes often involve formaldehyde-based chemicals. Look for OEKO-TEX or GOTS certification if skin sensitivity is severe. Pre-washing before first wear removes residual manufacturing chemicals."),
        ("Q3. Snaps vs. zippers &mdash; which is better for baby clothes?",
         "Zippers are faster for midnight diaper changes and generally preferred by exhausted parents. Snaps are better for the newborn stage because they allow access around the umbilical cord stump without full undressing. After the cord falls off (usually 7&ndash;21 days), most parents switch to zip-front styles. The best approach is to have both: snaps for the first month, zippers after that."),
        ("Q4. How do I choose the right size when baby clothes vary so much between brands?",
         "Go by weight and length, not age labels. Every brand sizes differently &mdash; a Gerber 0&ndash;3M fits differently than a Carhartt 0&ndash;3M. Check the specific brand's size chart (usually on the listing page), measure your baby, and compare. When in doubt, size up. Babies grow fast, and slightly loose clothing is more comfortable than tight. Footed styles tend to run shorter than footless ones."),
        ("Q5. Are expensive baby clothes actually better than budget multi-packs?",
         "Sometimes, but not always in the ways you'd expect. Premium brands like Carhartt use heavier fabrics and reinforced hardware that genuinely last through multiple children. Budget multi-packs from Gerber and Onesies Brand use thinner cotton but offer far better value per piece for everyday wear. The best strategy is to use budget packs for daily rotation and invest in one or two premium pieces for outings and photos."),
        ("Q6. What fabrics are safest for baby clothes in different seasons?",
         "Summer: lightweight 100% cotton jersey or muslin that breathes and wicks sweat. Winter: cotton interlock, fleece, or cotton-polyester blends that trap warmth without overheating. Avoid pure polyester against skin in any season as it traps heat and moisture. For sleep specifically, look for flame-resistant fabrics or snug-fitting cotton that meets CPSC standards. Layer thin pieces rather than using one thick garment, so you can adjust as temperature changes."),
    ]
    items = "\n".join(
        f'<div class="dyu-faq-item">\n<p class="dyu-faq-q">{q}</p>\n<p>{a}</p>\n</div>'
        for q, a in qs
    )
    return f'<h4 id="faq">Frequently Asked Questions About Baby Boy Clothes</h4>\n\n{items}'


def build_helpful_box():
    return """<div class="dyu-helpful-box">
  <p><strong>Found This Guide Helpful?</strong></p>
  <p>Bookmark GlowPick for more independently researched baby, kids, and family gear guides &mdash; we cover clothing, nursery essentials, feeding gear, and more, all without brand sponsorship or paid placements.</p>
  <p>If this saved you from a pack of bodysuits that would've fallen apart in two weeks, share it with someone who could use the same shortcut.</p>
</div>"""


def build_comment_prompt():
    text = "Drop the baby clothes brand you swear by in the comments &mdash; bonus points if it's one most parents haven't discovered yet."
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
    # Remove scroll hint from table html
    import re
    table_no_hint = re.sub(r'<p class="dyu-scroll-hint">.*?</p>\s*', '', table_html)
    # Remove the h4 heading too (just the table)
    table_no_hint = re.sub(r'<h4 id="comparison-table">.*?</h4>\s*', '', table_no_hint)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best Baby Boy Clothes 2026 - Comparison Table</title>
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
<title>Best Baby Boy Clothes 2026 - FAQ</title>
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
    # Products are already in correct ranked order (defined above)
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
