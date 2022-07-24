# 可迭代对象
# 生成器、元组、字典、集合、字符串、集合
# 可迭代的不一定是迭代器


from typing import Iterable


list1 = [1,4,6,2,7]
f = isinstance(list1 , Iterable)
print(type(f))  #bool 类型
print(f)        #可迭代对象


# 列表推导式表示生成器
generator1 = (x+1 for x in range(10))
f = isinstance(generator1 , Iterable)
print(f)          #生成器是可迭代的


'''  
可以被next()调用,并不断返回下一个对象称为 迭代器 :Iterator
迭代器从第一个元素开始访问,直到所以元素都被访问完结束,只能前进不能后退
'''