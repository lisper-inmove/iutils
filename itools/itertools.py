# -*- coding: utf-8 -*-


from itools import exceptions


class Itertools:

    def __init__(self):
        pass

    def groupby(self, lst, fn):
        if not isinstance(lst, list):
            raise exceptions.NotListException("参数 lst 必须是列表")
        tmp = {}
        for member in lst:
            ret = fn(member)
            tmp_lst = tmp.get(ret, [])
            tmp_lst.append(member)
            tmp.update({ret: tmp_lst})
        return tmp
