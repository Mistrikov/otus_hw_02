from random import randint

class Card:
    def __init__(self):
        self.numbers = self._gen()
        #self._numbers = self._gen()
        #self._select_numbers = [5, 4, 10, 22, 24, 43]

    def _gen(self)-> list:
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

    '''def show1(self):
        for i in range(3):
            for j in range(9):
                print("**" if self._numbers[i][j] in self._select_numbers else "  " if self._numbers[i][j]==0 else " "*(2-len(str(self._numbers[i][j])))+str(self._numbers[i][j]), end="  ")
            print()'''

    '''def show(self):
        for row in self._numbers:
            for num in row:
                print("**" if num in self._select_numbers else "  " if num==0 else " "*(2-len(str(num)))+str(num), end="  ")
            print()'''

    '''def add_select_number(self, number):
        self._select_numbers.append(number)'''

