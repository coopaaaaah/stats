
from math import floor

class IQR:
    def __init__(self):
        pass


    def average(self, a, b):
        return (a + b) / 2

    def find_median_location_of_list(self, a_list):
        if ( len(a_list) % 2 == 0 ):
            return None
        else:
            return floor(len(a_list)/2)

    def split_list(self, a_list, index):
        if ( len(a_list) % 2 == 0 ):
            return a_list[:index], a_list[index:]
        else:
            return a_list[:index], a_list[index + 1:]

    def calc_iqr(self):
        a_list = list(map(float, input("Enter your list of numbers > ").split()))
        median_location = self.find_median_location_of_list(a_list)

        if (median_location is None):
            subset_a, subset_b = self.split_list(a_list, int(len(a_list)/2))
        else:
            subset_a, subset_b = self.split_list(a_list, median_location)

        median_location_of_subset_a, median_location_of_subset_b = self.find_median_location_of_list(subset_a), self.find_median_location_of_list(subset_b)

        if (median_location_of_subset_a is None or median_location_of_subset_b is None):
            superset_a1, superset_a2 = self.split_list(subset_a, int(len(subset_a) / 2))
            superset_b1, superset_b2 = self.split_list(subset_b, int(len(subset_b) / 2))
            q1_median = (superset_a1[int(len(superset_a1) - 1)] + superset_a2[0]) / 2
            q3_median = (superset_b1[int(len(superset_b1) - 1)] + superset_b2[0]) / 2
        else:
            q1_median = subset_a[median_location_of_subset_a]
            q3_median = subset_b[median_location_of_subset_b]

        iqr = q3_median - q1_median
        print("ipr: {}".format(iqr))
