"""Zero Regret Buys -- content data (v2, from-scratch rebuild).

This file holds ONLY content: the 30 products, their Amazon links, photos,
and the short copy. Nothing about layout lives here. The design (templates
and CSS) lives in build.py and styles.css. The data is reused untouched from
the v1 build so every affiliate link, ASIN and photo stays identical.
"""



TAG = "zeroregretb04-20"


BASE = "https://zero-regret-buys-kirpal-singh.vercel.app"


DISCLOSURE = "As an Amazon Associate I earn from qualifying purchases."


PRODUCTS = [
    {
        "slug": "magnesium-glycinate", "num": 1, "title": "Magnesium Bisglycinate",
        "tile": "Mg", "keyword": "SLEEP", "asin": "B08WVD2YDB",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Minerals", "sub_slug": "minerals",
        "pitch": "A source of magnesium \u2014 a mineral that helps maintain proper muscle function and plays a role in tissue formation.",
        "rule": "\u201cglycinate\u201d on the label, not \u201coxide\u201d \u2014 and a third-party testing seal. If the cheaper bottle checks both boxes, buy the cheaper bottle.",
        "skip": "your diet already covers it, or you take medication that interacts with magnesium \u2014 ask your pharmacist first. This isn\u2019t a sleep aid.",
    },
    {
        "slug": "creatine-monohydrate", "num": 2, "title": "Creatine Monohydrate",
        "tile": "Cr", "keyword": "GAINS", "asin": "B0043YLNSC",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Performance", "sub_slug": "performance",
        "pitch": "Supports lean mass and strength gains when combined with resistance training. One of the most studied sports supplements out there.",
        "rule": "plain creatine monohydrate. No blends, no \u201cmatrix\u201d, no fairy dust \u2014 the single ingredient is the whole point.",
        "skip": "you won\u2019t take it daily \u2014 it only works with consistency. No resistance training, no reason to buy it.",
    },
    {
        "slug": "omega-3-fish-oil", "num": 3, "title": "Omega-3 Fish Oil",
        "tile": "\u03a93", "keyword": "OMEGA", "asin": "B079NP724M",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Everyday Essentials", "sub_slug": "everyday-essentials",
        "pitch": "A source of EPA and DHA omega-3 fatty acids for the maintenance of good health. The unglamorous daily the wellness aisle wishes it could be.",
        "rule": "check EPA/DHA per serving on the facts panel \u2014 not just \u201c1000mg fish oil\u201d. Molecularly distilled is a plus.",
        "skip": "you eat fatty fish twice a week already. On blood-thinning medication? Talk to your pharmacist before adding it.",
    },
    {
        "slug": "zinc-citrate", "num": 4, "title": "Zinc Citrate",
        "tile": "Zn", "keyword": "SHIELD", "asin": "B009D9NIGW",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Minerals", "sub_slug": "minerals",
        "pitch": "A source of zinc \u2014 an essential mineral involved in tissue formation and everyday cellular housekeeping.",
        "rule": "citrate or picolinate over oxide for absorption. Keep the dose sane \u2014 more is not more with zinc.",
        "skip": "your multivitamin already includes zinc \u2014 don\u2019t stack. Take with food if it bothers your stomach.",
    },
    {
        "slug": "vitamin-d3-k2", "num": 5, "title": "Vitamin D3 + K2",
        "tile": "D3", "keyword": "BONES", "asin": "B08WNTMWRV",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Everyday Essentials", "sub_slug": "everyday-essentials",
        "pitch": "Helps in the development and maintenance of bones and teeth, and helps the body absorb calcium. D3 with K2 \u2014 never solo.",
        "rule": "D3 <i>with</i> K2 (MK-7) in one capsule, dose per softgel clearly stated. D3 alone at a premium? Keep walking.",
        "skip": "you get real midday sun year-round (rare in Canada, October to March). On medication affected by vitamin K \u2014 ask your pharmacist.",
    },
    {
        "slug": "vichy-dercos", "num": 6, "title": "Vichy Dercos Anti-Dandruff Shampoo",
        "tile": "VD", "keyword": "SHINE", "asin": "B01BPHAD1W",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Hair & Scalp", "sub_slug": "hair-scalp",
        "pitch": "An anti-dandruff shampoo that visibly reduces flakes for a calmer-feeling scalp. Pharmacy-aisle serious, not salon-perfume serious.",
        "rule": "",
        "skip": "",
    },
    {
        "slug": "retinal-shot-booster", "num": 7, "title": "celimax Vita A Retinal Shot Tightening Booster",
        "tile": "RS", "keyword": "FIRM", "asin": "B0DK4Y2YP3",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "A 0.1% retinal booster with micro-fine A-Shot particles, made for the look of firmer skin and tighter-looking pores. Nighttime only \u2014 retinal and sunlight don\u2019t mix.",
        "rule": "retinal (not retinol) named on the ingredient list, with a clear nighttime-use plus sunscreen-the-next-day routine. If a booster can\u2019t name its vitamin A form, keep walking.",
        "skip": "you\u2019ve never used a vitamin A product \u2014 start every other night, or skip it. Irritation means less, not more. Nights only: sunscreen the morning after is non-negotiable.",
    },
    {
        "slug": "dr-althea-345", "num": 8, "title": "Dr. Althea 345 Relief Cream",
        "tile": "DA", "keyword": "GLASS", "asin": "B07PK2P2XB",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "A niacinamide cream built for the glass-skin look \u2014 calm, even-looking skin with a dewy finish. Fragrance-free and made for all skin types.",
        "rule": "niacinamide high on the ingredient list and no artificial fragrance. Glass skin is a finish, not a filter \u2014 the cream should calm first, glow second.",
        "skip": "you want actives that tingle \u2014 this is the calm one, not the strong one. If your skin hates niacinamide, this isn\u2019t your tube.",
    },
    {
        "slug": "axis-y-dark-spot", "num": 9, "title": "Axis-Y Dark Spot Correcting Glow Serum",
        "tile": "AY", "keyword": "CLEAR", "asin": "B091238V7N",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "A niacinamide serum aimed at the look of dark spots and post-blemish marks, for a more even-looking tone. The slow, steady brightening lane.",
        "rule": "niacinamide doing the brightening work, with sunscreen in the daytime routine \u2014 no serum outruns the sun on dark spots. Give it weeks of consistency before judging.",
        "skip": "you want overnight results \u2014 fading the look of marks takes weeks, and anyone promising days is selling something else. Active breakouts? Treat those first.",
    },
    {
        "slug": "arencia-rice-cleanser", "num": 10, "title": "Arencia Fresh Green Rice Mochi Cleanser",
        "tile": "Ar", "keyword": "BRIGHT", "asin": "B0C1BMWPR2",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "A rice-powder mochi cleanser for hydrating, deep cleansing with a brightening angle. The fun-textured first step that made the screenshots.",
        "rule": "rice powder doing the gentle exfoliation, and a hydrating (not squeaky) finish. If a cleanser leaves your face tight, it failed the only test that matters.",
        "skip": "you already have a cleanser you love \u2014 this is a swap, not a second cleanser. Over-exfoliated skin? Fix your barrier first.",
    },
    {
        "slug": "complex-15-cream", "num": 11, "title": "Complex 15 Daily Face Cream",
        "tile": "C15", "keyword": "DEW", "asin": "B00BPDF0YC",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "A propylene-glycol daily face cream \u2014 hypoallergenic, unscented, non-greasy, oil-free. The Canadian pharmacy answer to the viral cheap-cream slot.",
        "rule": "propylene glycol base, unscented, non-comedogenic. If the cheap cream has fragrance and shimmer, it\u2019s not the workhorse \u2014 keep walking.",
        "skip": "your skin runs oily \u2014 this is the dry-to-normal tube. Patch-test like everything else.",
    },
    {
        "slug": "azelaic-acid-10", "num": 12, "title": "The Ordinary Azelaic Acid Suspension 10%",
        "tile": "Az", "keyword": "EVEN", "asin": "B06WD5J8KY",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "A 10% azelaic acid suspension for the look of blemish-prone skin and a brighter, more even tone. The multitasker that doesn\u2019t brag.",
        "rule": "10% azelaic acid, clearly stated \u2014 and patience. It works on the look of tone and redness over weeks, not washes.",
        "skip": "you want a one-week miracle \u2014 this is a weeks-long one. Tingling at first is normal; burning is not.",
    },
    {
        "slug": "ashwagandha-ksm66", "num": 13, "title": "Webber Naturals Ashwagandha 7200mg (KSM-66)",
        "tile": "As", "keyword": "CALM", "asin": "B0B8PGT48W",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Adaptogens", "sub_slug": "adaptogens",
        "pitch": "A KSM-66 ashwagandha \u2014 the studied extract form \u2014 for stress and sleep. People say it calmed their stress and fixed their sleep.",
        "rule": "\u201cKSM-66\u201d on the label, not just \u201cashwagandha root powder\u201d \u2014 the extract is the whole point.",
        "skip": "you\u2019re pregnant, nursing, or on thyroid medication \u2014 talk to your doctor first. This isn\u2019t a sedative.",
    },
    {
        "slug": "organika-collagen", "num": 14, "title": "Organika Enhanced Collagen Powder",
        "tile": "Co", "keyword": "PLUMP", "asin": "B01MZ1FC46",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Beauty", "sub_slug": "beauty",
        "pitch": "A Canadian-made collagen powder \u2014 unflavoured, 500g \u2014 for hair, skin, and nails. People say their hair got thicker and nails stronger.",
        "rule": "unflavoured and Canadian-made with transparent sourcing. If it\u2019s a \u201cbeauty blend\u201d with fairy-dust doses, keep walking.",
        "skip": "you expect results in a week \u2014 collagen is a months-long game. Vegan? This is bovine-sourced.",
    },
    {
        "slug": "probiotic-30b", "num": 15, "title": "Webber Naturals Probiotic 30 Billion",
        "tile": "Pr", "keyword": "GUT", "asin": "B00L3WSHDG",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Gut Health", "sub_slug": "gut-health",
        "pitch": "A 30-billion CFU probiotic with 8 strains \u2014 one capsule daily. People say it sorted their bloating and gut issues.",
        "rule": "multi-strain (8 here) at a real CFU count \u2014 not a single strain at a sprinkle dose.",
        "skip": "you\u2019re immunocompromised \u2014 talk to your doctor first. Take consistently; sporadic use does little.",
    },
    {
        "slug": "truskin-vitamin-c", "num": 16, "title": "TruSkin Vitamin C Serum",
        "tile": "TC", "keyword": "GLOW", "asin": "B01M4MCUAF",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "A vitamin C serum for brighter-looking skin \u2014 106,000+ ratings. People say their skin looks brighter and spots are fading.",
        "rule": "vitamin C as a headline active with a real concentration \u2014 and sunscreen every morning, because C without SPF is half the job.",
        "skip": "your skin hates vitamin C (tingling that turns to burning) \u2014 patch-test first. Very sensitive? Start every other day.",
    },
    {
        "slug": "ordinary-hyaluronic", "num": 17, "title": "The Ordinary Hyaluronic Acid 2% + B5",
        "tile": "Hy", "keyword": "QUENCH", "asin": "B01MYEZPC8",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "The cult budget hydrator \u2014 2% hyaluronic acid with B5. A 73-year-old reviewer said it virtually erased her fine lines.",
        "rule": "apply to damp skin, seal with moisturizer \u2014 humectants need water to grab and a lid to keep it.",
        "skip": "you live somewhere bone-dry and won\u2019t seal it \u2014 HA without a moisturizer on top can backfire.",
    },
    {
        "slug": "ombrelle-spf60", "num": 18, "title": "Garnier Ombrelle Anti-Shine SPF 60",
        "tile": "SP", "keyword": "SHADE", "asin": "B081DNB1B2",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "Canada\u2019s daily sunscreen \u2014 SPF 60, lightweight, no white cast. The one reviewers actually wear every day.",
        "rule": "daily wear beats beach-day SPF \u2014 lightweight and no white cast is what gets it on your face every morning.",
        "skip": "you want a mineral-only formula \u2014 this is chemical. Reapply every 2 hours in real sun, like all sunscreen.",
    },
    {
        "slug": "myhalos-sleep-mask", "num": 19, "title": "MyHalos 3D Blackout Sleep Mask",
        "tile": "SM", "keyword": "DARK", "asin": "B09CZ68WV3",
        "cat": "Gadgets", "cat_slug": "gadgets",
        "sub": "Sleep", "sub_slug": "sleep",
        "pitch": "A 3D contoured blackout mask \u2014 100% darkness, zero eye pressure. Insomniacs call it a game-changer.",
        "rule": "3D contour (not flat) with an adjustable strap \u2014 if it presses your eyelids, it failed the only test.",
        "skip": "you sleep exclusively on your stomach with your face in the pillow \u2014 nothing survives that.",
    },
    {
        "slug": "schiara-posture", "num": 20, "title": "Schiara Posture Corrector",
        "tile": "Po", "keyword": "TALL", "asin": "B07VST9VYH",
        "cat": "Gadgets", "cat_slug": "gadgets",
        "sub": "Posture", "sub_slug": "posture",
        "pitch": "An adjustable posture corrector \u2014 30,000+ ratings. A chiropractor noticed the difference in weeks.",
        "rule": "adjustable and actually wearable \u2014 a corrector that doesn\u2019t fit doesn\u2019t get worn. Training, not dependence.",
        "skip": "you have a diagnosed spinal condition \u2014 see a professional first. This trains habits, it doesn\u2019t treat injuries.",
    },
    {
        "slug": "philips-wake-up", "num": 21, "title": "Philips SmartSleep Wake-Up Light",
        "tile": "WL", "keyword": "DAWN", "asin": "B0093162RM",
        "cat": "Gadgets", "cat_slug": "gadgets",
        "sub": "Sleep", "sub_slug": "sleep",
        "pitch": "A sunrise-simulating alarm \u2014 14,000+ ratings. Wake up to gradually brightening light, not a blaring alarm.",
        "rule": "gradual sunrise simulation with adjustable intensity \u2014 the light does the waking, sound is the backup.",
        "skip": "you need to be up at 4 AM for shift work and sleep through anything \u2014 keep a backup alarm.",
    },
    {
        "slug": "b12-2500", "num": 22, "title": "Nature's Bounty Vitamin B12 2500mcg",
        "tile": "B12", "keyword": "ENERGY", "asin": "B00BMEHEXE",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Energy", "sub_slug": "energy",
        "pitch": "A high-potency B12 for energy metabolism \u2014 cherry-flavoured fast-dissolve tablets. B12 helps prevent deficiency, and this is the easy daily.",
        "rule": "fast-dissolve at a real dose \u2014 if it\u2019s a tiny dose in a hard-pressed tablet, keep walking.",
        "skip": "you eat plenty of animal products and feel fine \u2014 B12 deficiency is the target here, not a buzz.",
    },
    {
        "slug": "turmeric-curcumin", "num": 23, "title": "Webber Naturals Turmeric Curcumin + Black Pepper",
        "tile": "Tu", "keyword": "JOINTS", "asin": "B09T8PKKRG",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Joints", "sub_slug": "joints",
        "pitch": "A turmeric curcumin with black pepper extract \u2014 the pepper boosts absorption. For joint comfort and everyday inflammation support.",
        "rule": "black pepper (piperine) on the label \u2014 curcumin without it barely absorbs. Standardized curcuminoids, not just turmeric powder.",
        "skip": "you\u2019re on blood thinners \u2014 talk to your doctor first. This is daily support, not a painkiller.",
    },
    {
        "slug": "melatonin-10mg", "num": 24, "title": "Jamieson Melatonin 10mg Dual-Action",
        "tile": "Me", "keyword": "REST", "asin": "B0797NJW1Q",
        "cat": "Supplements", "cat_slug": "supplements",
        "sub": "Sleep", "sub_slug": "sleep",
        "pitch": "A dual-action melatonin \u2014 helps you fall asleep faster and resets a scrambled sleep cycle. The training-wheels bottle for broken sleep.",
        "rule": "dual-action (fast + sustained release) \u2014 single-release wears off at 3 AM. Start low; more melatonin isn\u2019t better sleep.",
        "skip": "you need it every single night indefinitely \u2014 fix the habit, use the bottle as training wheels. Vivid dreams are a known side effect.",
    },
    {
        "slug": "cerave-cream", "num": 25, "title": "CeraVe Moisturizing Cream",
        "tile": "Ce", "keyword": "SOFT", "asin": "B083GGFTPW",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "The 24-hour moisturizer with three essential ceramides \u2014 dermatologist-developed, fragrance-free. The tub that dermatologists actually name.",
        "rule": "ceramides plus hyaluronic acid on the label \u2014 that combo is the whole formula. Fragrance-free matters for faces.",
        "skip": "your skin runs very oily \u2014 this is the rich cream; the lotion version is the lighter sibling.",
    },
    {
        "slug": "ordinary-niacinamide", "num": 26, "title": "The Ordinary Niacinamide 10% + Zinc 1%",
        "tile": "Ni", "keyword": "PORES", "asin": "B01MDTVZTZ",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "The cult pore-minimizer \u2014 10% niacinamide with 1% zinc, 51,000+ reviews. Regulates oil and refines the look of pores.",
        "rule": "10% niacinamide clearly stated \u2014 and sunscreen every morning, because no serum outruns the sun. Patch-test first.",
        "skip": "your skin hates niacinamide \u2014 you\u2019ll know fast. Very sensitive? Start every other day.",
    },
    {
        "slug": "hydro-boost-gel", "num": 27, "title": "Neutrogena Hydro Boost Gel Cream",
        "tile": "HB", "keyword": "BOOST", "asin": "B00YPBGIIS",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Skincare", "sub_slug": "skincare",
        "pitch": "A hyaluronic gel-cream for instant hydration \u2014 lightweight, never greasy. The drugstore hydrator that punches above its price.",
        "rule": "gel-cream texture with hyaluronic acid \u2014 if it pills under makeup or feels heavy, it failed the only test.",
        "skip": "you need heavy winter occlusion \u2014 this is the lightweight layer, not the final seal.",
    },
    {
        "slug": "acupressure-mat", "num": 28, "title": "ELEBOX Acupressure Mat + Pillow Set",
        "tile": "Am", "keyword": "RELIEF", "asin": "B07M9CGZNY",
        "cat": "Gadgets", "cat_slug": "gadgets",
        "sub": "Recovery", "sub_slug": "recovery",
        "pitch": "An acupressure mat and pillow set for back and neck relief \u2014 lie back, breathe, decompress. The 20-minute reset.",
        "rule": "a real spike count with the pillow included \u2014 the neck piece is half the value. Start with a shirt on.",
        "skip": "you have a skin condition or take blood thinners \u2014 check with a professional. Sharp at first is normal; painful is not.",
    },
    {
        "slug": "scalp-massager", "num": 29, "title": "Comfier Cordless Scalp Massager",
        "tile": "Sc", "keyword": "KNEAD", "asin": "B08KGD8JWK",
        "cat": "Gadgets", "cat_slug": "gadgets",
        "sub": "Recovery", "sub_slug": "recovery",
        "pitch": "A cordless scalp massager with deep-kneading nodes \u2014 waterproof, for stress relief and the best head massage you\u2019ve had at home.",
        "rule": "cordless and waterproof \u2014 if it needs a cord or fears the shower, it\u2019s the wrong one. Multiple speeds, not one.",
        "skip": "you have scalp wounds or a skin condition up there \u2014 let it heal first. Long hair? Detangle first.",
    },
    {
        "slug": "olaplex-no3", "num": 30, "title": "Olaplex No.3 Hair Perfector",
        "tile": "O3", "keyword": "REPAIR", "asin": "B08TWTQDCX",
        "cat": "Personal Care", "cat_slug": "personal-care",
        "sub": "Haircare", "sub_slug": "haircare",
        "latest": True,
        "pitch": "The at-home bond builder \u2014 22,000+ reviews. Repairs the look of damaged hair and reduces breakage. The salon step you do in your shower.",
        "rule": "No.3 specifically \u2014 the take-home treatment, not the shampoo. Damp hair before shampooing, 10+ minutes.",
        "skip": "you expect a conditioner \u2014 this is a pre-shampoo treatment. Very fine hair? Don\u2019t overdo the time.",
    },
]

