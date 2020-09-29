from sys import argv  #引入sys模块的argv方法
script,input_file=argv#解包

def print_all(f):  #定义print_all函数
    print(f.read())
def rewind(f):   #定义rewind函数
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file =open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind,kind of like a tape")

rewind(current_file)

print("Let's print three lines:")

current_line=1

print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)