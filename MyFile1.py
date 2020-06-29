file1 = open("MyFile.txt")
open("MyFile.txt")
number_of_lines = 1
for i in range(number_of_lines):
	print("the first number_of_lines lines of file1")
	line = file1.readline() 
print(line)