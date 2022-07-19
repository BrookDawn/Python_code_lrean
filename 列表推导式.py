
# 正常的写法
list1 = []
for i in range(1,21):
    list1.append(i)
print(list1)

# 用列表推导式的写法就是
list2 = [i for i in range(1,21)]  #先执行for循环然后再参与到前面的i中，加到列表
print(list2)

list3 = [i for i in range(1,21) if i % 2 == 0] #先执行for，再执行if，满足条件就放到列表中

# 三目格式
# [结果1 if 条件 else 结果2 for 变量 in 可迭代的 ]

list4 = [[j for j in range(i, i+3)] for i in range(1,100,3)]
print(list4)

names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],['Alice','Jill','Ana']]

new_names = [j for i in names for j in i if j.count('e') >= 2]  #在names中的列表i中拿出j，j才是name
print(new_names)