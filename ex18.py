def print_two(*args):
    arg1,arg2=args  #解包
    print("arg1:%r,arg2:%r" %(arg1,arg2))

def print_two_again(arg1,arg2):
    print("arg1:%r,arg2:%r" %(arg1,arg2))

def print_one(arg1):
    print("arg1:%r" %(arg1))

def print_none():
    print("I got nothing")

print_two("mernva",'alex')
print_two_again("mernva","alex")
print_one("First")
print_none()