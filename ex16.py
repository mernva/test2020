from sys import argv  #引入sys模块的argv方法

script,filename=argv  #对argv进行解包

print("We're going to erase %r." %filename)
print("If you don't want that,hit ctrl-c")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
target =open(filename,'w')


print("Truncating the file. Goodbye!")
target.truncate() #调用truncate方法，清空文件

print("Now I'm going to ask you for three lines.")

line1 =input("line 1:") #输入
line2 =input("line 2:")
line3 =input("line 3:")

print("I'm going to write these to the file")

#target.writelines(list)  列表可以实现多行写入，但是没有换行、空格
target.write('\nline1\nline2\nline3')  #如何用字符串，格式化字符，转义字符实现一次写入多行呢？

target.close()   #需先关闭
print("Open the file again:")
file_again=input('>')

target_again=open(file_again)   #必须先将文档关闭后再打开
print(target_again.read())

 