#！/usr/bin/python3
#coding=utf-8
import random

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


class EthUtil(object):

    @staticmethod
    def build_64_private_key():
        private_key = ""
        while len(private_key) < 64:
            private_key = private_key + arr[EthUtil.get_random()]
        return private_key

    @staticmethod
    def get_random():
        return random.randint(0, 15)
