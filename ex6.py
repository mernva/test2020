x="There are %d types of people." %10  #定义变量
binary="binary"
do_not="don't"
y="Those who know %s and those who %s." %(binary,do_not)  #python字符串格式化

print(x)
print(y)


print(" I said: %r." %x)
print("I also said :'%s'." %y)

hilarious = False
joke_evaluation ="Isn't that joke so funny! %r"

print(joke_evaluation  %hilarious)

w= "This os the left side of..."
e="a string with a right side."

print(w + e)