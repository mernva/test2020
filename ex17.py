#将一个文件内容复制到另外一个文档中

from sys import argv
from os.path import exists
script,from_file,to_file=argv

print("Copying from %s to %s" %(from_file,to_file))

indata=open(from_file).read()

print("The input file is %d bytes long" %len(indata))

print("Does the output file exists? %r" %exists(to_file))  #exists将文件名字符串作为参数，如果文件存在，将返回true，否则返回false
print("Ready,hit return to continue,ctrl-c to abort")
input()


open(to_file,'w').write(indata)

print("Alright,all done")

