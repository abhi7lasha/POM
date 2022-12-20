print("hello world")

# here are the comments

a = 3
print(a)

Str = "Hello"
print(Str)

b, c, d = 5, 6.4, "Great"
print(b, c, d)

# print("Value i"+b)

print("{} {}".format("Value is", b))
print(type(b))
print(type(c))
print(type(d))

# list demo

values = [1, 2, "rahul", 4, 5]
print(values[0])
print(values[2])
print(values[-1])
print(values[1:4])
print(values[2:])
print(values[:3])
values.insert(3, "shetty")  # insert
print(values)
values.append("End")  # add at last
print(values)

values[2] = "RAHUL"  # update
print(values)

del values[0]  # delete
print(values)

# tuple demo

val = (1, 2, "rahul", 4.5)
print(val[1])
# val[2] ="RAHUL"
print(val)

# dictionary demo
dic = {1: "value", "a": 1, "c": "Hello world"}
print(dic[1])
print(dic["c"])

#adding value in dictionary in run time
dict = {}
dict["firstname"] = "Rahul"
dict["last name"] = "shetty"
print(dict)
dict["Gender"] = "Male"
print(dict)



