from OopDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    #child constructor
    def __init__(self):
        #call parent constructor
        Calculator.__init__(self, 2, 10)

    #method
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

#object
obj = ChildImpl()
print(obj.getCompleteData())

