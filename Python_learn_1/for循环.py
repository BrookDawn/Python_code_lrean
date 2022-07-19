<<<<<<< HEAD
# python 中的for循环是封装好了的，只要按照格式写就行
#  for i in range(n) :
#  range(n) 函数的使用，默认从0到n-1，n个数字
#  range(start,stop)   [start,stop)  左闭右开
#  可以传三个参数
#  range(start,stop,step)  依然是这个范围[start,stop)  左闭右开
#  默认的增量是1，第三个参数是增量，可以以其他的大小增加

'''
多次输入用户名,如果三次没有登录成功,账号提示被锁定。


for i in range(1,4):
    username = input('用户名：')
    password = input('密码：')

#判断输入的是否正确
    if username == 'admin' and password == '1234' :
        print('用户登录成功！')
        break
    print('用户名或者密码错误！\n')

print(i)
'''

# for...else...(for 完全执行完，没有被中断过，就会默认执行else里面的内容)
=======
# python 中的for循环是封装好了的，只要按照格式写就行
#  for i in range(n) :
#  range(n) 函数的使用，默认从0到n-1，n个数字
#  range(start,stop)   [start,stop)  左闭右开
#  可以传三个参数
#  range(start,stop,step)  依然是这个范围[start,stop)  左闭右开
#  默认的增量是1，第三个参数是增量，可以以其他的大小增加

'''
多次输入用户名,如果三次没有登录成功,账号提示被锁定。


for i in range(1,4):
    username = input('用户名：')
    password = input('密码：')

#判断输入的是否正确
    if username == 'admin' and password == '1234' :
        print('用户登录成功！')
        break
    print('用户名或者密码错误！\n')

print(i)
'''

# for...else...(for 完全执行完，没有被中断过，就会默认执行else里面的内容)
>>>>>>> 4964576990c8a7518637762eb505343c55f336e8
