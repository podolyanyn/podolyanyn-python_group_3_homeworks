class Mathematician:
    def __init__(self, numbers):
        self.numbers = numbers

    def square_nums(self):
        print(list(map(lambda x:x**2, self.numbers)))
        return list(map(lambda x:x**2, self.numbers))

    def remove_positives(self):
        numbers = self.numbers
        pos =  [x for x in numbers if x <= 0]
        print(pos)
        return pos

    def filter_leaps(self):
        numbers = self.numbers
        lp =  [y for y in numbers if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]
        print(lp)
        return lp


M1 = Mathematician([5 , -5, -9, 8, -9])
M1.square_nums()
M1.remove_positives()
M3 = Mathematician([1985, 2005, 1895, 2000])
M3.filter_leaps()

#   Або без __init__
# class Mathematician:
#
#     def square_nums(self, numbers):
#         return [x ** 2 for x in numbers]
#
#     def remove_positives(self, numbers):
#         return [x for x in numbers if x <= 0]
#
#     def filter_leaps(self, years):
#         return [y for y in years if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]
