f = open('test.txt','rb+')
f.write(('0123456789').encode())

f.seek(3)