import asyncio

@asyncio.coroutine
def hello2():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1) #等待一秒，返回r=None
    print('Hello: ' + str(r))
    print("Hello again!")

#新版
async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1) # 等待一秒
    print('Hello: ' + str(r))
    print("Hello again!")
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()