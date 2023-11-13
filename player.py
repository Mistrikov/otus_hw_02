from card import Card

class Player:
    def __init__(self, name, human: bool):
        self.name = name
        self.isHuman = human
        self.card = Card()
        self.isWin = False
        self.isLoss = False
        self._select_numbers = []

    def show_card(self):
        print(f'Карточка игрока: {self.name}\n' + '-'*34)
        for row in self.card.numbers:
            for num in row:
                print("**" if num in self._select_numbers else "  " if num==0 else " "*(2-len(str(num)))+str(num), end="  ")
            print()
        print('-'*34)

    def _check_step_human(self, number):
        if input(f'{self.name}, зачеркнуть число? (y/n) ') == 'y':
            return any(number in x for x in self.card.numbers)
        else:
            return not any(number in x for x in self.card.numbers)

    def next_step(self, number):
        if any(number in x for x in self.card.numbers):
            self._select_numbers.append(number)
            self.isWin = len(self._select_numbers) == 15

        if self.isHuman:
            # Человек
            self.isLoss = not self._check_step_human(number)

