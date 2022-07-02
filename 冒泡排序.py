#先随机生成10个数放在空列表里面
#然后通过冒泡的比较，进行排序

import random
numbers = []
for i in range(10) :
    ran = random.randint(1,50)
    numbers.append(ran)
print(numbers)

for n in range(0,len(numbers)-1):
    for m in range(0, len(numbers)-1-n):
        if numbers[m] > numbers[m+1] :
            numbers[m],numbers[m+1] = numbers[m+1],numbers[m] #两个数进行交换
print(numbers)