for p in PRODUCTS:
    p["url"] = "https://www.amazon.ca/dp/%s?tag=%s" % (p["asin"], TAG)



BADGES = {
    "magnesium-glycinate": "Sleep",
    "creatine-monohydrate": "Gym Days",
    "omega-3-fish-oil": "Daily Omegas",
    "zinc-citrate": "Immunity",
    "vitamin-d3-k2": "Bones",
    "vichy-dercos": "Scalp",
    "retinal-shot-booster": "Firmness",
    "dr-althea-345": "Glass Skin",
    "axis-y-dark-spot": "Dark Spots",
    "arencia-rice-cleanser": "Bright Cleanse",
    "complex-15-cream": "Dry Skin",
    "azelaic-acid-10": "Even Tone",
    "ashwagandha-ksm66": "Stress & Sleep",
    "organika-collagen": "Hair, Skin & Nails",
    "probiotic-30b": "Gut Health",
    "truskin-vitamin-c": "Brightness",
    "ordinary-hyaluronic": "Budget Hydration",
    "ombrelle-spf60": "Daily SPF",
    "myhalos-sleep-mask": "Blackout Sleep",
    "schiara-posture": "Posture",
    "philips-wake-up": "Mornings",
    "b12-2500": "Energy Metabolism",
    "turmeric-curcumin": "Joint Comfort",
    "melatonin-10mg": "Falling Asleep",
    "cerave-cream": "24hr Moisture",
    "ordinary-niacinamide": "Pores & Oil",
    "hydro-boost-gel": "Lightweight Hydration",
    "acupressure-mat": "Back Relief",
    "scalp-massager": "Scalp Care",
    "olaplex-no3": "Damaged Hair",
}

