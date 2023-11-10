from card import Card

class Player:
    def __init__(self, name, human: bool):
        self.card = Card()
        self.name = name
        self.isHuman = human
        self._select_numbers = [5, 4, 10, 22, 24, 43]

    def show_card(self):
        print(f'Карточка игрока: {self.name}\n' + '-'*34)
        for row in self.card.numbers:
            for num in row:
                print("**" if num in self._select_numbers else "  " if num==0 else " "*(2-len(str(num)))+str(num), end="  ")
            print()
        print('-'*34)

    def add_select_number(self, number):
        self._select_numbers.append(number)