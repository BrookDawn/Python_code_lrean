'''
角色:  姓名、性别、职业
添加角色、删除角色、修改角色
查询角色
显示所以角色
退出系统

'''

all_role = [] #存放角色的列表


print('-----------欢迎进入王者荣耀角色管理系统-----------')

flag = True
while flag:
    choice = input('1.添加角色\n2.删除角色\n3.修改角色\n4.查询角色\n5.显示所以角色信息\n6.退出系统\n')
    
    if choice == '1':
        name = input('请输入角色名称: ')
        sex = input('请输入角色性别: ')
        job = input('请输入角色职业: ')
        role = [name , sex , job]
        all_role.append(role)
        print('成功添加{}到王者荣耀中!\n'.format(name))
    elif choice == '2':
        role_name = input('请输入要删除的角色名称: ')
        #判断该角色是否在系统中
        for role in all_role:
            if role_name in role :
                del_name = input('是否确定删除该角色(y/n)')
                if del_name == 'y' :
                    all_role.remove(role)
                    print('成功删除{}'.format(role_name))
                    break
                elif del_name == 'n':
                    print('你的选择是正确的,这个英雄以后还能创造更多的money!')
                    pass
                else :
                    print('输入错误,请重新输入!!!')
                    pass
        # 不存在该角色
        else :
            print('本系统不存在{},请重新输入'.format(role_name))

    elif choice == '3':
        role_name = input('请输入要修改的角色名称:')
        #判断该角色是否在系统中
        for role in all_role :
            if role_name in role :
                change_role = input('是否确定修改该角色的信息?(y/n)')
                if change_role == 'y' :
                    all_role.remove(role)
                    name = input('请输入修改后的角色名称: ')
                    sex = input('请输入修改后的角色性别: ')
                    job = input('请输入修改后的角色职业: ')
                    role = [name , sex , job]
                    all_role.append(role)
                    print('成功修改{}!\n'.format(name))
                    print('当前你的角色总共有: ')
                    print('{}{}{}'.format('名称'.center(10),'性别'.center(11),'职业'.center(10) ) ) 
                    for role in all_role:
                        print(role[0].center(10),end=' ')
                        print(role[1].center(10),end=' ')
                        print(role[2].center(10),end=' ')
                        print('\n')
                elif change_role == 'n':
                    print('你的辣鸡英雄再不改改,money就都要跑路了')
                    break
                else :
                    print('输入错误，请重新输入')
                    pass
    elif choice == '4':
        print('这里是查询角色模块')
        role_name = input('请输入要查询的角色名称:')
        for role in all_role:
            if role_name in role :
                print('你要查询的角色是\n')
                print('{}{}{}'.format('名称'.center(10),'性别'.center(11),'职业'.center(10) ) ) 
                print('{}{}{}'.format(role[0].center(10),role[1].center(11),role[2].center(10)))
                print('\n')
        else :
            print('本系统不存在{},请重新输入'.format(role_name))           

    elif choice == '5':
        print('{}{}{}'.format('名称'.center(10),'性别'.center(11),'职业'.center(10) ) ) 
        for role in all_role:
            print(role[0].center(10),end=' ')
            print(role[1].center(10),end=' ')
            print(role[2].center(10),end=' ')
            print('\n')

    elif choice == '6':
        print('成功退出管理系统')
        flag = False

    else :
        print('输入错误,请重新选择')