'''
图书管理系统
至少五本书
library = []  #书名 作者  馆存数量
1、借书
2、还书
3、查询
4、查看所以书
5、退出
'''


library = [ 
    {'bookname':'挪威的森林','author':'村上春树','number':20},
    {'bookname':'平凡的世界','author':'路遥','number':20},
    {'bookname':'1Q84','author':'村上春树','number':20},
    {'bookname':'海边的卡夫卡','author':'村上春树','number':20},
    {'bookname':'四世同堂','author':'老舍','number':20} 
]
book_name = [] #储存所有的书名，放进book_name中
book_num = []  #储存所以书的数量，放到book_num中
for book in library:
    book_name.append(book['bookname'])
    book_num.append(book['number'])
print(book_name)
print(book_num)

print('——————————欢迎进入图书馆管理系统————————')
flag = True 
while flag:
    choice = int(input('\n1、借书\n2、还书\n3、查询书籍\n4、查看所有\n5、退出\n请选择你想要的服务\n'))
    if choice == 1 :
    
        book_list = []  #创建借书列表 
        book_borrow = input('请输入你要借阅的书籍名称: \n')
        # 判断图书馆中是否存在
        for book in library:
            if book['bookname'] == book_borrow and book['number'] > 0 :
                print('借书成功！')
                print(f"书名:{book['bookname']},作者:{book['author']}库存:{book['number']-1}")
                break
            elif book['bookname'] != book_borrow :
                print('书名可能输入错误,图书馆内没有你要找的书.')
                break
            elif book['bookname'] == book_borrow and book['number'] == 0 :
                print('你想要借的书已经被借完了,下次早点来！')
                break
                 
    elif choice == 2 : 
        book_borrow = input('请输入你要还的书籍名称: \n')
        for book in library:
            if book['bookname'] == book_borrow and book['number'] < 20 :
                borrow_num = int(input('输入你要还书的数量:\n'))
                print('还书成功！\n')
                print(f"书名:{book['bookname']},  作者:{book['author']},  库存:{book['number'] + book_borrow}")
            elif book['bookname'] == book_borrow and book['number'] == 20 :
                print('当前该书的数量正常,请确认你是在这个图书馆中借出的吗?')
                break
            elif book['bookname'] != book_borrow:
                print('你的书不是从这里借出的,请寻找到正确的图书馆再还书。')
                break

    elif choice == 3 :
        book_finding = input('请输入你要查询的书籍名称: \n')
        for book in library:
            if book['bookname'] == book_finding:
                print(f"书名:{book['bookname']},   作者:{book['author']},   库存:{book['number']}")
                continue

    elif choice == 4 :
        print('正在查看所有书籍,请稍后: \n')
        print('当前图书馆里有的书籍信息如下： \n')
        for book in library:
            print(f"书名:{book['bookname']},  作者:{book['author']},  库存:{book['number']}")

    elif choice == 5:
        result = input('确定要退出系统吗(y/n) :')
        if result == 'y':
            flag = False
        elif result == 'n':
            pass
        else :
            print('输入错误，请重新输入！')
    else :
        print('输入失败,请重新输入')
