# -*- coding: utf-8 -*-


from itools.itertools import Itertools

lst = [1, 2, 3, 4]
groupby_lst = Itertools().groupby(lst, fn=lambda x: x % 2)
print(groupby_lst)
