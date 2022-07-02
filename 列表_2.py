#  删除:    pop                       remove                           clear 
#     删除列表中的元素(填下标)   直接填入列表中元素的名称，然后移除    清空列表元素
#   del list :删除整个列表，该列表就不存在了
#   del list[下标]  删除列表中指定下标的元素

# remove 从左往右开始检索，只删除第一个标定的元素


# 修改  insert(下标，新元素)   插队，插入到哪个位子上
# 正确的修改是直接给位置赋新值

# .clear  清空列表元素
# .count  查找列表中存在的元素，不存在就返回0，存在就返回相应的个数
# in , not in   返回是bool值

list1 = ['火腿肠','酸奶','面包','酸奶','酸奶','酸奶']
list1.remove('酸奶')
print(list1)           #运行结果是   ['火腿肠', '面包', '酸奶', '酸奶', '酸奶']
#如果想删掉多个重复的元素，要进行多次循环

n = 0 
while n < len(list1) :
    if list1[n] == '酸奶' :
        list1.remove('酸奶')
    else :
        n += 1
print(list1)

n = 0
list2 = []  #开一个新的列表来放置移走的元素，然后输出原来的列表
for n in range(len(list1)):
    if list1[n] == '酸奶' :
        list2 = list1.remove(n)
    else :
        n += 1
print(list1) 

list1[1] = 0    #原来的是火腿肠，面包
print(list1)    #替换后是火腿肠，0

place = list1.index('火腿肠')   #index()是查找元素在列表中的位置，然后可以直接替换
list1[place] = '辣条'
print(list1)

