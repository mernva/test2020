from sys import argv  #引入sys模块的argv方法
script,input_file=argv#解包

def print_all(f):  #定义print_all函数
    print(f.read())
def rewind(f):   #定义rewind函数
    f.seek(0)   #移动文件读取指针到指定位置

def print_a_line(line_count,f): #定义print_a_line，有两个参数
    print(line_count,f.readline())

current_file =open(input_file)  #打开输入的文件

print("First let's print the whole file:\n",)

print_all(current_file)  #调用print_all函数，打印全部

print("Now let's rewind,kind of like a tape")

rewind(current_file)   #调用rewind函数,重新打印全部

print("Let's print three lines:")

current_line=1

print_a_line(current_line,current_file)

current_line=2
print_a_line(current_line,current_file)

current_line=3
print_a_line(current_line,current_file)