# 字典推导式

dict = {'a':'A','b':'B','c':'C','d':'C',}
newdict = {value:key for key,value in dict.items()}
# 进行键值和value值的交换，
print(newdict)      #{'A': 'a', 'B': 'b', 'C': 'd'}

'''
通过列表推导式,我们可以直接创造一个列表，
创建不完整的列表,然后根据前面的数推导出完整的列表,叫做生成器.(一边循环,一边计算)

'''

generator = (x * 3 for x in range(20))
print(type (generator))
print(generator)
#通过调用__next__()的方式得到元素
print(generator.__next__())  #调用一次生成一个数值
print(generator.__next__())
print(generator.__next__())

#  只要函数中出现了yield的关键字，说明函数就不是函数了，它就是生成器
#  调用函数，接收调用的结果,得到的结果就是生成器了


def func():
    n = 0 
    while True:
        n += 1
        yield n 

generator = func()
print(next(generator)) #1
print(next(generator)) #2
print(next(generator)) #3 
print(next(generator)) #4

# 斐波那数列
def fib(length):
    a,b = 0,1
    n = 0
    while n < length :
        yield b
        a,b = b,a+b
        n += 1
g = fib(8)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp: ',temp)
        for x in range(temp):
            print('------------->',x)
        print('$$$$$$$$$$$$$$$$$$$')
        i += 1
    return '没有更多的数据'

# send(value): 每次向生成器调用中传值，注意：第一次调用send(None),

ge = gen()
print(ge.send(None))
n1 = ge.send('2')
print('n1:',n1)