
from math import sqrt, pow, fabs

// calculates population standard deviation

class SD:
    def __init__(self):
        pass

    def mean(self, a_list):
        return sum(a_list) / len(a_list)

    def calc_sd(self):
        a_list = list(map(float, input("Enter your list of numbers > ").split()))
        average = self.mean(a_list)
        absolute_values = [abs(value - average) for value in a_list]
        squared_values = [pow(value, 2) for value in absolute_values]
        sd = sqrt( sum(squared_values) / len(a_list))
        print("standard deviation: {}".format(sd))
