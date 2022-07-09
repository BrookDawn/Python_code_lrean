def greet_user(username):
    print('hello, ' + username.title() +'!')
greet_user('john')

def favorite_book(author,bookname):
    print('One of my favorite book is ' + author.title()+ ' 的 ' + bookname.title())
favorite_book('村上春树','《呜呜呜》')

# 返回字典
def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hex')
print(musician)


def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name

while True:
    print('\nPlease tell me your name: ')
    f_name = input('First name: ')
    l_name = input('Last name: ')
    formatted_name = get_formatted_name(f_name,l_name)
    print('\nHello, '+ formatted_name + '!')

