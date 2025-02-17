# -*- coding: utf-8 -*-

# Домашнее задание по теме "Блокировки и обработка ошибок"

import threading
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = randint(50, 500)
            self.balance += amount
            print(f'Пополнение: {amount}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)
        # if self.lock.locked():  # гарантирование завершения, т.е. снятие
        #     self.lock.release() # блокировки после завершения цикла

    def take(self):
        for _ in range(100):
            amount = randint(50, 500)
            print(f'Запрос на {amount}')
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
        # if self.lock.locked():  # гарантирование завершения, т.е. снятие
        #     self.lock.release() # блокировки после завершения цикла


bk = Bank()

deposit_thread = threading.Thread(target=Bank.deposit, args=(bk,))
take_thread = threading.Thread(target=Bank.take, args=(bk,))

deposit_thread.start()
take_thread.start()

deposit_thread.join()
take_thread.join()

print(f'Итоговый баланс: {bk.balance}')
