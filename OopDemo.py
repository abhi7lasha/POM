#class
class Calculator:
    num = 100

    #default constructor
    def __init__(self,a,b):
        self.firstNum= a
        self.secondNum= b
        print("I am called automatically when object is created")


    #method
    def getData(self):
        print("I am now executing as method in class.")

    def Summation(self):
        return self.firstNum + self.secondNum + Calculator.num




#object
obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.Summation())

