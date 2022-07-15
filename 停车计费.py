'''
停车计费系统
1、进入停车场会记录时间,出去也会有时间记录,停车的时间记录格式是: 13:00-15:00
2、停车场的数据结构是:[{'车牌':[进入时间,0]}]:用随机数生成停车时间
3、提示收费: 15分钟一块钱
4、停车变量--->全局变量
5、函数设计:
def enter():
    #键盘输入车牌号
    
def go_out():
    #键盘输入车牌号
时间会被记录
'''
import random
car_park = []                    #建立一个空的停车场

def enter():
    print('欢迎进入停车场！')
    number = input('输入你的车牌号即可停车:\n')
    #  构建字典的结构
    car = {}
    car[number] = [0]
    car_park.append(car)
    print('车牌号: {},已经进场'.format(number))


def go_out():
    number = input('请输入你的车牌号: ')
    for car in car_park:
        if number in car:
            #计算停车时间:分钟
            time = random.randint(0,720)
            time_record = car.get(number)
            time_record.append(time)
            total = (time / 15)
            print('车牌号{}的车主,您一共停车{}分钟,总计应缴费{}元'.format(number,time,total))
            print('欢迎您再次光临！')
        else :
            print('您输入的车牌号没在停车场里面,请重新输入.')
