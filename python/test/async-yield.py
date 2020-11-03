# python的协程(单线程异步io)coroutine是通过yield实现的
# generator每次每调用到yield时返回结果，到下一次调用时，再从上次yield下一个语句resume开始往后执行
def consumer():
    #r = ''
    r = 'init...' #测试
    while True:
        #关键,yield r返回r给调用者，同时在调用者send(n)也接受传过来的值
        # nn = yield ...这里yield接受值nn
        nn = yield r #通过yield拿到caller传过来的结果，同时也通过yield返回一个结果
        print('[CONSUMER]-0: ' + str(nn)) #测试，从caller接受来的n
        if not nn:
            return
        print('[CONSUMER]-1: Consuming %s...' % nn)
        r =  '200 OK ' + str(nn)

def produce(c):
    # TypeError: can't send non-None value to a just-started generator
    # 刚启动的gnerator,第一要发送None
    #c.send(None) #为啥先要发送None,因为相当于初始化generator,不然会报TypeError
    re = c.send(None) #为啥先要发送None,因为相当于初始化generator,不然会报TypeError
    print('[PRODUCER] ' + str(re)) #测试
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER]-0: Producing %s...' % n)
        r = c.send(n) #generator有方法send()和close()
        print('[PRODUCER]-1: Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)