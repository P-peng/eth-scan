#！/usr/bin/python3
#coding=utf-8

from web3 import Web3, Account, HTTPProvider
import logging
import random

main_url = 'https://mainnet.infura.io/v3/eeb4395af38744ce9129d8975781d34e'
# main_url = 'https://mainnet.infura.io/v3/baba69547b5049d687d12db75d58431a'
# main_url = 'https://mainnet.infura.io/v3/e674ba0fd9dd4a78b50ed333a3198c64'
w3 = Web3(HTTPProvider(main_url))
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
fp = logging.FileHandler('log.txt', encoding='utf-8')
fs = logging.StreamHandler()
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def main():
    i = 1
    priv = '2defac83d19dfe04610864da99cec58fdcf11af07178cfacbf30c02d6ac57e46'
    account = Account.privateKeyToAccount(priv)
    print(account.address)
    try:
        balance = w3.eth.getBalance(account.address)
        if balance != 0:
            logging.info("有钱地址-" + account.address + ",私钥-" + priv)
            print(balance)
    except BaseException as e:
        print(str(e))


def random_find():
    logging.info("启动扫描，扫描地址-->>" + main_url)
    while True:
        private_key = build_64_private_key()
        try:
            account = Account.privateKeyToAccount(private_key)
            balance = w3.eth.getBalance(account.address)
            if balance != 0:
                logging.info("有钱地址-" + account.address + ",私钥-" + private_key)
                print(private_key)
                print(balance)
        except BaseException as e:
            logging.error("异常信息" + str(e))
            continue


def build_64_private_key():
    private_key = ""
    while len(private_key) < 64:
        private_key = private_key + arr[get_random()]
    return private_key


def get_random():
    return random.randint(0, 15)


if __name__ == '__main__':
    # random_find()
    main()
