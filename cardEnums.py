from enum import Enum

def enumMatch(enum, text):
    lookup = {e.value: e for e in enum}
    return lookup[text]

class CardExpansion(Enum):
    """ Represents the different expansions that a card can be from """
    The_First_Chapter = "The First Chapter"
    Rise_of_the_Floodborn = "Rise of the Floodborn"
    Into_the_Inklands = "Into the Inklands"

class CardClassification(Enum):
    """ Represents the different classifications that a card can have """
    Action = "Action"
    Alien = "Alien"
    Ally = "Ally"
    Broom = "Broom"
    Captian = "Captain"
    Deity = "Deity"
    Detective = "Detective"
    Dragon = "Dragon"
    Dreamborn = "Dreamborn"
    Fairy = "Fairy"
    Floodborn = "Floodborn"
    Hero = "Hero"
    Hyena = "Hyena"
    Inventor = "Inventor"
    Item = "Item"
    King = "King"
    Knight = "Knight"
    Location = "Location"
    Mentor = "Mentor"
    Musketeer = "Musketeer"
    Pirate = "Pirate"
    Prince = "Prince"
    Princess = "Princess"
    Puppy = "Puppy"
    Queen = "Queen"
    Seven_Dwarves = "Seven Dwarves"
    Song = "Song"
    Sorcerer = "Sorcerer"
    Storyborn = "Storyborn"
    Tigger = "Tigger"
    Titan = "Titan"
    Villain = "Villain"

class InkColor(Enum):
    """ Represents the different ink colors that a card can have """
    Amber = "Amber"
    Amethyst = "Amethyst"
    Emerald = "Emerald"
    Ruby = "Ruby"
    Sapphire = "Sapphire"
    Steel = "Steel"

class CardRarity(Enum):
    """ Represents the different rarities that a card can have """
    Common = "Common"
    Uncommon = "Uncommon"
    Rare = "Rare"
    Super_Rare = "Super Rare"
    Enchanted = "Enchanted"
    Legendary = "Legendary"
    Promo = "Promo"

class CardType(Enum):
    """ Represents the different types that a card can have """
    Character = "Character"
    Location = "Location"
    Action = "Action"
    Song = "Action • Song" # This is a special case
    Item = "Item"