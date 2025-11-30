import random


# Prefix for Name
PREFIXES = [
    "Shimmering", "Ancient", "Crystal", "Shadow", "Ethereal",
    "Molten", "Void", "Glowing", "Stormforged", "Icy", "Tiny"
]

# Species for Name
SPECIES = [
    "Trout", "Carp", "Eel", "Sting Ray", "Salmon", "Crab",
    "Guppy", "Shark", "Sea Horse", "Sea Snake", "Sponge",
    "Starfish", "Squirrel", "Squid", "Plankton", "Lobster"
]

COMMON_DESCRIPTIONS = [
    "A fairly common fish found.",
    "A peaceful swimmer that keeps to itself.",
    "Spends most of its day looking for snacks.",
    "Lives in a pineapple under the sea."
]

UNCOMMON_DESCRIPTIONS = [
    "A sturdy fish known to put up a decent fight.",
    "Prefers quiet coves and shaded waters.",
    "Not rare, but it's something I guess.",
    "Really loves Texas for some reason."
]

RARE_DESCRIPTIONS = [
    "Its scales shimmer like stardust under moonlight.",
    "Said to appear only when the waters fall silent.",
    "Finding one is considered a very good omen.",
    "Said to be looking for a secret formula."
]

LEGENDARY_DESCRIPTIONS = [
    "Legends claim it guides lost sailors to safety.",
    "Its presence seems to change the mood of the water.",
    "Said to have lived for centuries beneath the waves.",
    "Cover your ears, this one plays the clarinet, horribly."
]

MYTHIC_DESCRIPTIONS = [
    "A mythical creature most people only hear about in stories.",
    "Glows softly as if carrying ancient light inside... or it swallowed your tamagotchi.",
    "Old sailors insist this fish can change a person’s fate.",
    "Who you calling pinhead?"
]

RARITIES = ["Common", "Uncommon", "Rare", "Legendary", "Mythic"]

# Value will be anywhere between the listed values
RARITY_VALUE = {
    "Common": (5, 15),
    "Uncommon": (16, 40),
    "Rare": (41, 100),
    "Legendary": (101, 250),
    "Mythic": (251, 500)
}

# Maps descriptions to rarities
DESCRIPTION_MAP = {
    "Common": COMMON_DESCRIPTIONS,
    "Uncommon": UNCOMMON_DESCRIPTIONS,
    "Rare": RARE_DESCRIPTIONS,
    "Legendary": LEGENDARY_DESCRIPTIONS,
    "Mythic": MYTHIC_DESCRIPTIONS
}


def generate_fantasy_fish():
    """Generates a single fantasy fish dictionary"""
    prefix = random.choice(PREFIXES)
    species = random.choice(SPECIES)
    rarity = random.choice(RARITIES)
    name = f"{prefix} {species}"

    # Pick description based on rarity
    description = random.choice(DESCRIPTION_MAP[rarity])

    # Random value in range of rarity
    min_val, max_val = RARITY_VALUE[rarity]
    value = random.randint(min_val, max_val)

    return {
        "name": name,
        "description": description,
        "rarity": rarity,
        "value": value
    }
