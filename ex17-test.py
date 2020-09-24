#1.1 判断1-100之间的奇数之和

sum=0
for x in range(1,101):
    if x %2 != 0:
        sum += x
print(sum)

'''
sum=0
for x in range(1,101,2):
    sum+=x
print(sum)
'''


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

