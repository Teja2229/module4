t=["This is Delhi \n", "This is Paris \n", "This is London \n","This is korea\n"] 
with open("myfile.txt", "w") as file1:
	file1.write("Hello \n")
	file1.writelines(t) 
with open("myfile.txt", 'a') as file1: 
	file1.write("Today") 
with open("myfile.txt", "r+") as file1: 
	print(file1.read())
