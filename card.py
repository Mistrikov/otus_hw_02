from random import randint

class Card:
    def __init__(self):
        self._numbers = self._gen()

    def _gen(self):
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
 
        for i in range(3):
            numbers[i] = ["  " if q==0 else str(q) if q>9 else "0"+str(q) for q in numbers[i] ]

        return numbers

    def show(self):
        for i in range(3):
            print(" ".join(self._numbers[i]))      