# PDP-only copy for the verdict-first layout (redesign 2026-10).
# Derived strictly from the approved pitch/rule/skip copy above — no new claims.



PDP_COPY = {
    "magnesium-glycinate": {
        "verdict": "A magnesium bisglycinate in the label form worth checking for: "
                   "glycinate, not oxide. It\u2019s a source of magnesium \u2014 a mineral "
                   "that helps maintain proper muscle function and plays a role in "
                   "tissue formation.",
        "getif": [
            "You read labels \u2014 \u201cglycinate\u201d, not \u201coxide\u201d.",
            "You check for a third-party testing seal before you buy.",
            "You want a mineral source for muscle function and tissue formation.",
        ],
        "key": "200 mg bisglycinate per capsule \u2014 glycinate, not oxide",
    },
    "creatine-monohydrate": {
        "verdict": "Plain creatine monohydrate \u2014 the single ingredient is the "
                   "whole point. One of the most studied sports supplements out "
                   "there, it supports lean mass and strength gains when combined "
                   "with resistance training.",
        "getif": [
            "You\u2019ll take it daily \u2014 consistency is the whole game.",
            "You\u2019re doing resistance training.",
            "You want one ingredient: no blends, no \u201cmatrix\u201d.",
        ],
        "key": "Plain monohydrate \u2014 one ingredient, no blends",
    },
    "omega-3-fish-oil": {
        "verdict": "A source of EPA and DHA omega-3 fatty acids for the maintenance "
                   "of good health. The real pick here is the facts panel: EPA/DHA "
                   "per serving \u2014 not just \u201c1000 mg fish oil\u201d \u2014 with "
                   "molecularly distilled as a plus.",
        "getif": [
            "You don\u2019t eat fatty fish twice a week.",
            "You compare EPA/DHA per serving, not the front label.",
            "You want the unglamorous daily, not a miracle bottle.",
        ],
        "key": "EPA + DHA per serving \u2014 check the facts panel",
    },
    "zinc-citrate": {
        "verdict": "A zinc citrate \u2014 citrate over oxide for absorption. It\u2019s a "
                   "source of zinc, an essential mineral involved in tissue "
                   "formation, and it comes with one dose rule worth respecting: "
                   "more is not more with zinc.",
        "getif": [
            "Your multivitamin doesn\u2019t already include zinc.",
            "You prefer citrate or picolinate over oxide.",
            "You\u2019ll take it with food if it bothers your stomach.",
        ],
        "key": "Citrate form \u2014 not oxide; keep the dose sane",
    },
    "vitamin-d3-k2": {
        "verdict": "D3 with K2 (MK-7) in one capsule \u2014 never solo. It helps in "
                   "the development and maintenance of bones and teeth, and helps "
                   "the body absorb calcium.",
        "getif": [
            "You see little midday sun through the Canadian winter.",
            "You want D3 with K2 (MK-7) in one capsule.",
            "You check that the dose per softgel is clearly stated.",
        ],
        "key": "D3 with K2 (MK-7) in one capsule \u2014 never solo",
    },
    "vichy-dercos": {
        "verdict": "The pharmacy-aisle answer to flakes: an anti-dandruff shampoo "
                   "that visibly reduces them for a calmer-feeling scalp. "
                   "Pharmacy-aisle serious \u2014 not salon-perfume serious.",
        "getif": [
            "Flakes keep coming back.",
            "You want results, not salon perfume.",
            "Your scalp needs calmer, not harsher.",
        ],
        "key": "Anti-dandruff \u2014 visibly reduces flakes",
    },
    "retinal-shot-booster": {
        "verdict": "The vitamin-A pick for people who read the ingredient list: "
                   "0.1% retinal (the advanced form of retinol) with micro-fine "
                   "A-Shot particles, plus Matrixyl. Made for the appearance of "
                   "firmer skin and tighter-looking pores \u2014 at night, with "
                   "sunscreen the morning after.",
        "getif": [
            "You\u2019ve used vitamin A before and your skin tolerates it.",
            "You want retinal named on the label \u2014 not just \u201cretinol\u201d.",
            "You\u2019ll commit to nights only, plus sunscreen the next morning.",
        ],
        "key": "0.1% retinal + A-Shot \u2014 nights only, sunscreen after",
    },
    "dr-althea-345": {
        "verdict": "The glass-skin cream that starts with calm: niacinamide in a "
                   "fragrance-free base, made for an even-looking, dewy finish on "
                   "all skin types. Calm first, glow second.",
        "getif": [
            "You want the glass-skin finish without fragrance.",
            "Your skin likes niacinamide.",
            "You\u2019d rather calm first, treat second.",
        ],
        "key": "Niacinamide cream \u2014 fragrance-free, glass-skin finish",
    },
    "axis-y-dark-spot": {
        "verdict": "The dark-spot serum for the patient: a niacinamide formula "
                   "that targets the appearance of dark spots and post-blemish "
                   "marks for a more even-looking tone \u2014 on a timeline of "
                   "weeks, not days.",
        "getif": [
            "Your marks are post-blemish, not active breakouts.",
            "You\u2019ll wear sunscreen daily \u2014 non-negotiable for spots.",
            "You can give it weeks before judging.",
        ],
        "key": "Niacinamide serum \u2014 for the look of dark spots",
    },
    "arencia-rice-cleanser": {
        "verdict": "The cleanser with the mochi texture: rice powder\u2019s gentle "
                   "exfoliation plus a hydrating finish \u2014 brightening angle "
                   "included, squeaky-tight finish not.",
        "getif": [
            "You want a cleanser that exfoliates gently while it cleans.",
            "Your skin likes rice-based brightening.",
            "You hate the tight-after-wash feeling.",
        ],
        "key": "Rice-powder mochi cleanser \u2014 brightening, hydrating finish",
    },
    "complex-15-cream": {
        "verdict": "The Canadian pharmacy workhorse: a propylene-glycol daily "
                   "face cream \u2014 hypoallergenic, unscented, non-greasy, "
                   "oil-free \u2014 built to restore the look of the skin\u2019s "
                   "natural moisture balance without the perfume.",
        "getif": [
            "Your skin runs dry, especially in winter.",
            "You want a humectant cream without fragrance.",
            "You trust the boring pharmacy tube over the pretty one.",
        ],
        "key": "Propylene glycol cream \u2014 hypoallergenic, unscented",
    },
    "azelaic-acid-10": {
        "verdict": "The quiet multitasker: a 10% azelaic acid suspension for the "
                   "look of blemishes, redness, and uneven tone in one step \u2014 "
                   "with the standard honest timeline of weeks.",
        "getif": [
            "You want one step for the look of blemishes + uneven tone.",
            "You\u2019ll give it weeks, not days.",
            "You patch-test new actives like a responsible adult.",
        ],
        "key": "10% azelaic acid \u2014 the even-tone multitasker",
    },
    "ashwagandha-ksm66": {
        "verdict": "People say KSM-66 ashwagandha calmed their stress and fixed "
                   "their sleep \u2014 one reviewer went from 2\u20133 hours of "
                   "broken sleep to 7\u20138 hours. This is the KSM-66 extract "
                   "form \u2014 the one with studies behind it \u2014 not generic "
                   "root powder.",
        "getif": [
            "Stress needs a dial-down, not a pep talk.",
            "You want \u201cKSM-66\u201d on the label \u2014 the studied extract.",
            "Better sleep is the goal, not just \u201crelaxation\u201d.",
        ],
        "key": "KSM-66 extract \u2014 the studied ashwagandha form",
    },
    "organika-collagen": {
        "verdict": "People say their hair got thicker, nails stronger, skin "
                   "plumper \u2014 13,500+ ratings on a Canadian-made powder. "
                   "Unflavoured 500g that disappears into coffee; the long game, "
                   "not a week-long miracle.",
        "getif": [
            "You want the hair-skin-nails routine in one scoop.",
            "Canadian-made with transparent sourcing matters to you.",
            "Unflavoured is non-negotiable \u2014 you\u2019re mixing it into things.",
        ],
        "key": "500g unflavoured collagen \u2014 Canadian-made",
    },
    "probiotic-30b": {
        "verdict": "4.6 stars across 4,300+ ratings \u2014 people say it sorted "
                   "their bloating and gut issues. 30 billion CFU across 8 "
                   "strains in one daily capsule; strain count is the quick "
                   "filter on a crowded shelf.",
        "getif": [
            "Bloating is your unwelcome roommate.",
            "You want multi-strain \u2014 8 strains, not a sprinkle of one.",
            "One capsule daily beats a handful of pills.",
        ],
        "key": "30B CFU, 8 strains \u2014 one capsule daily",
    },
    "truskin-vitamin-c": {
        "verdict": "106,000+ ratings \u2014 people say their skin looks brighter "
                   "and their spots are fading. One reviewer called it the "
                   "\u201cbest $20 ever spent.\u201d Vitamin C without the luxury "
                   "markup, with sunscreen every morning as the package deal.",
        "getif": [
            "Dullness is the complaint; brightness is the goal.",
            "You want vitamin C without the $80 serum.",
            "Dark spots need fading, not covering.",
        ],
        "key": "Vitamin C serum \u2014 for the look of brightness",
    },
    "ordinary-hyaluronic": {
        "verdict": "The cult budget hydrator: 2% hyaluronic acid with B5. A "
                   "73-year-old reviewer said it virtually erased her fine "
                   "lines. Apply to damp skin, seal with moisturizer \u2014 "
                   "that\u2019s the whole technique, and the price doesn\u2019t hurt.",
        "getif": [
            "Your skin drinks water and asks for more.",
            "You want hydration without the $60 serum.",
            "Fine lines look worse on dehydrated skin.",
        ],
        "key": "2% hyaluronic acid + B5 \u2014 budget hydration",
    },
    "ombrelle-spf60": {
        "verdict": "Canada\u2019s daily sunscreen: SPF 60 that doesn\u2019t feel "
                   "like SPF 60. Lightweight, no white cast, no sticky residue "
                   "\u2014 the three reasons people skip sunscreen, removed. The "
                   "best SPF is the one you\u2019ll actually wear every morning.",
        "getif": [
            "You skip sunscreen because it\u2019s greasy or white.",
            "Daily wear matters more than beach-day SPF.",
            "Anti-shine finish suits oily and combination skin.",
        ],
        "key": "SPF 60 \u2014 lightweight, no white cast",
    },
    "myhalos-sleep-mask": {
        "verdict": "The Amazon\u2019s Choice sleep mask: 100% blackout with zero "
                   "eye pressure, thanks to the 3D contour \u2014 your eyelids "
                   "never touch fabric. Memory foam, adjustable strap. People "
                   "who struggle to fall asleep call it a game-changer.",
        "getif": [
            "Light leaks ruin your sleep.",
            "Flat masks press on your eyes \u2014 you hate that.",
            "Total darkness is what finally lets you drop off.",
        ],
        "key": "3D contoured blackout \u2014 zero eye pressure",
    },
    "schiara-posture": {
        "verdict": "30,000+ ratings \u2014 a chiropractor noticed the difference "
                   "in weeks. It trains muscle memory for straighter posture "
                   "rather than just yanking shoulders back; adjustable and "
                   "unisex, because a corrector that doesn\u2019t fit doesn\u2019t "
                   "get worn.",
        "getif": [
            "Your desk is turning you into a shrimp.",
            "You want posture training, not a brace worn forever.",
            "Adjustable fit matters \u2014 one size never fits all.",
        ],
        "key": "Adjustable corrector \u2014 trains posture habits",
    },
    "philips-wake-up": {
        "verdict": "14,000+ ratings \u2014 it mimics sunrise with gradually "
                   "brightening light so you wake up actually feeling ready. "
                   "One reviewer called it \u201ca necessity I didn\u2019t know I "
                   "needed.\u201d Light does the waking; sound is the backup.",
        "getif": [
            "Alarms make you feel attacked every morning.",
            "Winter mornings are brutally dark.",
            "You\u2019d rather surface gradually than be jolted.",
        ],
        "key": "Sunrise simulation \u2014 wake up to light",
    },
    "b12-2500": {
        "verdict": "A high-potency B12 \u2014 2500 mcg in cherry fast-dissolve tablets. B12 helps prevent deficiency and supports energy metabolism, and the fast-dissolve form is the easy daily.",
        "getif": [
            "You want B12 for energy metabolism and deficiency prevention.",
            "You prefer fast-dissolve over hard-pressed tablets.",
            "You check that the dose is real, not a sprinkle.",
        ],
        "key": "2500 mcg fast-dissolve \u2014 the easy B12 daily",
    },
    "turmeric-curcumin": {
        "verdict": "Turmeric curcumin with black pepper extract \u2014 the pepper is what makes the curcumin absorb. For joint comfort and everyday inflammation support.",
        "getif": [
            "You check for piperine on the label, not just turmeric.",
            "You want standardized curcuminoids, not powder.",
            "You understand this is daily support, not a painkiller.",
        ],
        "key": "Curcumin + black pepper \u2014 absorption is the point",
    },
    "melatonin-10mg": {
        "verdict": "A dual-action melatonin \u2014 fast release to fall asleep, sustained release to stay there. The training-wheels bottle for a scrambled sleep cycle.",
        "getif": [
            "You fall asleep fine but wake at 3 AM.",
            "Your sleep cycle is scrambled and needs a reset.",
            "You\u2019ll start low and fix the habit alongside.",
        ],
        "key": "Dual-action 10 mg \u2014 fall asleep and stay asleep",
    },
    "cerave-cream": {
        "verdict": "The dermatologist-named tub: three essential ceramides plus hyaluronic acid, fragrance-free, 24-hour hydration. The workhorse moisturizer.",
        "getif": [
            "You want ceramides doing the barrier work.",
            "Fragrance-free matters for your face.",
            "You need 24-hour hydration, not a 4-hour glow.",
        ],
        "key": "Ceramides + hyaluronic acid \u2014 the barrier tub",
    },
    "ordinary-niacinamide": {
        "verdict": "10% niacinamide with 1% zinc \u2014 51,000+ reviews. The oil-regulating, pore-refining serum at a price that makes no sense.",
        "getif": [
            "Oily T-zone is your daily reality.",
            "You want the look of refined pores.",
            "You\u2019ll patch-test and wear sunscreen.",
        ],
        "key": "10% niacinamide + 1% zinc \u2014 oil and pores",
    },
    "hydro-boost-gel": {
        "verdict": "A hyaluronic gel-cream for instant, lightweight hydration \u2014 never greasy. The drugstore hydrator that punches above its price.",
        "getif": [
            "Heavy creams feel like a mask on you.",
            "You want instant hydration that layers well.",
            "Greasy is a dealbreaker.",
        ],
        "key": "Hyaluronic gel-cream \u2014 light, never greasy",
    },
    "acupressure-mat": {
        "verdict": "An acupressure mat plus pillow for back and neck relief \u2014 lie back for 20 minutes and decompress. Sharp at first, bliss after.",
        "getif": [
            "Your back and neck carry the day\u2019s tension.",
            "You want the pillow included, not sold separately.",
            "You\u2019ll start with a shirt on and build up.",
        ],
        "key": "Mat + pillow set \u2014 the 20-minute reset",
    },
    "scalp-massager": {
        "verdict": "A cordless, waterproof scalp massager with deep-kneading nodes \u2014 the best head massage you\u2019ve had at home, on demand.",
        "getif": [
            "Tension lives in your scalp and neck.",
            "Cordless and waterproof are non-negotiable.",
            "You want multiple speeds, not one.",
        ],
        "key": "Cordless deep-knead \u2014 waterproof scalp relief",
    },
    "olaplex-no3": {
        "verdict": "No.3 \u2014 the at-home bond builder with 22,000+ reviews. A pre-shampoo treatment that repairs the look of damaged hair and reduces breakage.",
        "getif": [
            "Heat, bleach, or color has done damage.",
            "You want the take-home treatment, not the shampoo.",
            "You\u2019ll give it 10+ minutes on damp hair.",
        ],
        "key": "No.3 bond builder \u2014 pre-shampoo repair",
    },
}
for p in PRODUCTS:
    p["badge"] = "Best for " + BADGES[p["slug"]]
    p.update(PDP_COPY[p["slug"]])

