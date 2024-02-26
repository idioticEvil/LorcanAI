from enum import Enum
from abc import ABC, abstractmethod

class LorcanaCard(ABC):
    """ Represents a basic card in the game that all cards will inherit from """
    def __init__(self, card_id, name, ink_color, cost, classifications, image_url, inkable, expansion, rarity):
        self.card_id = card_id
        self.name = name
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
        super().__init__(card_id=card_id, name=name, ink_color=ink_color, cost=cost, classifications=classifications, image_url=image_url, inkable=inkable, expansion=expansion, rarity=rarity, strength=strength, willpower=willpower, loreVal=loreVal)
        self.version = version
        self.abilities = abilities
        self.keywords = keywords

class LocationCard(AttributedCard):
    """ Subclass to represent location cards """
    def __init__(self, card_id, name, version, ink_color, cost, classifications, image_url, inkable, expansion, rarity, strength, willpower, loreVal, abilities):
        super().__init__(card_id=card_id, name=name, ink_color=ink_color, cost=cost, classifications=classifications, image_url=image_url, inkable=inkable, expansion=expansion, rarity=rarity, strength=strength, willpower=willpower, loreVal=loreVal)
        self.version = version
        self.abilities = abilities

class ActionCard(LorcanaCard):
    """ Subclass to represent action cards """
    def __init__(self, card_id, name, ink_color, cost, classifications, image_url, inkable, expansion, rarity, abilities):
        super().__init__(card_id, name, ink_color, cost, classifications, image_url, inkable, expansion, rarity)
        self.abilities = abilities

class SongCard(LorcanaCard):
    """ Subclass to represent song cards """
    def __init__(self, card_id, name, ink_color, cost, classifications, image_url, inkable, expansion, rarity, abilities):
        super().__init__(card_id, name, ink_color, cost, classifications, image_url, inkable, expansion, rarity)
        self.abilities = abilities

class ItemCard(LorcanaCard):
    """ Subclass to represent item cards """
    def __init__(self, card_id, name, ink_color, cost, classifications, image_url, inkable, expansion, rarity, abilities):
        super().__init__(card_id, name, ink_color, cost, classifications, image_url, inkable, expansion, rarity)
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
    # ... (omitted for brevity)

class InkColor(Enum):
    """ Represents the different ink colors that a card can have """
    # ... (omitted for brevity)