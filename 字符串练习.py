# 模拟文件的上传，键盘输入文件上传的名称(abc.jpg)，判断文件名是否是大于六位数字以上，
# 拓展名是否为jpg、GIF、png格式，如果不是则提示上传失败，如果名字不符合条件
# 而拓展名满足条件则随机生成一个6位数字组成的文件名，打印成功上传xxx.png

import random

while True :
    file = input('请输入文件的名称')
    #判断文件名
    if file.endswith('jpg') or file. endswith('gif') or file.endswith('png') :
        #判断文件的名字
        i = file.rfind('.')
        name = file[:i]
        #判断文件名是否符合规范
        if len(name) < 6:
            print('您的文件名不符合规范,已经自动帮您生成了一个文件名')
            #重构文件名
            file_name = ''
            s = 'qwerytouipdasfghljkzcxnbvm'
            for a in range(6) :
                index = random.randint(0 , len(s) - 1)   #标记下标
                file_name += s[index]                    #获得随机生成的字符串
            name = file_name + file[i:]
        print('成功上传%s文件' % name)
        m = input('是否再次上传文件,退出请输入q,按任意键继续上传文件\n')
        if m == 'q':
            break
        else :
            pass
    else :
        print('文件格式错误,上传失败')

'''
随机产生字母和数字的组合
'''

# file_name = ''
# s = 'qwerytouipdasfghljkzcxnbvm'
# for a in range(6) :
#     index = random.randint(0 , len(s) - 1)   #标记下标
#     file_name += s[index]                    #获得随机生成的字符串
# print(file_name)