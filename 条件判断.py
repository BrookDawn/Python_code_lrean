'''
if
if...else
if...elif....else

'''


# result = input('请输入(y/n):')
# if result == 'y':
#     print(4)
#     print('over')
# elif result == 'n':
#     print('请再次输入')
# else :
#     print('输入错误')

'''
import random               #调出随机数
ran = random.randint(1,10)  #产生一个从1到10的随机数
guess = int(input('请输入一个1到10的数字:')) #注意输入的值要进行类型转化
print(ran)

#把产生的随机数和猜测的数字进行对比
if guess == ran & 1<=guess<=10 :
    print('猜测正确')
elif guess != ran  & 1<=guess<=10 :
    print('猜测错误')
else :
    print('输入的数字不和规范,请重新输入')
'''

# 在键盘上输入用户名 和 密码

# username = input('用户名')
# password = input('密码')
# is_remember = True

# if username == 'admin':
#     if password == '1234':
#         print('密码正确')
#         print(is_remember)
#     else :
#         print('密码错误')
# else :
#     print('用户名错误,请重新输入')


'''
输入一个年份,判断是否为润年
'''
'''
year = int(input('请输入一个年份'))
if year % 4 == 0 and year % 100 != 0 :
    print('这一年是闰年')
elif year % 400 == 0 :
    print('这一年是闰年') 
else :
    print('这一年不是闰年')
'''

# 模拟超市付款：商品单价、商品数量
# 在键盘上输入商品单价，以及商品数量
# 然后计算应付的总额（float）
# 提醒用户可以用四种付款方式（现金、微信九五折、支付宝九折、刷卡满100-20）


# print('欢迎光临,可以开始结账')
# price = float(input('商品单价'))
# number = int(input('商品数量'))
# total = price * number
# print(total)
# print('您可以选择四种支付方式')

# ch = input('1、现金;2、微信;3、支付宝;4、银行卡;')
# if ch == '1':
#     print("请支付现金",total)
# elif ch == '2':
#     print('请在微信上支付',total*0.95)
# elif ch == '3':
#     print('请在支付宝上支付',total*0.9)
# else :
#     total = total - (total // 100)*20
#     print('请刷卡支付%d',total)


