'''
*args   加*号就会默认把这些都放在同一个列表中,在函数中就是放在元组中
**kwargs :可变的参数,传入键和value值, key word args 关键字参数,才能封装成字典


'''
a,b,*c = 1,2,3,4,5   #装包，把后面的三个值放到c中
print(c)  #[3, 4, 5]

def get_sum(*args):
    s = 0
    for i in args:
        s += i 
    print(s)

get_sum(2,3,4,5)    #求得总和为14


list_1 = [21,32,32,5,2]
get_sum(*list_1)            #将列表传入求和函数中，就可实现拆包和装包，进行求和


def show_book(**kwargs):
    print(kwargs)

show_book(bookname = '西游记',author = '吴承恩')  #{'bookname': '西游记', 'author': '吴承恩'}



# 用return来接收函数内的值，在外面重新调用
def get_sum(*args):
    total = 0
    for i in args:
        total += i 
    print("内部",total)
    return total

total = get_sum(1,2,3)  #只要函数有返回值，就必须在外面用一个新的参数去接收这个值
print(total)
ts = 1 + total
print(ts)

# return 后面超过一个值，就会用元组封装起来，或者用两个值去接收元组中的数

def get_maxmin(list1):
    for i in range(0,len(list1)-1):
        for j in range(0,len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    min = list1[0]
    max = list1[-1]
    return min ,max
list2 = [23,52,54,32,91,34,51]
min,max = get_maxmin(list2)
print(min,max)                  #  23 91

# 可变与不可变类型
# 不可变就是值改变了，地址也就发生改变
# 不可变类型：int str float bool tuple(元组)
# 可变就是内容变了，但是地址没有发生改变
# 可变类型：list  dict  set 
