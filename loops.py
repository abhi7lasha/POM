# if-else condition
greeting = "Good Morning"
a = 4
if a > 2:
    print("condition matches")
else:
    print("don't matches")
print("if-else condition code is completed")

# for loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i * 2)
    print(i)

# sum of first natural number 1+2+3+4+5
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("*******************************")

for k in range(1, 10, 5):
    print(k)
print("*******************************")
for m in range(10):
    print(m)
print("*******************************")
# while loop

it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1
print("while loop execution is done")

# function demo


print("function demo")


def greetme(name):
    print("Good Morning" + name)


def AddIntegers(a, b):
    return a + b


greetme("Abhilasha")


print(AddIntegers(2, 3))
