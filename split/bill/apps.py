from django.apps import AppConfig
from statistics import mean


class BillConfig(AppConfig):
    name = 'bill'


def split_the_bill(x):
    keys = list(x.values())
    keys2 = list(x.keys())
    average = mean(keys)
    keys3 = [(round(i-average, 1)) for i in keys]
    ans = dict( zip( keys2, keys3))
    return ans