# Shop-by-job themes (R2, full-redesign plan Sections 4 and 7). Every
# "Best for" job sits in exactly one theme; rail counts come from this map.



PHOTOS = {
    "magnesium-glycinate": [
        "images/products/mg-glycinate-webber-1.jpg",
    ],
    "creatine-monohydrate": [
        "images/products/creatine-monohydrate-2.jpg",
    ],
    "omega-3-fish-oil": [
        "images/products/omega-3-1.jpg",
    ],
    "zinc-citrate": [
        "images/products/zinc-citrate.jpg",
    ],
    "vitamin-d3-k2": [
        "images/products/vitamin-d3-k2.jpg",
    ],
    "vichy-dercos": [
        "images/products/vichy-dercos.jpg",
    ],
    "retinal-shot-booster": [
        "images/products/retinal-shot-celimax.webp",
    ],
    "dr-althea-345": [
        "images/products/dr-althea-345.jpg",
    ],
    "axis-y-dark-spot": [
        "images/products/axis-y-dark-spot.jpg",
    ],
    "arencia-rice-cleanser": [
        "images/products/arencia-rice-cleanser.jpg",
    ],
    "complex-15-cream": [
        "images/products/complex-15.jpg",
    ],
    "azelaic-acid-10": [
        "images/products/azelaic-acid-10.png",
    ],
    "ashwagandha-ksm66": [
        "images/products/ashwagandha-ksm66.jpg",
    ],
    "organika-collagen": [
        "images/products/organika-collagen.jpg",
    ],
    "probiotic-30b": [
        "images/products/probiotic-30b.jpg",
    ],
    "truskin-vitamin-c": [
        "images/products/truskin-vitamin-c.jpg",
    ],
    "ordinary-hyaluronic": [
        "images/products/ordinary-hyaluronic.jpg",
    ],
    "ombrelle-spf60": [
        "images/products/ombrelle-spf60.jpg",
    ],
    "myhalos-sleep-mask": [
        "images/products/myhalos-sleep-mask.jpg",
    ],
    "schiara-posture": [
        "images/products/schiara-posture.jpg",
    ],
    "philips-wake-up": [
        "images/products/philips-wake-up.jpg",
    ],
    "b12-2500": [
        "images/products/b12-2500.jpg",
    ],
    "turmeric-curcumin": [
        "images/products/turmeric-curcumin.jpg",
    ],
    "melatonin-10mg": [
        "images/products/melatonin-10mg.jpg",
    ],
    "cerave-cream": [
        "images/products/cerave-cream.jpg",
    ],
    "ordinary-niacinamide": [
        "images/products/ordinary-niacinamide.jpg",
    ],
    "hydro-boost-gel": [
        "images/products/hydro-boost-gel.jpg",
    ],
    "acupressure-mat": [
        "images/products/acupressure-mat.jpg",
    ],
    "scalp-massager": [
        "images/products/scalp-massager.jpg",
    ],
    "olaplex-no3": [
        "images/products/olaplex-no3.jpg",
    ],
}
for p in PRODUCTS:
    p["photos"] = PHOTOS.get(p["slug"], [])
    p["cart_url"] = ("https://www.amazon.ca/gp/aws/cart/add.html?AssociateTag=%s"
                     "&ASIN.1=%s&Quantity.1=1" % (TAG, p["asin"]))



