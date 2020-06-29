file1=open("MyFile.txt","r")
with open('MyFile.txt') as f:
  last = None
  for line in (line for line in f if line.rstrip('\n')):
    last = line
print(last)
