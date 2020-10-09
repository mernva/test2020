#1.1求阶乘
'''
def fac(num):
	result=1
	for n in range(1,num+1):
		result *= n
	return result

m=int(input('m= '))
n=int(input('n= '))

print(fac(m)//fac(n)//fac(m-n))   #求整数

#1.2实现最大公约数和最小公倍数的函数
def gcd(x,y):  #最大公约数
	(x,y)=(y,x) if x>y else(x,y)
	for factor in range(x,0,-1):
		if x % factor ==0 and y % factor ==0:
			return factor

def lcm(x,y):  #最小公倍数
	return x*y//gcd(x,y)
print(gcd(55,33))
'''
#1.3 判断一个数是不是回文数的函数,回文数是指一个数翻转过来还是等于它本身的数字
def is_palindrome(num):
	temp=num
	total=0
	while temp>0:
		total= temp % 10+ total * 10
		temp //=10
	return total ==num





#1.4判断一个数是不是素数,素数是指大于1除了1和自身没有其他公约数的数字
def is_prime(num):
	for factor in range(2,num):
		if num % factor ==0:
			return False
	return True if num !=1 else False



#1.5写一个回文素数
num=int(input('请输入正整数: '))
if is_prime(num) and is_palindrome(num):
	print('%d是回文素数' % num)
else:
	print('%d不是回文素数' %num)

