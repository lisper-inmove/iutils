# -*- coding: utf-8 -*-

"""
Filename: obj_utils.py
Date: 2020-07-21 11:57:03
Title: obj_utils
"""


class ObjUtils:
    def __init__(self, **kargs):
        self.__dict__ = {}
        self.__dict__.update(**kargs)

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__.get(name)
        return None

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            del self.__dict__[name]


if __name__ == '__main__':
    obj = ObjUtils(name="inmove", age=21)
    print(obj.name)
    print(obj.age)
    obj.work = "programmer"
    print(obj.work)
    del obj.work
    print(obj.work)
