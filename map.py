# -*- coding: utf-8 -*-

class Map(object):

    def __init__(self, **kargs):
        # 如果使用 self.data会访问 __getattr__ 函数
        # 所以在__init__里不要使用 self.xxx 来初始化
        super(Map, self).__setattr__('data', kargs)

    def __setattr__(self, k, v):
        self.data[k] = v

    def __getattr__(self, k):
        ret = self.data.get(k, None)
        if not ret:
            return None
        if isinstance(ret, int):
            return ret
        if isinstance(ret, str):
            return ret
        if isinstance(ret, list):
            for index, r in enumerate(ret):
                if isinstance(r, dict):
                    r = Map(**r)
                    ret[index] = r
            return ret
        if isinstance(ret, dict):
            r = Map(**ret)
            self.data[k] = r
            return r
        return ret


class ClassA:
    def __init__(self):
        self.name = "inmove"


if __name__ == '__main__':
    obj = Map()
    obj.name = "inmove"
    obj.user = {"name": "inmove", "age": 30, "job": {"address": 'shenZhen', "content": "programmer", "obj": ClassA()}}
    print(obj.user.job.obj)
