
class Animal(object):
    def __init__(self,id):
        self.id = id

class Dog(Animal):

    # __xx__模块函数
    # cls代表要实例化的类，此参数在实例化是由python解释器自动提供
    def __new__(cls, *args, **kwargs): # 创建对象调用的方式
        print("new创建对象")

        #return super.__new__(cls)
        return super().__new__(cls)
        #return object.__new__(cls) #必须有返回值，父类的new方法

    # self代表实例化的对象，在对象被创建后立刻被默哀人调用
    def __init__(self, name, age): #不是构造器，只是完成对象的初始化操作
        print("init调用初始化对象的属性")
        super().__init__(1)
        self.name = name
        self.age = age

    def __str__(self):

        return str(self.id) + "," +self.name + "," +str(self.age)

    def __del__(self):
        print("对象被删除")

    def run(self):
        print("running")

dog=Dog("carl",2)
print(id(dog)) #id输出内存地址
dog2=Dog("gougou",3)
print(id(dog2)) #id输出地址
dog.run()

print(dog)
print(dog2)
del dog2
print(Dog.__mro__)

print("-----------")

class Person(object):
    name="alex" #类属性,类似java的静态属性
    def __init__(self,name,age):
        self.name=name #实例属性
        self.age=age

    @classmethod #相当于java的静态方法，一般用于工厂模式创建对象
    def test(cls):
        print("类方法")

    def test2(self):
        print("实例方法")

    @staticmethod
    def test3(): #静态方法无需参数，一版是工具方法
        print("静态方法")

p=Person("bob",28)
print(p.name)
print(Person.name)
Person.name="wangwu"
print(Person.name)

p.test()
p.test2()
p.test3()
Person.test()
Person.test2(p)
Person.test3()

print("-----------")

class Car(object):
    name="bmw"

c=Car()
print(c.name)
print(Car.name)
c.name="benz"
print(c.name)
print(Car.name)
Car.name="luxes"
print(c.name)
print(Car.name)
