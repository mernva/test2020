from sys import argv  #引入argv模块
script,user_name=argv  #对argv进行解包，将每个参数赋值给左边的变量

attention=">"  #将提示符设置为prompt变量

print("Hi %s,I'm the %s script." %(user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" %user_name)
likes=input(attention)


print("Where do you live %s?" %user_name)  
lives=input(attention)

print("what kind of computer do you have?")
computer=input(attention)


print("""
Alright,so you said %r about liking me.
You live in %r.Not sure where that is.
And you have a %r computer.Nice.
"""  %(likes,lives,computer) )  #双引号用于多行输入4
