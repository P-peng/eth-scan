#！/usr/bin/python3
#coding=utf-8

from web3 import Web3, Account, HTTPProvider
import threading
import logging

from config.EthConfig import EthConfig
from util.EthUtil import EthUtil

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"  # 日期格式
fp = logging.FileHandler('log.txt', encoding='utf-8')
fs = logging.StreamHandler()
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])  # 调用


class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter, main_url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.main_url = main_url

    def run(self):
        main_url = self.main_url;
        logging.info("启动扫描，扫描地址-->>" + main_url)
        logging.info(self.print_thread_group_name())
        w3 = Web3(HTTPProvider(main_url))
        while True:
            private_key = EthUtil.build_64_private_key()
            try:
                account = Account.privateKeyToAccount(private_key)
                balance = w3.eth.getBalance(account.address)
                # logging.info(self.print_thread_group_name() + "," + private_key)
                if balance != 0:
                    logging.info(self.print_thread_group_name() + ",有钱地址-" + account.address + ",私钥-" + private_key)
            except BaseException as e:
                logging.error("异常信息" + str(e))
                continue

    def print_thread_group_name(self):
        return "线程信息,thread.counter-" + str(self.counter) + ",thread.threadID-" + str(self.threadID) + ",thread.name-" + str(self.name)


if __name__ == '__main__':
    # 一个url启动几条线程
    count = 2
    # 线程计数器
    number = 0
    for i in range(len(EthConfig.keys)):
        key = EthConfig.get_key();
        for j in range(count):
            number = number + 1
            thread = MyThread(number, "Thread-" + str(number), number, key)
            thread.start()
            logging.info("成功启动，线程数" + str(number))
