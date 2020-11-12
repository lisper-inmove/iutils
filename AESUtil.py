# -*- coding: utf-8 -*-

import time
import base64
from Crypto.Cipher import AES


class Prpcrypt():
    def __init__(self, secret):
        # key值（密码）
        self.key = secret.encode("utf-8")
        # vi偏移量
        self.iv = secret.encode("utf-8")
        self.mode = AES.MODE_CBC
        self.BS = AES.block_size
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def encrypt(self, text):
        text = self.pad(text).encode("utf-8")
        cryptor = AES.new(self.key, self.mode, self.iv)
        ciphertext = cryptor.encrypt(text)
        return base64.b64encode(bytes(ciphertext))

    def decrypt(self, text):
        text = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(text)
        return self.unpad(bytes.decode(plain_text).rstrip('\0'))    # 解密字节？？？

    def padding_to_16(self, value):
        pass


if __name__ == '__main__':
    pc = Prpcrypt("aaaaaaaaaaaaaaaa")  # 初始化密钥 和 iv
    # text='access&a494fcbc-9aa1-4718-bd7d-a90d01211d97&0&2&'
    text = 'access&a494fcbc-9aa1-4718-bd7d-a90d01211d97&0&1&'
    # text='access&a494fcbc-9aa1-4718-bd7d-a90d01211d97&1&1&'
    # text='access&a494fcbc-9aa1-4718-bd7d-a90d01211d97&1&2&'
    # text='update&a494fcbc-9aa1-4718-bd7d-a90d01211d97&0&2&'
    # text='update&a494fcbc-9aa1-4718-bd7d-a90d01211d98&0&2&'
    # text='logout&'
    e = pc.encrypt(text + str(int(time.time() / 10)))  # 加密
    d = pc.decrypt(e)  # 解密
    print("加密: {}".format(e.decode("utf-8")))
    print("解密: {}".format(d))
    print("长度: {}".format(len(d)))
