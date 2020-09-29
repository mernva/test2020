#1.1 寻找水仙花数
#说明：水仙花数是一个三位数，其百位、十位、个位各自的立方和等于该数值本身
'''
for num in range(100,1000):
    high= num //100
    mid = num //10 %10
    low = num % 10
    if num==high **3 + mid ** 3+ low ** 3:
        print(num)
       
#1.2正整数反转
num = int(input('请输入正整数:'))
reverse_num= 0 #初始赋值

while num>0:
    reverse_num= num%10+reverse_num*10
    num//=10
print(reverse_num)

#1.3百钱百鸡问题

for x in range(0,20):
    for y in range(0,33):
        z=100-x-y
        if 5*x+3*y+z/3 ==100:
            print('公鸡:%d只,母鸡:%d只,小鸡:%d只' %(x,y,z))
      

#1.4 CRAPS赌博游戏

from random import randint
money =1000
while money >0:
    print('你的总资产为:',money)
    needs_go_on =False
    while True:
        debt=int(input('请下注:'))
        if 0<debt<= money:
            break
    first =randint(1,6)+randint(1,6)
    print('玩家玩出了%d点' %first)
    if first==7 or first == 11:
        print('玩家胜利')
        money += debt
    elif first==2 or first==3 or first==12:
        print('庄家胜利')
        money -= debt
    else:
        needs_go_on=True
    while needs_go_on:   #使用while避免使用if多次嵌套
        needs_go_on=False #只有false情况才能执行以下代码
        current=randint(1,6)+randint(1,6)
        print('玩家玩出了%d点' %current)
        if current ==7:
            print('庄家胜利')
            money-=debt
        elif current==first:
            print('玩家胜利')
            money+= debt
        else:
            needs_go_on=True
print('you have no money,game over!!!')

     

#1.5生成斐波那契数列的前20个数
def fib(i):
    if i<=1:
        return 1
    else:
        result=fib(i-1)+fib(i-2)
        return result
for i in range(20):
    print(fib(i),end=' ')
print()

 
#1.6找出10000内的完美数
#完美数是指除自身外所有整除数之和等于这个数本身的数.
#6=1+2+3 ,28=1+2+4+7+14

for num in range(1,10000):
    sum =0   #初始定义赋值
    for i in range(1,num):
        if num % i ==0:
            sum+=i
    if sum == num:
        print(num)

'''

#1.7输出100以内的所有素数
#素数是指被1和自身整除的正整数(不包括1)

import math
for num in range(2,100):
    is_prime=True
    for factor in range(2,int(math.sqrt(num))+1):
        if num % factor == 0:
            is_prime=False
            break
    if is_prime:
        print(num,end=' ')
print()
