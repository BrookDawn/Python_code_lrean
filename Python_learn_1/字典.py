# 键 可以添加、删除，但是键是不能修改的，只能修改键后面的值

# 1、添加元素:
# 字典名[key] = value
# 注意: key是唯一的，所以在添加的时候如果出现同名的key，后面的key对应的value值会替换掉原来的value

# 2、修改value值
# 字典名[key] = value
# 

# 字典有点类似C语言中的结构体
book = {}
book['书名'] = '《三体》'
book['价格'] = 20
book['作者'] = '刘慈欣'
print(book)

book1 = {}
book1['书名'] = '《挪威的森林》'
book1['价格'] = '32'
book1['作者'] = '村上春树'


#  修改价格
book['价格'] *= 0.8  # 原来的价格乘以0.8 等于现在的价格  是16
print(book)

result = book.pop('价格')    #删除里面价格的元素
print(book)

# popitem
r = book.popitem()
print(r)              #把字典里面的最后一个元素删掉，放在元组里面
print(book)           #当字典里面没有东西时，就会出现异常

#字典可以放在列表中
list_book = [book1,book]
print(list_book)


#  根据key得到value值
#  dict.get():根据key来获取value值  #key如果不存在则默认返回None，，可以设置返回的默认值
#  dict[key]:根据key来获取value值   #key如果不存在则报keyerror

value = book1.get('书名')
print(value)

# 如果使用for...in直接遍历字典，取出的只有key值

# 如果要获取value值，

print(list(book1.values()))   #列表结构

for v in book1.values():      #获取字典中所有的值
    print(v)                   

# 字典的items，把每一项都放在元组里面，然后通过列表一起输出
print(book1.items())# dict_items([('书名', '《挪威的森林》'), ('价格', '32'), ('作者', '村上春树')])


#   用for in的形式去输出
for i in book1.items() :
    print(i)               # 以元组的形式去输出key和value

for k,v in book1.items() : # 把key和value 分开输出
    print(k,v)

#只能用添加键值对使用
book1.setdefault('出版社','人民教育出版社')
print(book1)                        # 在原来的基础上次添加
# 添加后{'书名': '《挪威的森林》', '价格': '32', '作者': '村上春树', '出版社': '人民教育出版社'}

# update 实现两个列表的合并
dict1 = {'a':10,'b':20}     #把book列表和dict1两个组合到一起
book.update(dict1)           
print(book)

print(book)
result = dict.fromkeys(['a','b'],[10]) #以整体的形式给a，b赋值
print(result)