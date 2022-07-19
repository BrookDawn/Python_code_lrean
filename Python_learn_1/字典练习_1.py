#输入三本书的信息，然后放在列表中
books = []

while True :                   #输入三本书的信息
    if len(books) == 3:        #当达到三本时就自动跳出
        break
    
    name = input('请输入书名')  

    for book in books :
        if name == book.get('name'):    #判断书名是否重复
            print('书名重复')
            break
    else :
        author = input('输入作者')
        price = input('输入书的价格')

        books.append(
            {
                'name':name,
                'author':author,
                'price':price
            }
        )
print(books)