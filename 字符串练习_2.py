#    isalpha           isdigit          isalnum                 isspace
# 判断是否为纯字母    判断是否为纯数字   判断是否为字母和数字组合    判断是否是空格

#       isupper 
#  判断是否全部是大写字母   

'''
s = 'A1234'
result  = s.isalpha()  #纯字母返回True
print(result)          #不是纯字母,返回False

s = '1234'
result = s.isdigit()
print(result)          

s = 'A1234'
result = s.isalnum()
print(result)         

'''

'''
用户名或者手机号登录+密码
用户名: 全部是小写,首位不能是数字,长度必须是6位以上
手机号码: 11位纯数字

密码是六位数字;
都符合规范就进行验证 是否正确

用户名:   admin123
电话号码: 15811119999
密码 :    200325
'''