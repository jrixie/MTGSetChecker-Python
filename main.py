from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

def main():
    card = Card.find(42)
    print(card.name)


if __name__ == "__main__":
    main()