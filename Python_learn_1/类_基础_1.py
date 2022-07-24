'''
1、寻找空间,有没有该对象的内存空间
2、利用类,向内存申请一块和Phone一样的空间
3、去寻找__init__中有没有,如果没有就执行开辟空间内存给该对象
4、如果__init__有就去执行init方法里的动作

'''
# 类中方法: 动作
# 种类: 普通方法、类方法、静态方法、魔术方法


# 类方法 : 类方法中只能用类属性，不能用对象属性
# 类中方法的调用，需要通过self.方法名()
# 类方法的作用:只能访问类属性和类方法，所以可以再对象创立之前，如果需要完成一些动作，可以用类方法
class Dog:
    def __init__(self,nickname):
        self.nickname = nickname
    
    def run(self):
        print("{}在院子里跑来跑去!\n".format(self.nickname))

dog1 = Dog('大黄')  # 对象1，大黄       
dog1.run()


'''
私有类: 在类中的参数前加上__, __参数 = 
就不可以在外界调用,只能通过@classmethod 定义其他类来调用

'''

'''
静态方法: 
1、需要装饰器@staticmethod
2、可以没有参数
3、也只能访问类的属性和方法,对象的是无法访问的
4、加载时机和类方法一样

总结: 类方法和静态方法
不同之处 1、装饰器不同  2、有无参数(静态方法没有参数)
相同之处 3、只能访问类的属性和方法,对象的是无法访问的
        4、都可以通过类名去调用访问

普通方法: 
1、没有装饰器
2、永远需要依赖对象,因为普通方法都有一个self
3、只用创建对象才能调用普通方法,否则无法使用
'''
class Person:
    __age = 18

    def show(self):
        print('------->',Person.__age)

    @classmethod     # 类方法
    def update_age(cls):
        cls.__age = 20
        print('------>类方法')
    
    @classmethod
    def show_age(cls):
        print('修改后的年龄是:',cls.__age)

    @staticmethod                #修饰器,声明静态方法
    def test():                  #静态方法，可以没有参数
        print('----->静态方法')

# Person.update_age()  # 先更新,在展示年龄
# Person.show_age()

