file = open('test.txt')
print(file.readline())
print(file.read(4))

line = file.readline()
while line!="":
    print(line)
    line = file.readline()

file.close()