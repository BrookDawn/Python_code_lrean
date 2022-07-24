'''
面向对象: 类、 对象、 属性、 方法
程序
对象     --->   具体的事物
将现实中的东西转化为电脑程序————>世间万物都是对象

对象的共同特征: 构成一个类别
 特征 ----> 属性
 动作 ----> 方法
 # 多个对象,提取对象的共同特征和动作,然后封装到同一个类中
'''

# 所有的类名都要求首字母大写
'''
class 类名():
    属性:特征

    方法:动作
'''

# class Restaurant():
#     #魔术方法之一：__名字__():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type

#     def a(self):
#         print('餐厅的名字是' + self.name.title())
#     def b(self):
#         print('餐厅正在正常运行!')

# the_res = Restaurant("沙县","5种")
# print("my restaurant name is " + the_res.name.title())


# 先找自己空间的属性，如果没有就去模型中寻找属性

