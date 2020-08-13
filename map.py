# -*- coding: utf-8 -*-


class Map(object):

    def __init__(self, **kargs):
        # 如果使用 self.data会访问 __getattr__ 函数
        # 所以在__init__里不要使用 self.xxx 来初始化
        super(Map, self).__setattr__('data', kargs)

    def __setattr__(self, k, v):
        self.data[k] = v

    def __getattr__(self, k):
        return self.data.get(k)


if __name__ == '__main__':
    obj = Map()
    obj.name = "inmove"
    print(obj.name)
