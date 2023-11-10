from card import Card

class Player:
    def __init__(self, name, human: bool):
        self.name = name
        self.isHuman = human
        self.card = Card()
        self.isWin = False
        self._select_numbers = []

    def show_card(self):
        print(f'Карточка игрока: {self.name}\n' + '-'*34)
        count = 0
        for row in self.card.numbers:
            for num in row:
                print("**" if num in self._select_numbers else "  " if num==0 else " "*(2-len(str(num)))+str(num), end="  ")
                if num in self._select_numbers:
                    count += 1
            print()
        print('-'*34)
        if count == 15:
            self.isWin = True

    def add_select_number(self, number):
        self._select_numbers.append(number)

    def next_step(self, number):
        if self.isHuman:
            # Человек
            if input('Зачеркнуть число? (y/n)') == 'y':
                # человек - вычеркивать число в карточке
                if number in self.card.numbers:
                    self._select_numbers.append(number)
                    return True
                else:
                    return False
            else:
                # человек - не вычеркивать число карточке
                if number not in self.card.numbers:
                    self._select_numbers.append(number)
                    return False
                else:
                    return True
        else:
            # Компьютер
            self._select_numbers.append(number)
            return True