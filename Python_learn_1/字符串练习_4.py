# 空格处理:    
# 添加空格，对齐输出的字符串   ljust   rjust  center
#                           左对齐， 右对齐，居中对齐
#  center(30):左右两边各生成30个空格
# ： lstrip      rstrip      strip
#  只去除左侧   只去除右侧   全部去除
# 字符串拼接:  join   把列表中的字符直接拼接，形成字符串


s = '  admin   '
print(len(s))        #打印原来字符串的长度    10
result = s.strip()   #去除字符串中的全部空格 
print(len(result))   #打印去除字符串后的长度   5
print(result)        #打印去除字符串后的结果


result = s.center(30)
print(len(result))
print(result)


'''
省略字段名
替代字段名的形式:{}
注意: 大括号个数可以少于位置参数的个数,反之不然
'''

name = '牛头人'
age = 18
print('我是{},今年{}岁'.format(name,age))  #注意是用点来间隔开
# 输出结果: 我是牛头人，今年18岁。传入字符串或者数字都可以



#也可以传入format后面参数的下标
name = '内鬼'
score_chinese = 100
score_math = 99
#英语成绩和数学成绩一样
s = '{0}本次考试的数学分数是{2},语文分数是{1},英语分数是{2}'.format(name,score_chinese,score_math)
print(s)