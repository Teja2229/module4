file1 = open("MyFile.txt","r")
str=""
for i in range(0,100):
    str=str + file1.read(i)
print(str)
