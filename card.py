from random import randint

class Card:
    def __init__(self):
        # для быстрой проверки, можно зафиксировать карточки для обоих игроков
        self.numbers = self._gen()
        #self.numbers = [[0, 13, 0, 34, 43, 0, 62, 77, 0], [0, 0, 0, 35, 0, 54, 64, 78, 86], [4, 14, 28, 0, 44, 0, 0, 79, 0]]

    def _gen(self)-> list:
        # подбор чисел для карточки. три ряда по 5 чисел, остальные 4 числа в ряду заполняются нулями
        # в каждом столбце числа идут по возрастанию
        # не самый удобный способ
        numbers = []
        counts = [0]*9
        count_in_row = [0]*9
        for i in range(3):
            row = [0]*9
            while sum(1 for num in row if num > 0)<5:
                a = randint(1, 90)
                if not any(a in q for q in numbers) and a!=90 and count_in_row[(a)//10 ]<3:
                    if a!=90:
                        row[(a)//10] = a
                        count_in_row[(a)//10 ] += 1
                if not any(a in q for q in numbers) and a==90 and count_in_row[(a-1)//10 ]<3:
                        row[(a-1)//10] = a
                        count_in_row[(a-1)//10 ] += 1
            numbers.append(row)

        for j in range(9):
            a = []
            for i in range(3):
                if numbers[i][j]>0:
                    a.append(numbers[i][j])
            a.sort()
            q = 0
            for i in range(3):
                if numbers[i][j]>0:
                    numbers[i][j] = a[q]
                    q+=1

        return numbers