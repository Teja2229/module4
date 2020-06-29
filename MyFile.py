file1 = open("MyFile.txt","r") 
content = file1.read()
print(content)
file1 = open("Myfile.txt","w") 
t= ["This is Delhi\n","This is Paris \n","This is London\n","This is korea\n"] 
file1.write("Hello \n") 
file1.writelines(t) 
file1.close() 
