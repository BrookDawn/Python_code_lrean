# sort  排序默认是升序的
# sort(reverse = True)  当reverse 等于True时，就是降序排列
# reverse 独立使用时是单纯的翻转，

'''
生成8个1-20之间的随机整数,保存到列表中

'''
import random
numbers = []

for i in range(8) :
    ran = random.randint(1,20)
    numbers.append(ran)
print(numbers)

numbers.sort()               #升序排列
print(numbers)

# numbers.sort(reverse= True)  #降序排列
# print(numbers)


# 在原来排好顺序的列表中加入一个数，然后排序
num = int(input('请输入一个数字:'))
for i in range(len(numbers)):
    if (numbers[i] <= num) and (numbers[i+1] >= num) :
        numbers.insert(i+1,num)
        break
print(numbers)

