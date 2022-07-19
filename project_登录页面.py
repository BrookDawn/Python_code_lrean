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


flag = True 

while flag:
    name = input('用户名/手机号码')
    if ( name.islower() and not name[0].isdigit and len(name) >= 6 ) or ( name.isdigit() and len(name) == 11 ) :
        while True:
            password = input('请输入密码: ')
            if password.isdigit() and len(password) == 6:
                if name == 'admin123' or '15811119999'  and password == '200325' :
                    print('登录成功')
                    flag = False
                    break
                else :
                    print('登录失败')
                    break
            else :
                print('密码格式错误,请重新输入')
    else :
        print('用户名或者手机号码格式错误\n')