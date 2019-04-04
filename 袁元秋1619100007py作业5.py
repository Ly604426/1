
import random as r
def student_name():
    xing=['刘','袁','王','陈','林','董','欧','崔','李','黄','邓','冯','肖','周','孔','劳','张','文','汤','习','朱','葛','郭']
    ming1=['莎','峰','轨','和','丹','胡','贵','萍','秋','佳','聪','富','学','德','星','丽','均','开']
    ming2=['丽','庆','清','明','铭','远','向','冰','幂','敏','杰','猪','肥']
    x= r.randint(0,len(xing)-1)
    m1= r.randint(0,len(ming1)-1)
    m2= r.randint(0,len(ming2)-1)
    return xing[x]+ming1[m1]+ming2[m2]
def number():
    x=int(r.random()*10000000000)
    return x
a=[]
for i in range(10):
    a.append(student_name())
t=[]
for i in range(10):
    t.append(number())
Tellbook={}
for i in range(len(a)):
    d1="{}".format(a[i])
    d2="{}".format(t[i])
    Tellbook[d1]=d2
import random as r

def fun1(a):   
    a=input("请输入姓名：")
    t=int(input("请输入手机号码："))
    d1="{}".format(a)
    d2="{}".format(t)
    Tellbook[d1]=d2
    print("")
    print("添加成功！")
    return print("")

def fun2(a):       
    b=input("请输入被删除人姓名：")
    if b in Tellbook:
        del Tellbook[b]
    print("删除成功！")
    return print("")



def fun4(a):         
    for i in range(1):
        for i,j in Tellbook.items():
            print(i,j,sep=':')
    print("")

def fun5(a): 
    b=input("请输入被查看人姓名：")
    if b in Tellbook:
        print(Tellbook[b])
    else:
        print("联系人不存在")
print("====通讯录管理系统====")
print("1.添加联系人")
print("2.删除联系人")
print("3.退出")
print("4.显示所有联系人")
print("5.查找联系人")
print("")

n=int(input("请输入您想实现的功能的序号："))
if n==1:
    fun1(a)
elif n==2:
    fun2(a)
elif n==3:
    fun3(a)
elif n==4:
    fun4(a)
elif n==5:
    fun5(a)
else:
    print("无效输入")
print("请选择“继续”或“退出”程序！")
print("“继续”请输入：1")
print("“退出”请输入：2")
symbol=int(input("指令："))

if symbol==1:
    dead_loop=1
    while(dead_loop==1):
        print("====通讯录管理系统====")
        print("1.添加联系人")
        print("2.删除姓名")
        print("3.退出")
        print("4.显示所有联系人")
        print("5.查找联系人")
        print("")

        n=int(input("请输入您想实现的功能的序号："))
        if n==1:
            fun1(a)
        elif n==2:
            fun2(a)
        elif n==3:
            break
        elif n==4:
            fun4(a)
        elif n==5:
            fun5(a)
        else:
            print("无效输入")
        print("“继续”请输入：1")
        print("“退出”请输入：2")
        symbol=int(input("指令："))
        if symbol==2:
            break
else:
    print("无效输入")

