#计算输入数字的和，input（）输出后是字符类型，要先转换为int或者float型
# one = input("请输入第一个数：")
# two = input("请输入第二个数：")

# print(int(one) + int(two))

a = '9.9'
print(float(a))
#字符类型的‘9.9’，转化为int行会报错，转化为float型能正常运行。
#str ---> int
#str ---> float

#int --->   str
#float ---> str

#int ---> float
#float ---> int    转化成int会抹掉小数点


# number = int(input('请输入一个整数'))
# a = number - 1
# print(a)

# 识别一个三位数三个位的数字
# number = int(input('请输入一个三位数：'))
# print('百位数:',number // 100)
# print('十位数：',number // 10 % 10)
# print('个位数：',number % 10)

#赋值运算符
# a = 2
# b = 4
# c = 0
# a += 1
# b -= 2
# print(a,b)

#输入考试成绩判断成绩是否在100到80之间
score = float(input("请输入你的分数："))
print(80<=score<=100)
#如果分数是在这个范围内就输出True，不在就输出False

#逻辑运算符
# and or not  与或非
# 结果也为布尔类型
