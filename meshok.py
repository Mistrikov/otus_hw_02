from random import choice

class Meshok:
    def __init__(self):
        self._new = [i for i in range(1, 91)]

    def get_new(self)-> int:
        if len(self._new)>0:
            q = choice(self._new)
            self._new.remove(q)
            print(f'Новый бочонок: {q} (осталось {len(self._new)})')
            return q
        else:
            print(f'Бочонки закончились')
            return False