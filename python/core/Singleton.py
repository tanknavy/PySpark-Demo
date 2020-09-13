import threading
import time
import logging
import random

# 单例模式
class Singleton(object):
    __instance=None # 私有类属性，__代表私有，放到cls下面表示类的属性
    __lock=threading.Lock()

    def __new__(cls,name,age): #重写new方法
        if not cls.__instance: #如果没有
            try:
                logging.debug('Acquired a lock')
                cls.__lock.acquire()
                if not cls.__instance:
                    cls.__instance = object.__new__(cls)  # 调用父类的new方法创建此类的实例
                print(id(cls))
                print(id(cls.__instance))

            finally:
                logging.debug('Released a lock')
                cls.__lock.release()

        return cls.__instance # 特别主要要加cls,不加的话就不是指向同一个对象了

    def __init__(self, name, age):
        self.name=name
        self.age=age


a=Singleton("bob",19)
b=Singleton("carl",29)

print(id(a))
print(id(a)==id(b))
print(a.name)
print(a.age)
print(b.name)
print(b.age)

print("-------------------------------------------")
#工厂模式：常用的实例化对象模式，使用工厂方法代替new操作
# 简单工厂模式


# 抽象工厂模式
class Woker(object):
    def __init__(self,name):
        self.name=name
    def work(self,type_axe):
        print("%s开始工作啦"%(self.name))
        # axe=StoneAxe()
        # axe.cut_tree()
        axe=Factory.create_axe(type_axe) #工厂类
        axe.cut_tree()



class Axe(object):
    def cut_tree(self):
        print("砍树")

class StoneAxe(object):
    def cut_tree(self):
        print("石斧砍树")

class SteelAxe(object):
    def cut_tree(self):
        print("铁斧头砍树")

# 创建简单工厂类
class Factory(object):
    @classmethod
    def create_axe(cls,type_axe):
        if type_axe=="stone":
            return StoneAxe()
        elif type_axe=="steel":
            return SteelAxe()
        else:
            print("参数不对")



w=Woker("bob")
w.work("steel")