'''
字符串变量[start:end]
字符串变量[start:end:step]   默认从左到右依次取元素
step 正数 从左向右
     负数 从右向左

索引和切片
len()字符串长度
切片格式:
print(s1[1:4])  #左闭右开
print(s1[:4])   #没有前面的就是默认从0开始
或者是
print(s1[-3:])  #后面省略不写就默认取到最后一个字符,从后面开始数第三个是-3

print(s1[1:-1:2])   #第三个变量是取的步长

'''
# s1 = '1234567890'
# print(s1[::-2])        #反方向，从零开始取到结束
# print(s1[0:])

# 字符串的查找
# find, index, rfind, rindex ;r是从右侧开始查找

# 字符串的统计
# count 统计指定字符串的个数; i = path.count()

# 字符串的判断
# startswith, endswith, isalpha, isdigit, isalnum, isspace
# 返回值都是布尔类型


'''
path = 'https://www.baidu.com/img/dong_e70247ce4b0a3e5ba73e8b3b05429d84.gif'

i = path.find('_')
print(i)
image_name = path[i+1:]
print(image_name)
'''
'''
result = path.startswith('h')   #判断是否是以'h'开头的
'''


# 模拟文件的上传，键盘输入文件上传的名称，判断文件名是否是大于六位数字以上，
# 拓展名是否为jpg、GIF、png格式，如果不是则提示上传失败，如果名字不符合条件
# 而拓展名满足条件则随机生成一个6位数字组成的文件名，打印成功上传xxx.png
