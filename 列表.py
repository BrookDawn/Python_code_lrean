# 列表: 存储多个数据。然后可以统一打印
# 列表里面可以套列表
# 通过下标可以取出列表中单独的字符

# 切片  和字符串中的切片一样，[a:b] 左开右闭

# .append()  添加新的到列表中
# .extned()  把原来的列表扩充

'''
shopping_list = []   #定义一个空的列表
shopping_list1 = []

#添加    删除    修改    查询

shopping_list.append('面包')
shopping_list1.append('火腿肠')
print(shopping_list)         
print(shopping_list1)

shopping_list1 = shopping_list1 + shopping_list   #把两个列表相加
print(shopping_list1)

shopping_list1.extend(shopping_list)          #extend 扩充，把括号内的变量添加到前面的列表中
print(shopping_list1)
'''



shopping_lists = []   #定义一个空列表存放
while True :
    name = input('商品名称:')
    price = input('商品单价:')
    number = input('商品数量:')
    goods = [name,price,number]

    shopping_lists.append(goods)  #把物品放到购物车中
    answer = input('是否继续加入商品,退出请按Q/q\n')
    if answer.lower == 'q':
        break
    else :
        pass
print('-*-'*20)
for goods in shopping_lists:
    print(goods)
    print(shopping_lists)