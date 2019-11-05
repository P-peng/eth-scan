#！/usr/bin/python3
#coding=utf-8


class EthConfig(object):
    keys = {
        # 894194651@qq.com key
        # "https://mainnet.infura.io/v3/eeb4395af38744ce9129d8975781d34e": 1,
        # "https://mainnet.infura.io/v3/baba69547b5049d687d12db75d58431a": 1,
        # "https://mainnet.infura.io/v3/e674ba0fd9dd4a78b50ed333a3198c64": 1,

        # 3392612933@qq.com
        "https://mainnet.infura.io/v3/1b87fa0b1a2d4147b0df388dafea4635": 1,
        "https://mainnet.infura.io/v3/ce55a2288521418389de018b33afb6c9": 1,
        "https://mainnet.infura.io/v3/24b1f31e0ab8475a961d18ceaf4572c7": 1
    }

    @staticmethod
    def get_key():
        keys = EthConfig.keys
        for key in EthConfig.keys:
            if keys.get(key) == 1:
                keys[key] = 0
                return key
        return None