PDP_EXTRA = {
    "magnesium-glycinate": {
        "bullets": [
            "A source of magnesium \u2014 a mineral that helps maintain proper muscle function and plays a role in tissue formation.",
            "Glycinate form, not oxide \u2014 check the label.",
            "Look for a third-party testing seal.",
        ],
        "desc": [
            "Not all magnesium is the same bottle. This pick is magnesium bisglycinate \u2014 the form worth checking for on the label \u2014 and it earns its spot the usual way: a real job to do, label math that checks out, and an honest skip-list.",
            "The buying rule is short: \u201cglycinate\u201d on the label, not \u201coxide\u201d, plus a third-party testing seal. If the cheaper bottle checks both boxes, buy the cheaper bottle.",
        ],
    },
    "creatine-monohydrate": {
        "bullets": [
            "Supports lean mass and strength gains when combined with resistance training.",
            "One of the most studied sports supplements out there.",
            "Plain creatine monohydrate \u2014 no blends, no \u201cmatrix\u201d.",
        ],
        "desc": [
            "The least exotic pick on the list, and that\u2019s the point. Creatine monohydrate is one of the most studied sports supplements out there, supporting lean mass and strength gains when combined with resistance training.",
            "The entire buying criteria fits in one line: plain creatine monohydrate. No blends, no \u201cmatrix\u201d, no fairy dust \u2014 the single ingredient is the whole point.",
        ],
    },
    "omega-3-fish-oil": {
        "bullets": [
            "A source of EPA and DHA omega-3 fatty acids for the maintenance of good health.",
            "Check EPA/DHA per serving on the facts panel \u2014 not just \u201c1000mg fish oil\u201d.",
            "Molecularly distilled is a plus.",
        ],
        "desc": [
            "The unglamorous daily. A source of EPA and DHA omega-3 fatty acids for the maintenance of good health \u2014 the kind of bottle you buy for the facts panel, not the front label.",
            "Check EPA/DHA per serving, not just \u201c1000mg fish oil\u201d. Molecularly distilled is a plus.",
        ],
    },
    "zinc-citrate": {
        "bullets": [
            "A source of zinc \u2014 an essential mineral involved in tissue formation.",
            "Citrate or picolinate over oxide for absorption.",
            "Keep the dose sane \u2014 more is not more with zinc.",
        ],
        "desc": [
            "An essential mineral involved in tissue formation and everyday cellular housekeeping. The form matters more than the brand here: citrate or picolinate over oxide for absorption.",
            "And the dose discipline matters too \u2014 keep it sane, because more is not more with zinc.",
        ],
    },
    "vitamin-d3-k2": {
        "bullets": [
            "Helps in the development and maintenance of bones and teeth.",
            "Helps the body absorb calcium.",
            "D3 <i>with</i> K2 (MK-7) in one capsule \u2014 never solo; dose per softgel clearly stated.",
        ],
        "desc": [
            "The Canadian-winter pick. Helps in the development and maintenance of bones and teeth, and helps the body absorb calcium.",
            "The rule that earned it a spot: D3 <i>with</i> K2 (MK-7) in one capsule, dose per softgel clearly stated. D3 alone at a premium? Keep walking.",
        ],
    },
    "vichy-dercos": {
        "bullets": [
            "Anti-dandruff shampoo that visibly reduces flakes for a calmer-feeling scalp.",
            "Pharmacy-aisle serious, not salon-perfume serious.",
        ],
        "desc": [
            "Flakes are a confidence tax, and this is the pharmacy-aisle answer. An anti-dandruff shampoo that visibly reduces flakes for a calmer-feeling scalp.",
            "Serious about the job, not about smelling like a salon \u2014 that\u2019s exactly why it made a list called Zero Regret Buys.",
        ],
    },
    "retinal-shot-booster": {
        "bullets": [
            "0.1% retinal \u2014 the advanced form of retinol \u2014 with micro-fine A-Shot particles.",
            "Made for the appearance of firmer skin and tighter-looking pores.",
            "Nighttime use only; sunscreen the following morning is non-negotiable.",
        ],
        "desc": [
            "Retinal is retinol\u2019s faster-acting sibling, and this booster names it plainly: 0.1% retinal with micro-fine A-Shot particles, plus Matrixyl for the look of elasticity.",
            "The honest part is the routine, not the bottle \u2014 every other night for the first two weeks, a small amount on target areas, moisturizer if it nips, and sunscreen every morning after. Vitamin A rewards patience and punishes enthusiasm.",
        ],
    },
    "dr-althea-345": {
        "bullets": [
            "Niacinamide cream made for an even-looking, dewy finish.",
            "No artificial fragrance; made for all skin types.",
            "The calm step \u2014 pairs under stronger actives, not instead of them.",
        ],
        "desc": [
            "Glass skin is mostly evenness plus hydration, and this is the evenness tube: niacinamide in a fragrance-free cream base, built to leave skin looking calm and dewy rather than matte.",
            "It\u2019s the supporting actor of the shelf \u2014 the cream you reach for when your skin wants soothing, not stripping. Strong actives do the drama; this does the recovery.",
        ],
    },
    "axis-y-dark-spot": {
        "bullets": [
            "Niacinamide serum for the appearance of dark spots and post-blemish marks.",
            "Built for a more even-looking skin tone with consistent use.",
            "Sunscreen daily \u2014 no brightening serum outruns the sun.",
        ],
        "desc": [
            "Dark spots fade on a timeline measured in weeks, and this serum is built for exactly that: niacinamide aimed at the look of post-blemish marks and uneven tone.",
            "The unglamorous truth is the second ingredient \u2014 sunscreen. Every morning, no exceptions. The serum does the fading; the sunscreen keeps new marks from taking their place.",
        ],
    },
    "arencia-rice-cleanser": {
        "bullets": [
            "Rice powder for gentle exfoliation while cleansing.",
            "Hydrating, deep-cleansing finish \u2014 not squeaky-tight.",
            "The brightening angle comes from the rice, not hype.",
        ],
        "desc": [
            "This is the green tube from the screenshots: a mochi-textured cleanser built around rice powder \u2014 gentle exfoliation plus a hydrating cleanse, with brightening as the bonus.",
            "The test every cleanser has to pass is the after-feel. This one aims for clean and comfortable, not tight. If your face feels like it shrank, the cleanser failed \u2014 this one doesn\u2019t.",
        ],
    },
    "complex-15-cream": {
        "bullets": [
            "Propylene glycol base \u2014 hypoallergenic, unscented, non-greasy, oil-free.",
            "Made to restore the look of the skin\u2019s natural moisture balance.",
            "100 mL of no-nonsense: moisture first, marketing never.",
        ],
        "desc": [
            "The viral cheap-cream slot needed a Canadian resident, and this is it: a propylene glycol daily face cream whose entire purpose is helping dry skin look and feel moisturized.",
            "Hypoallergenic, unscented, non-greasy, non-comedogenic \u2014 the four words that matter on a workhorse cream. Boring is the feature.",
        ],
    },
    "azelaic-acid-10": {
        "bullets": [
            "10% azelaic acid suspension, clearly stated.",
            "For the look of blemish-prone skin and a more even tone.",
            "Works on the appearance of tone over weeks of consistent use.",
        ],
        "desc": [
            "Azelaic acid is the ingredient that does three jobs quietly: the look of blemishes, the look of redness, the look of uneven tone. This is it at 10%, stated plainly, in a no-frills suspension.",
            "No fragrance story, no 12-step ritual \u2014 one tube, consistent use, weeks of patience. The multitasker that doesn\u2019t brag is usually the one worth keeping.",
        ],
    },
    "ashwagandha-ksm66": {
        "bullets": [
            "KSM-66 ashwagandha extract \u2014 7200mg equivalent per serving.",
            "The studied extract form, not generic root powder.",
            "60 capsules.",
        ],
        "desc": [
            "Ashwagandha is everywhere, but KSM-66 is the extract with the studies behind it. People say it calmed their stress and \u2014 more specifically \u2014 fixed their sleep, with one reviewer going from 2\u20133 broken hours to 7\u20138.",
            "The buying rule fits on the label: \u201cKSM-66\u201d, not just \u201cashwagandha root\u201d. The extract is the whole point \u2014 everything else is marketing dust.",
        ],
    },
    "organika-collagen": {
        "bullets": [
            "Enhanced collagen powder \u2014 500g, unflavoured.",
            "Canadian-made with transparent sourcing.",
            "For hair, skin, and nails \u2014 per the people who take it.",
        ],
        "desc": [
            "Collagen is a long game, and this is the Canadian-made powder people stick with: unflavoured, 500g, built for the hair-skin-nails routine. It disappears into coffee \u2014 no clumps, no taste negotiations.",
            "People say their hair got thicker and their nails stronger. It won\u2019t work in a week \u2014 but 13,500+ ratings suggest people keep refilling for a reason.",
        ],
    },
    "probiotic-30b": {
        "bullets": [
            "30 billion CFU across 8 probiotic strains.",
            "One capsule daily \u2014 no handful of pills.",
            "4.6 stars across 4,300+ ratings.",
        ],
        "desc": [
            "Probiotics are a crowded shelf, and strain count is the quick filter: 8 strains at 30 billion CFU in a single daily capsule is the spec that matters here.",
            "People say it sorted their bloating and gut issues. The 4.6-star average across 4,300+ ratings is the social proof doing the talking \u2014 consistency does the rest.",
        ],
    },
    "truskin-vitamin-c": {
        "bullets": [
            "Vitamin C serum for brighter-looking skin.",
            "Targets the look of dark spots and uneven tone.",
            "30ml \u2014 morning use, sunscreen after.",
        ],
        "desc": [
            "Vitamin C is the brightness workhorse, and this is the bottle with 106,000+ ratings behind it. People say their skin looks brighter and their spots are fading \u2014 one reviewer called it the best $20 ever spent.",
            "Morning use, sunscreen after \u2014 vitamin C and sun protection are a package deal. The serum does the brightening; the sunscreen keeps new spots from taking its place.",
        ],
    },
    "ordinary-hyaluronic": {
        "bullets": [
            "2% hyaluronic acid with vitamin B5.",
            "For dehydrated skin and the look of fine lines.",
            "30ml \u2014 the budget hero of hydration.",
        ],
        "desc": [
            "Hyaluronic acid is a humectant \u2014 it pulls water into skin \u2014 and this is the bottle that proved it doesn\u2019t need to cost $60. 2% HA plus B5, no frills, no fragrance story.",
            "A 73-year-old reviewer said it virtually erased her fine lines. The technique is the whole product: apply to damp skin, seal with moisturizer. Skip the seal and you skip the result.",
        ],
    },
    "ombrelle-spf60": {
        "bullets": [
            "SPF 60 sun protection in a daily-wear formula.",
            "Lightweight anti-shine finish \u2014 no white cast.",
            "90ml \u2014 made for every morning, not just beach days.",
        ],
        "desc": [
            "Ombrelle is Canada\u2019s sunscreen for a reason: SPF 60 that doesn\u2019t feel like SPF 60. Lightweight, no white cast, no sticky residue \u2014 the three reasons people skip sunscreen, removed.",
            "Reviewers call it a daily staple, and the anti-shine finish makes it the pick for oily and combination skin. The best sunscreen is the one that actually makes it onto your face.",
        ],
    },
    "myhalos-sleep-mask": {
        "bullets": [
            "3D contoured design for 100% blackout.",
            "Memory foam \u2014 zero pressure on the eyes.",
            "Adjustable strap; one mask fits most.",
        ],
        "desc": [
            "Flat sleep masks press on your eyelids; this one doesn\u2019t. The 3D contour creates space around your eyes \u2014 total darkness with nothing touching your lids \u2014 in memory foam with an adjustable strap.",
            "It carries the Amazon\u2019s Choice badge, and the reviews read like relief: people who struggled to fall asleep call it a game-changer. Darkness is a sleep signal, and this delivers it fully.",
        ],
    },
    "schiara-posture": {
        "bullets": [
            "Adjustable, unisex posture corrector.",
            "Trains muscle memory \u2014 not a brace you wear forever.",
            "30,000+ ratings.",
        ],
        "desc": [
            "Posture correctors work by reminding your muscles where they should be \u2014 and this is the one with 30,000+ ratings doing exactly that. A chiropractor noticed the difference in weeks.",
            "Adjustable and unisex, which matters because a corrector that doesn\u2019t fit doesn\u2019t get worn. The goal is training, not dependence: wear it for periods, build the habit, then rely on the habit.",
        ],
    },
    "philips-wake-up": {
        "bullets": [
            "Simulates sunrise with gradually brightening light.",
            "Gentle wake-up \u2014 light first, sound as backup.",
            "14,000+ ratings.",
        ],
        "desc": [
            "Being jolted awake by sound is a stress response; being eased awake by light isn\u2019t. This simulates sunrise \u2014 gradually brightening over 30 minutes \u2014 so you surface naturally instead of surfacing scared.",
            "14,000+ ratings, and the reviews read like conversions: skeptics who mocked it, then couldn\u2019t go back. One called it a necessity they didn\u2019t know they needed.",
        ],
    },
    "b12-2500": {
        "bullets": [
            "High-potency B12 \u2014 2500 mcg for energy metabolism.",
            "Helps prevent B12 deficiency.",
            "Cherry-flavoured fast-dissolve tablets.",
        ],
        "desc": [
            "B12 deficiency is more common than the energy-drink aisle admits, and the fix is simpler than the marketing: a real dose in a form you\u2019ll actually take. Cherry fast-dissolve beats a horse-pill you skip.",
            "The buying rule is one line: fast-dissolve at a real dose. If it\u2019s a tiny dose in a hard-pressed tablet, keep walking.",
        ],
    },
    "turmeric-curcumin": {
        "bullets": [
            "Turmeric curcumin with black pepper extract for absorption.",
            "Standardized curcuminoids \u2014 not just turmeric powder.",
            "For joint comfort and everyday inflammation support.",
        ],
        "desc": [
            "Curcumin barely absorbs on its own \u2014 that\u2019s the open secret of the turmeric aisle. Black pepper extract (piperine) is what makes it bioavailable, which is why it\u2019s on this label.",
            "Standardized curcuminoids, piperine on the label, daily consistency. That\u2019s the whole formula \u2014 everything else is packaging.",
        ],
    },
    "melatonin-10mg": {
        "bullets": [
            "Dual-action: fast release plus sustained release.",
            "Helps you fall asleep faster.",
            "Resets a scrambled sleep cycle.",
        ],
        "desc": [
            "Single-release melatonin wears off at 3 AM \u2014 ask anyone who\u2019s stared at the ceiling since. Dual-action covers both jobs: fast release to fall asleep, sustained release to stay there.",
            "Start low, fix the habit alongside, and treat the bottle as training wheels \u2014 not a permanent passenger. Vivid dreams are a known side effect, not a malfunction.",
        ],
    },
    "cerave-cream": {
        "bullets": [
            "Three essential ceramides plus hyaluronic acid.",
            "24-hour hydration; dermatologist-developed.",
            "Fragrance-free.",
        ],
        "desc": [
            "The tub dermatologists actually name. Three essential ceramides do the barrier work, hyaluronic acid holds the water, and the fragrance-free formula means faces tolerate it.",
            "This is the rich cream \u2014 the workhorse for dry to normal skin. Very oily? The lotion is the lighter sibling.",
        ],
    },
    "ordinary-niacinamide": {
        "bullets": [
            "10% niacinamide with 1% zinc.",
            "Regulates oil; refines the look of pores.",
            "51,000+ reviews.",
        ],
        "desc": [
            "Niacinamide is the rare active that does two jobs at once: visibly refines pores and regulates oil \u2014 which is why 51,000+ reviewers keep buying the ten-dollar tube.",
            "10% clearly stated, sunscreen every morning, patch-test first. No serum outruns the sun, and tingling at first isn\u2019t for everyone.",
        ],
    },
    "hydro-boost-gel": {
        "bullets": [
            "Hyaluronic gel-cream for instant hydration.",
            "Lightweight texture \u2014 never greasy.",
            "Layers well under makeup and sunscreen.",
        ],
        "desc": [
            "Some hydrators feel like a second skin; this one feels like no skin at all. The gel-cream texture delivers hyaluronic hydration without the weight \u2014 which is exactly why it layers under makeup instead of pilling.",
            "The drugstore hydrator that punches above its price. If it feels heavy, it failed the only test that matters.",
        ],
    },
    "acupressure-mat": {
        "bullets": [
            "Acupressure mat plus pillow for back and neck.",
            "Deep relaxation in ~20 minutes.",
            "Drug-free tension relief.",
        ],
        "desc": [
            "Thousands of small spikes, one simple idea: lie back, breathe, and let the pressure do what your thumbs can\u2019t. Twenty minutes on the mat reads like a reset button for backs and necks.",
            "Start with a shirt on \u2014 sharp at first is normal, painful is not. The included pillow is half the value; don\u2019t buy the mat alone.",
        ],
    },
    "scalp-massager": {
        "bullets": [
            "Deep-kneading nodes for scalp stress relief.",
            "Cordless and waterproof \u2014 shower-safe.",
            "Multiple speed settings.",
        ],
        "desc": [
            "Tension doesn\u2019t stop at the shoulders \u2014 it lives in the scalp too. Deep-kneading nodes work it out on demand, cordless and waterproof so the shower counts.",
            "If it needs a cord or fears water, it\u2019s the wrong one. Multiple speeds, not one \u2014 scalps have moods.",
        ],
    },
    "olaplex-no3": {
        "bullets": [
            "At-home bond builder \u2014 pre-shampoo treatment.",
            "Repairs the look of damaged hair; reduces breakage.",
            "22,000+ reviews.",
        ],
        "desc": [
            "No.3 is the take-home version of the salon bond-building step \u2014 applied to damp hair before shampooing, 10+ minutes, then wash as usual. Heat, bleach, and color damage is its home turf.",
            "This is a treatment, not a conditioner \u2014 don\u2019t expect it to replace one. Very fine hair: don\u2019t overdo the time.",
        ],
    },
}
for p in PRODUCTS:
    p.update(PDP_EXTRA[p["slug"]])

