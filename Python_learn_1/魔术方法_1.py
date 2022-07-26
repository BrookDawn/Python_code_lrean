# __new__实例化的魔术方法

class Person:
    def __init__(self,name):
        self.name = name

    def __new__(cls,*args,**kwargs):
        print('_____________>new')
        return object.__new__(cls,*args,**kwargs)  

#  __str__