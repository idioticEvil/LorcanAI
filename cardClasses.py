from abc import ABC, abstractmethod
from typing import List
import cardEnums

""" 
TODO:
- Action & Song Cards implement abilities differently than Character & Location Cards, and have no name,
so implement a way to handle that
- Implement the print_info() method for all card types
- Implement a basic print_info method for the LorcanaCard class for common information, 
and use something like a tuple list to control print order
- Implement the abilities and keywords for all card types
- Implement print functions for abilities and keywords that card print_info() can call
"""

class CardAbility:
    """ Represents an ability that a card can have """
    def __init__(self, name: str, description: str, exertion: bool):
        self.name = name
        self.description = description
        self.exertion = exertion

class CardKeyword:
    """ Represents a keyword that a card can have """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class LorcanaCard(ABC):
    """ Represents a basic card in the game that all cards will inherit from """
    def __init__(self, card_id: int, name: str, ink_color: cardEnums.InkColor, 
                 cost: int, classifications: List[cardEnums.CardClassification], 
                 image_url: str, inkable: bool, expansion: cardEnums.CardExpansion, 
                 rarity: cardEnums.CardRarity):
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
    def print_info(self):
        pass

class AttributedCard(LorcanaCard, ABC):
    """ Subclass to represent cards with attributes """
    @abstractmethod
    def __init__(self, strength: int, willpower: int, loreVal: int, **kwargs):  
        super().__init__(**kwargs)
        self.strength = strength
        self.willpower = willpower
        self.loreVal = loreVal

class CharacterCard(AttributedCard):
    """ Subclass to represent character cards """
    def __init__(self, card_id: int, name: str, version: str, ink_color: cardEnums.InkColor, 
                 cost: int, classifications: List[cardEnums.CardClassification], 
                 image_url: str, inkable: bool, expansion: cardEnums.CardExpansion, 
                 rarity: cardEnums.CardRarity, strength: int, willpower: int, loreVal: int, 
                 abilities, keywords):
        super().__init__(card_id=card_id, name=name, ink_color=ink_color, cost=cost, 
                         classifications=classifications, image_url=image_url, inkable=inkable, 
                         expansion=expansion, rarity=rarity, strength=strength, willpower=willpower, 
                         loreVal=loreVal)
        self.version = version
        self.abilities = abilities
        self.keywords = keywords

        def print_info(self):
            print("Card Name: " + self.name)
            print("Card Version: " + self.version)
            print("Ink Color: " + self.ink_color.value)
            print("Inkwell: " + str(self.inkable))
            print("Cost: " + str(self.cost))
            print("Strength: " + str(self.strength))
            print("Willpower: " + str(self.willpower))
            print("Lore Value: " + str(self.loreVal))
            print("Classifications: " + ', '.join([classification.value for classification in self.classifications]))
            print("Expansion: " + self.expansion.value)
            print("Rarity: " + self.rarity.value)
            # TODO: Implement abilities and keywords

class LocationCard(AttributedCard):
    """ Subclass to represent location cards """
    def __init__(self, card_id: int, name: str, version: str, ink_color: cardEnums.InkColor, 
                 cost: int, classifications: List[cardEnums.CardClassification], 
                 image_url: str, inkable: bool, expansion: cardEnums.CardExpansion, 
                 rarity: cardEnums.CardRarity, strength: int, willpower: int, loreVal: int, 
                 abilities):
        super().__init__(card_id=card_id, name=name, ink_color=ink_color, cost=cost, 
                         classifications=classifications, image_url=image_url, inkable=inkable, 
                         expansion=expansion, rarity=rarity, strength=strength, willpower=willpower, 
                         loreVal=loreVal)
        self.version = version
        self.abilities = abilities

        def print_info(self):
            print("Card Name: " + self.name)
            print("Card Version: " + self.version)
            print("Ink Color: " + self.ink_color.value)
            print("Inkwell: " + str(self.inkable))
            print("Cost: " + str(self.cost))
            print("Strength: " + str(self.strength))
            print("Willpower: " + str(self.willpower))
            print("Lore Value: " + str(self.loreVal))
            print("Classifications: " + ', '.join([classification.value for classification in self.classifications]))
            print("Expansion: " + self.expansion.value)
            print("Rarity: " + self.rarity.value)
            # TODO: Implement abilities

class ActionCard(LorcanaCard):
    """ Subclass to represent action cards """
    def __init__(self, card_id: int, name: str, ink_color: cardEnums.InkColor, cost: int, 
                 classifications: List[cardEnums.CardClassification], image_url: str, 
                 inkable: bool, expansion: cardEnums.CardExpansion, 
                 rarity: cardEnums.CardRarity, abilities):
        super().__init__(card_id, name, ink_color, cost, classifications, image_url, 
                         inkable, expansion, rarity)
        self.abilities = abilities

        def print_info(self):
            print("Card Name: " + self.name)
            print("Ink Color: " + self.ink_color.value)
            print("Inkwell: " + str(self.inkable))
            print("Cost: " + str(self.cost))
            print("Classifications: " + ', '.join([classification.value for classification in self.classifications]))
            print("Expansion: " + self.expansion.value)
            print("Rarity: " + self.rarity.value)
            # TODO: Implement abilities

class SongCard(LorcanaCard):
    """ Subclass to represent song cards """
    def __init__(self, card_id: int, name: str, ink_color: cardEnums.InkColor, cost: int, 
                 classifications: List[cardEnums.CardClassification], image_url: str, 
                 inkable: bool, expansion: cardEnums.CardExpansion, 
                 rarity: cardEnums.CardRarity, abilities):
        super().__init__(card_id, name, ink_color, cost, classifications, image_url, 
                         inkable, expansion, rarity)
        self.abilities = abilities

        def print_info(self):
            print("Card Name: " + self.name)
            print("Ink Color: " + self.ink_color.value)
            print("Inkwell: " + str(self.inkable))
            print("Cost: " + str(self.cost))
            print("Classifications: " + ', '.join([classification.value for classification in self.classifications]))
            print("Expansion: " + self.expansion.value)
            print("Rarity: " + self.rarity.value)
            # TODO: Implement abilities

class ItemCard(LorcanaCard):
    """ Subclass to represent item cards """
    def __init__(self, card_id: int, name: str, ink_color: cardEnums.InkColor, 
                 cost: int, classifications: List[cardEnums.CardClassification], 
                 image_url: str, inkable: bool, expansion: cardEnums.CardRarity, 
                 rarity: cardEnums.CardRarity, abilities):
        super().__init__(card_id, name, ink_color, cost, classifications, image_url, 
                         inkable, expansion, rarity)
        self.abilities = abilities

        def print_info(self):
            print("Card Name: " + self.name)
            print("Ink Color: " + self.ink_color.value)
            print("Inkwell: " + str(self.inkable))
            print("Cost: " + str(self.cost))
            print("Classifications: " + ', '.join([classification.value for classification in self.classifications]))
            print("Expansion: " + self.expansion.value)
            print("Rarity: " + self.rarity.value)
            # TODO: Implement abilities