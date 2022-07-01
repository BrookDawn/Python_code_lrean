'''
模拟论坛输入
要求
1、可以输入用户名
2、回复的内容不能为空
3、可进行多次的回复
4、每次评论最多可以20个字,显示剩余字数
5、回复的内容的前后不可以有空格
6、里面不能存在敏感词汇,如果有要进行替换
'''
# 流程
# 1、输入用户名
# 2、输入回复的消息
# 3、验证回复的消息，没有验证成功则重新输入
# 4、评论成功后，是否再次评论


words = 'nmd'

msg = input('论坛的帖子:')
print('-'*50)
print('以下为回答的内容')
while True :
    username = input('用户名:')
    comment = input('评论:')
    comment = comment.strip()
    if len(comment) != 0 :
        if len(comment) <= 20:
            comment = comment.replace(words,'***')
            print('\t{}发表的评论是:\n\t{}'.format(username,comment))
        else :
            print('评论过长,请减少评论字数')
    else :
        print('您输入的内容为空,请再次输入')
    
