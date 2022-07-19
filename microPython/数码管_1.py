import time
import machine

a = machine.Pin(13,machine.Pin.OUT)
b = machine.Pin(12,machine.Pin.OUT)
c = machine.Pin(14,machine.Pin.OUT)
d = machine.Pin(27,machine.Pin.OUT)
e = machine.Pin(26,machine.Pin.OUT)
f = machine.Pin(25,machine.Pin.OUT)
g = machine.Pin(33,machine.Pin.OUT)
h = machine.Pin(32,machine.Pin.OUT)   #数码管上面的一个小点

led_lsit = [a,b,c,d,e,f,g,h]

number_dict = {             #把数码管的显示数字储存在字典中
    0:"11111100",           #共阳极数码管
    1:"01100000",
    2:"11011010",
    3:"11110010",
    4:"01100110",
    5:"10110110",
    6:"10111110",
    7:"11100000",
    8:"11111110",
    9:"11110110",
}

def show_number(number):
    if number_dict.get(number):
        i = 0
        for num in number_dict.get(number):
            if num == '1':
                led_lsit[i].value(1)
            if num == '0':
                led_list[i].value(0)
            i += 1
            
#从0到9的数字显示，每个数字之间延时1秒            
for i in range(10):
   show_number(i)
   time.sleep(1)