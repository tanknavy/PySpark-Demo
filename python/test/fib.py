def fib_loop_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b #解构赋值，scala,java中不支持
    return a


def fib_loop_while(n):
    a, b = 1, 1
    while n > 0:
        a, b = b, a + b
    n -= 1
    return a


for i in range(20):
    print(fib_loop_for(i), end=' ')
