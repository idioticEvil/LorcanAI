from enum import Enum
from abc import ABC, abstractmethod

class LorcanaCard(ABC):
    """ Represents a basic card in the game that all cards will inherit from """
    def __init__(self, card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity):
        self.card_id = card_id
        self.name = name
        self.version = version
        self.ink_color = ink_color
        self.cost = cost
        self.classifications = classifications
        self.image_url = image_url
        self.inkable = inkable
        self.expansion = expansion
        self.rarity = rarity

    @abstractmethod
    def some_method(self):
        pass

class AttributedCard(LorcanaCard, ABC):
    """ Subclass to represent cards with attributes """
    @abstractmethod
    def __init__(self, strength, willpower, loreVal, **kwargs):  
        super().__init__(**kwargs)
        self.strength = strength
        self.willpower = willpower
        self.loreVal = loreVal

class CharacterCard(AttributedCard):
    """ Subclass to represent character cards """
    def __init__(self, card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity, strength, willpower, loreVal, abilities, keywords):
        super().__init__(card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity, strength, willpower, loreVal)
        self.abilities = abilities
        self.keywords = keywords

class LocationCard(AttributedCard):
    """ Subclass to represent location cards """
    def __init__(self, card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity, strength, willpower, loreVal, abilities):
        super().__init__(card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity, strength, willpower, loreVal)
        self.abilities = abilities

class ActionCard(LorcanaCard):
    """ Subclass to represent action cards """
    def __init__(self, card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity, abilities):
        super().__init__(card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity)
        self.abilities = abilities


class SongCard(LorcanaCard):
    """ Subclass to represent song cards """
    def __init__(self, card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity, abilities):
        super().__init__(card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity)
        self.abilities = abilities


class ItemCard(LorcanaCard):
    """ Subclass to represent item cards """
    def __init__(self, card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity, abilities):
        super().__init__(card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity)
        self.abilities = abilities

class CardAbility:
    """ Represents an ability that a card can have """
    def __init__(self, name, description, exertion):
        self.name = name
        self.description = description
        self.exertion = exertion

class CardKeyword:
    """ Represents a keyword that a card can have """
    def __init__(self, name, description):
        self.name = name
        self.description = description

class CardClassification(Enum):
    """ Represents the different classifications that a card can have """
    Action = 1
    Alien = 2
    Ally = 3
    Broom = 4
    Captian = 5
    Deity = 6
    Detective = 7
    Dragon = 8
    Dreamborn = 9
    Fairy = 10
    Floodborn = 11
    Hero = 12
    Hyena = 13
    Inventor = 14
    Item = 15
    King = 16
    Knight = 17
    Location = 18
    Mentor = 19
    Musketeer = 20
    Pirate = 21
    Prince = 22
    Princess = 23
    Puppy = 24
    Queen = 25
    Seven_Dwarves = 26
    Song = 27
    Sorcerer = 28
    Storyborn = 29
    Tigger = 30
    Titan = 31
    Villain = 32

class InkColor(Enum):
    """ Represents the different ink colors that a card can have """
    Amber = 1
    Amethyst = 2
    Emerald = 3
    Ruby = 4
    Sapphire = 5
    Steel = 6
