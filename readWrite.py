file = open('test.txt')
#read by index
#print(file.read(5))
#read line wise
#print(file.readline())
#print(file.readline())



#print line by line using readline method
#line = file.readline()
#while line!= "":
#    print(line)
#    line = file.readline()

#print(file.readlines())
for line in file.readlines():
    print(line)

file.close()