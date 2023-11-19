from random import choice

class Meshok:
    def __init__(self):
        self._barrels = [i for i in range(1, 91)]

    def get_new(self)-> int:
        if len(self._barrels)>0:
            q = choice(self._barrels)
            self._barrels.remove(q)
            print(f'Новый бочонок: {q} (осталось {len(self._barrels)})')
            return q
        else:
            print(f'Бочонки закончились')
            return False