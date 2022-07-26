#封装: 1、私有化属性，2、定义共有化set和get方法
#私有化隐藏属性，不被外界随意修改，可以通过函数进行修改和筛选(判断是否符合条件)

class Student:
    # __age = 18  #类属性
    def __init__(self,name,age,score):
        self.name = name 
        self.age = age
        self.__score = score   # 私有化，不可在外部修改
    
    #定义公有的set和get方法(set是赋值，get是取值)
    def setScore(self):
        self.__score = 80 
    def getScore(self):
        return self.__score 
    def __str__(self):
        return "姓名:{},年龄:{},考试分数:{}".format(self.name,self.age,self.__score)


yupeng = Student('yupeng',18,80)
print(yupeng.getScore())