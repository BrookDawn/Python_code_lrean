#  替换内容 replace
#  切割字符串  split  rsplit   splitlines   partition   rpartition  
#  修改大小写     capitalize                   title            upper       lower 
#            一句话中第一个单词转大写   一个单词的首字母转大写   全部转大写   全部转小写
'''

s = 'hello,world;hello,people'
result = s.replace('hello','hi')      #传入两个参数，第一个是原字符串中的  
print(result)                         #第二个参数是替换后的结果
                         

s = 'hello,world;hello,people'    
result = s.replace('hello','hi',1)     #第三个参数是指定替换的次数
print(result)                          #从左到右进行替换

'''



s = '牛头人   内鬼   郭导'    #传入的参数是空格，就是搜索空格进行分隔
result = s.split('  ')       #把字符串分割开，然后放置在列表之中
print(result)

s1 = 'hello,world'
s2 = 'HELLO,WORLD'
result = s1.capitalize()    # 一句话中第一个单词转大写
print(result)

result = s1.title()         #每一个单词的首字母转大写
print(result)

result = s1.upper()         #全部转大写
print(result)

result = s2.lower()         #全部转小写
print(result)