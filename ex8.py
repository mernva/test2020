formatter ="%r %r %r %r"


print(formatter %(1,2,3,4))
print(formatter %("one","two","three","four"))
print(formatter %(True ,False,True,False))
print(formatter %(formatter,formatter,formatter,formatter))
print(formatter %("一","二","三","四"))

print(formatter %(
"I had this thing",
"That you could type up right",
"But it don't sing",
"So I said goodnight.")
)


print("%s %s %s %s" %("一","二","三","四"))