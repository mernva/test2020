'''
#1.1 判断1-100之间的奇数之和
#可以用''' '''或者""" """进行多行注释

sum=0
for x in range(1,101):
    if x %2 != 0:
        sum += x
print(sum)

sum=0
for x in range(1,101,2):
    sum+=x
print(sum)



 #1.2 猜数字游戏
import random

answer=random.randint(1,100)
counter=0

while True:
    counter += 1
    number =int(input('请输入:'))
    if number <answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了！')
        break  #终止所在那次循环。而continue循环是放弃本次循环后续的代码进入下一次循环
print('你总共猜了%d次' %counter)
if counter>8:
    print('你的智商余额不足:')


#1.3 输出九九乘法表
for i in range(1,10):  #外循环
    for j in range(1,i+1):  #内部嵌套
        print('%d * %d =%d' %(i,j,i*j),end='\t')
    print()



#1.4 输出一个正整数是不是素数
#素数指的是只能被1和自身整除的大于1的整数
from math import sqrt    #sqrt求平方根
num=int(input('请输入一个正整数:'))
p=int(sqrt(num))
is_primer=  True

for x in range(2,p):
    if num % x==0:
        is_primer=False
        break  #break跳出当前循环，而continue是不管本次循环后续的代码直接进入下一次循环
if num!=1 and is_primer:
    print("%d是素数" %num)
else:
    print('%d不是素数' %num)


#1.5 输入两个正整数，计算他们的最大公约数和最小公倍数
#提示:两个数的最大公约数是两个数的公共因子中最大的那个数，最小公倍数是是指同时被两个正整数整除的最小的那个数
# //求商的正数，向下取整；%求余
x=int(input('x='))
y=int(input('y='))
if x>y:
   x,y =y,x
for target in range(x,0,-1):  #从两个数中较大数做递减的循环
    if x% target==0 and y % target ==0:
        print('%d和%d的最大公约数是:%d' %(x,y,target))
        print('%d和%d的最小倍数是:%d' %(x,y,x*y//target))
        break
'''

#1.6打印三角形
row=int(input('请输入行数:'))
for i in range(row):
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(row,1,-1):
    for j in range(i-1):
        print('*',end='')  #没有end就是竖排
    print()

for i in range(row):
    for j in range(row):
        if j<row-i-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()


for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()


