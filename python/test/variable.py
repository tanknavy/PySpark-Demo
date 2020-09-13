#python和java类似，对primitive类型是value传递，对于list,map,set和其它类型是reference传递
#Golang中默认都是value传递，除了slice和map,所以经常使用*指针

def func(num):
    print("variable in func:", num)
    num += 10
    print("variable in func:", num)

num = 3
print("variable in main:", num)
func(3)
print("variable in main:", num)#不同

a = 5
b = a #值传递
print("current b is :", b)
a = 15
print("current b is :", b) #不同

aa = [1,2,3]
bb = aa
print("current bb is :", bb)
aa[0] = 11
print("new aa is :", aa)
print("new bb is :", bb) #相同


