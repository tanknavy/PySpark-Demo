#高阶函数，scala/javascript里面的闭包，python的装饰器

#需求，任何执行的函数答应出当前函数名

#Decorator
def log(func):
    def wrapper(*args, **kw):
        print("current function: " + func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def square(x): #被装饰的函数
    return x * x

res = square(2)
print("result:", res)


def highFunc(x): #高阶函数，闭包closure
    return lambda y : x * y

#scala中基本类型都是值传递，python这里匿名函数是引用，具体函数是值传递，js中都是引用传递！
def testClousure():
    a1 = []
    a2 = []
    for i in range(3):
        #特别注意，两个函数功能一样，单保存变量不一样
        # 使用外部函数时，是值传递，使用lambda匿名函数时，是引用传递
        a1.append(lambda x: x * i) #这里两种方式不一样的结果
        a2.append(highFunc(i))  # i是值传递，只有javascript是值引用

    for j in range(3):
        print("Use lambda function:", a1[j](5)) # 相同
        # print("Use outer function: ", a1[j](5)) #不同

    print("---------------function vs lamdba-----------------------")

    for k in range(3):
        print("Use outer function: ", a2[k](5))
        #print("Use lambda function:", a2[k](5))

testClousure()