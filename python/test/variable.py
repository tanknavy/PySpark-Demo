#python和java类似，对primitive类型是value传递，对于list,map,set和其它类型是reference传递
#Golang中默认都是value传递，除了slice和map,所以经常使用*指针

def func(num): #num是值传递
    print("variable in func:", num)
    num += 10
    print("variable in func:", num)

num = 3
print("variable in main:", num)
func(3)
print("variable in main:", num)#不同

a = 5 #数字类型
b = a #值传递
print("number current b is :", b)
a = 15
print("number current b is :", b) #不同

sa = "hello" #字符串类型
sb = sa #字符串是引用类型
print(sa == sb)
print("string current sb is :", sb)
sa = "world"
print(sa == sb)
print("string current sb is :", sb) #字符串，相同！！！
#sa[0] = "H" #字符串不可变


aa = [1,2,3] #list列表类型
bb = aa
print("current bb is :", bb)
aa[0] = 11
print("list new aa is :", aa)
print("list new bb is :", bb) #相同


