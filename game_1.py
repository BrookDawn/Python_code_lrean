'''
骰子游戏
两个1-6
1、玩游戏得先有金币;
2、每玩一局奖励金币一枚,充值获得金币;
3、10元20个金币
4、玩游戏消耗金币5个
5、猜大小,猜对奖励2枚;猜错,没有奖励
6、游戏结束:主动退出 or 没有金币自动退出
7、退出打印剩余金币数、游戏总次数、猜对的次数
'''


import random

coins = 0 #初始化金币数
count = 0 #初始化计数

if coins < 5:
    print('金币不足,请充值再继续开始')
    while True :
         money = int(input('请输入充值金额:'))
    
         if money % 10 == 0:
            coins += money // 10 *20
            print('充值成功\n当前金币数%d' % coins)

            print('你当前的金币数:%d' % coins)
            print('~~~~~~~~~开始你的游戏之旅~~~~~~~~')
            answer1 = input('是否开启游戏(y/n)')
            while True :
                if coins >= 5 and answer1 == 'y':
                    count += 1
                    #开始游戏赠送一枚金币
                    coins += 1
                    #每玩一局游戏扣五枚金币
                    coins -= 5
                    #产生两个随机数 1-6
                    ran1 = random.randint(1,6)
                    ran2 = random.randint(1,6)
                    guess = input('洗牌完毕,可以开始猜测:')
                    if guess == '大' and ran1 + ran2 > 6 or guess == '小' and ran1 + ran2 < 6 :
                        print('恭喜你猜对了,win')
                        coins += 2
                        print('你当前的金币数%d' % coins)
                    else :
                        print('你猜错了,很遗憾')
                        coins -= 5
                        print('你当前的金币数%d' % coins)
                        break
                elif coins < 5 and answer1 == 'n':
                    print('你当前的金币数量不够,请重新充值')
                    break
         elif money % 10 != 0:
            print('不是10的倍数,充值失败\n')
