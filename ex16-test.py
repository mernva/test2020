#1.1将华氏温度转换为摄氏温度
#华氏温度到摄氏温度公式:c=(f-32)/1.8
f=float(input('请输入摄氏温度：'))
c=(f - 32)/1.8

#print('%.1f华氏度=%.1f摄氏度' %(f,c))

print(f'{f:.1f}华氏度={c:.1f}摄氏度')  #{f:.1f}和{c:.1f}表示{f},{c}的占位符


#1.2输入圆半径计算周长和面积

radius=float(input('请输入半径:'))
perimeter=2*3.14*radius
area=3.14*radius**2
print('周长:%.2f' %perimeter)
print('面积:%.2f' %area)

#1.3判断年份是不是闰年
year=int(input('请输入年份:'))


if(year % 4==0 and year % 100 !=0 or year % 400 ==0):
    print("year is 闰年")
else:
    print("year is 平年")

#1.4分段函数求值

x=float(input('x= '))
if x>1:
    y=3*x-5
elif -1<=x<=1:
    y=x+2
else:
    y=5*x+3
print('f(%.2f)=%.2f' %(x,y))

#1.6 英尺单位尺寸与公制厘米互换
value=float(input('请输入长度:'))
unit=input("请输入单位: ")
if unit=='in' or unit == '英寸':
    print('%f英寸=%f厘米' %(value,value*2.54))
elif unit=='cm' or unit=='厘米':
    print('%f厘米=%f英寸' %(value,value/2.54))
else:
    print('请输入有效的单位')

#1.7 百分制成绩转换为等级成绩
score=float(input('请输入成绩:'))
if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score >=70:
    grade='C'
elif score >=60:
    grade='D'
else:
    grade='E'
print('这个学生的等级是:',grade)

#1.8输入三条边长，如果能构成三角形就计算周长面积
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))

if(a+b>c and b+c >a and c+a >b):  #任意两边之和大于第三边
    print('周长:%f' %(a+b+c))
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5 #使用海伦公式
    print('面积:%f' %area)
else:
    print("不能构成三角形")