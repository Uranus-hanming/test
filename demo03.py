# import multiprocessing
# import time
#
#
# def fun():
#     print("开始一个进程")
#     time.sleep(5)
#
#
# p = multiprocessing.Process(target=fun)
# p.start()
# time.sleep(2)
# p.join()

# from multiprocessing import Process
# from time import sleep
#
#
# def work(second, name):
#     for i in range(3):
#         sleep(second)
#         print("i am %s" % name)
#
#
# p = Process(target=work, args=(2,), kwargs={"name": "tom"})
# p.start()
# p.join()


from multiprocessing import Process
from time import sleep
import os


def func01():
    sleep(2)
    print("吃饭")
    print(os.getppid(), "--", os.getpid())


def func02():
    sleep(3)
    print("睡觉")
    print(os.getppid(), "--", os.getpid())


def func03():
    sleep(4)
    print("玩耍")
    print(os.getppid(), "--", os.getpid())


list = []
for item in [func01, func02, func03]:
    p = Process(target=item)
    list.append(p)
    p.start()
for i in list:
    i.join()
