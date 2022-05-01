import sys
import time
from enum import Enum
from pyfiglet import Figlet, FigletString


from state import Stdin
from cards import Deck, Card
from component import Player, Dealer


class VictoryType(Enum):
    PLAYER_WIN = 0
    DEALER_WIN = 1
    DRAW = 2
    NONE = 3


class Status(Enum):
    INIT = 0
    RESTART = 1
    START = 2
    NEXT = 3
    BATTLE = 4
    END = 5
    NONE = 6


class Game:
    def __init__(
        self
    ) -> None:
        self.player_name: str = input("名前を入力してください : ")
        self.player: Player = Player(self.player_name, 5000)
        self.dealer: Dealer = Dealer("Dealer")
        self.deck: Deck = Deck()
        self.round: int = 0
        self.status: Status = Status.NONE
        self.round_bet = 0

    def init(self) -> None:
        self.status = Status.INIT
        self.print("BlackJack!")
        if Stdin.get_response("ゲームを開始しますか？"):
            print("ゲームを開始します。")
            self.start()
        else:
            print("ゲームを終了します。")
            sys.exit()

    def start(self) -> None:
        self.status = Status.START
        self.round += 1

        if self.player.money <= 1000:
            self.player.money = 1000

        print(f"{self.player.name}の所持金は{self.player.money}円です")

        bet = Stdin.input("いくらベットしますか？ : ", num=True)

        while True:
            if bet > self.player.money:
                print("お金が足りません。")
            else:
                self.round_bet = bet
                self.player.money -= bet
                break

        self.draw_entities_new_cards()

        victory_type = self.check_blackjack()

        if (
            victory_type == VictoryType.PLAYER_WIN or
            victory_type == VictoryType.DEALER_WIN or
            victory_type == VictoryType.DRAW
        ):
            self.end(victory_type)
        else:
            self.next()

        self.show_entities_cards()

    def restart(self) -> None:
        self.status = Status.RESTART

        self.player: Player = Player(self.player_name, self.player.money)
        self.dealer: Dealer = Dealer("Dealer")
        self.deck: Deck = Deck()
        self.round_bet = 0

        self.start()

    def next(self) -> None:
        self.status = Status.NEXT

        self.show_entities_cards()
        response: str = Stdin.get_response("HIT or STAND", ["Hit", "Stand"])

        if response:
            self.player_draw()

            victory_type = self.check_player_win()

            if (
                victory_type == VictoryType.PLAYER_WIN or
                victory_type == VictoryType.DEALER_WIN
            ):
                self.end(victory_type)
            else:
                self.next()
        else:
            self.battle()

    def battle(self) -> None:
        self.status = Status.BATTLE

        self.dealer.show_all_cards()

        if (
            self.dealer.is_more_17()   and
            not self.dealer.is_bust()  and
            self.dealer.count_cards() > self.player.count_cards()
        ):
            print("ディーラーの勝利！！")
            self.end(VictoryType.DEALER_WIN)
        else:
            while True:
                self.dealer_draw()

                victory_type = self.check_dealer_win()

                if (
                    victory_type == VictoryType.PLAYER_WIN or
                    victory_type == VictoryType.DEALER_WIN or
                    victory_type == VictoryType.DRAW
                ):
                    self.end(victory_type)
                    break

    def end(self, victory_type) -> None:
        self.status = Status.END

        if victory_type == VictoryType.PLAYER_WIN:
            self.player.money += self.round_bet * 2
        elif victory_type == VictoryType.DRAW:
            self.player.money += self.round_bet

        if Stdin.get_response("もう一度プレイしますか？"):
            self.restart()
        else:
            sys.exit()

    def show_entities_cards(self) -> None:
        self.dealer.show_cards()
        self.player.show_cards()

    def show_entities_all_cards(self) -> None:
        self.dealer.show_all_cards()
        self.player.show_cards()

    def draw_entities_new_cards(self) -> None:
        self.player.set_cards(
            self.deck.first_draw()
        )
        self.dealer.set_cards(
            self.deck.first_draw()
        )

    def player_draw(self) -> None:
        new_card: Card = self.deck.draw()
        self.player.push_card(new_card)

    def dealer_draw(self) -> None:
        new_card: Card = self.deck.draw()
        self.dealer.push_card(new_card)

    def check_blackjack(self) -> VictoryType:
        if self.player.is_21() and self.dealer.is_21():
            self.show_entities_all_cards()

            print("二人共ブラックジャック！！")
            print("引き分けです！")

            return VictoryType.DRAW
        elif self.dealer.is_21():
            self.show_entities_all_cards()

            print("ブラックジャック！")
            print("ディーラーの勝利！！")

            return VictoryType.DEALER_WIN
        elif self.player.is_21():
            self.show_entities_all_cards()

            print("ブラックジャック！")
            print(f"{self.player.name}の勝利！！")

            return VictoryType.PLAYER_WIN
        else:
            return VictoryType.NONE

    def check_player_win(self):
        if self.player.is_bust():
            self.player.show_cards()
            print("バースト！")
            print("ディーラーの勝利！！")

            return VictoryType.DEALER_WIN
        elif self.player.is_21():
            self.player.show_cards()
            print("ブラックジャック！")
            print(f"{self.player.name}の勝利！！")

            return VictoryType.DEALER_WIN
        else:
            return VictoryType.NONE

    def check_dealer_win(self):
        time.sleep(2)
        self.dealer.show_all_cards()
        time.sleep(1)

        if self.dealer.is_bust():
            print("ディーラーがバーストした！")
            print(f"{self.player.name}の勝利！")

            return VictoryType.PLAYER_WIN
        elif self.dealer.is_more_17():
            if self.dealer.count_cards() == self.player.count_cards():
                self.player.show_cards()
                print("引き分けです！")
                self.player.show_cards()

                return VictoryType.DRAW
            elif self.dealer.is_21():
                print("ブラックジャック！")
                print("ディーラーの勝利です！！")
                self.player.show_cards()

                return VictoryType.DEALER_WIN
            elif self.player.count_cards() > self.dealer.count_cards():
                self.player.show_cards()
                print(f"{self.player.name}の勝利！！")
                self.player.count_cards()

                return VictoryType.PLAYER_WIN
            else:
                self.player.show_cards()
                print("ディーラーの勝利です！！")
                self.player.count_cards()

                return VictoryType.DEALER_WIN
        else:
            return VictoryType.NONE



    def print(self, word) -> None:
        figlet: Figlet = Figlet(font='big')
        message: FigletString = figlet.renderText(word)

        print(message)

    def new_deck(self) -> None:
        self.deck = Deck()

    def new_player(self) -> None:
        self.player = Player(
            name=self.player.name
        )
