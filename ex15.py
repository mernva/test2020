from sys import argv  #引入sys模块的argv方法
script,filename=argv  #对argv 进行解包，将argv中每个参数赋值给左边


txt=open(filename)  #open接受文件类型，返回文件对象，等同于input()接收参数并且返回一个值，我可以把值赋给变量。open()用于打开文件，创建file对象，相关方法才可以调用它进行读写。

print("Here's your file %r:" %filename)
print(txt.read()) #调用txt的read()函数

print("Type the filename again:")
file_again =input('>')   #用变量对命令提示符进行定义方便调用

txt_again=open(file_again) #open接受文件类型，返回文件对象，将值赋值给左边
print(txt_again.read())  #调用txt_again的read()函数


print(txt.close()) #关闭
