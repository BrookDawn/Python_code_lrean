'''
定义两个类
公路(Road)
    属性:公路名称,公路长度

车(Car)
    属性:车名,时速
    方法 : 1、求车名在那条公路上以什么速度行驶了多远的距离
           2、初始化车的属性__init__方法
           3、打印对象显示车的属性信息

'''

import random


class Road:
    def __init__(self,name,len):
        self.name = name
        self.len = len


class Car:
    def __init__(self,brand,speed) -> None:
        self.brand = brand
        self.speed = speed
    
    def get_time(self,road):
        ran_time = random.randint(1,10)
        msg = "{},在{}上,以{}的速度行驶{}小时".format(self.brand,road.name,self.speed,ran_time)
        print(msg)

    def __str__(self) -> str:
        return "{},速度:{}".format(self.brand,self.speed)

r = Road('京藏高速',12000)
audi = Car("奥迪",120)
print(audi)
audi.get_time(r)