# "Add them all to cart": built from products with resolved ASINs only.
# Products still on LINK_TODO are skipped until their affiliate links land.



FAQS = [
    ("Why don\u2019t you show prices?",
     "Because they\u2019d be wrong by tomorrow. Amazon changes prices constantly, and typing a number here would mislead you. Click through \u2014 you\u2019ll see today\u2019s live price before you decide."),
    ("Do you earn a commission?",
     "Yes. Every product link on this site is a paid link, labeled as one \u2014 the commission costs you nothing extra."),
    ("Are these medical recommendations?",
     "No. These are general wellness descriptions, not medical advice. Supplements interact with medications and conditions \u2014 talk to your pharmacist or clinician before starting anything new."),
    ("Why only thirty products?",
     "One product per reel episode. The list grows as new episodes drop \u2014 that\u2019s the whole format. A hundred-item catalog would just be another store."),
]



def _cart_all_url():
    parts = []
    n = 0
    for p in PRODUCTS:
        if p["asin"] == "LINK_TODO":
            continue
        n += 1
        parts.append("ASIN.%d=%s&Quantity.%d=1" % (n, p["asin"], n))
    return ("https://www.amazon.ca/gp/aws/cart/add.html?AssociateTag=%s&%s"
            % (TAG, "&".join(parts)))


CART_ALL_URL = _cart_all_url()

CART_ALL_HTML = CART_ALL_URL.replace("&", "&amp;")

