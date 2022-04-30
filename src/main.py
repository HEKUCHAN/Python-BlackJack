from cards import Deck

def main():
    deck = Deck()
    for card in deck.cards:
        print(card)
    card = deck.draw()
    print(str(card))

if __name__ == "__main__":
    main()
