class class1:
    num1 = 100

    def __init__(self,a,b):
        self.firstNum = a
        self.secondNum = b
        print("Default Constructor")

    def getData(self):
        print("Method Executed from Class")

    def summation(self):
        summation = self.firstNum + self.secondNum + class1.num1
        return summation

obj = class1(5,2)
obj.getData()
print(obj.num1)
print(obj.summation())

obj2 = class1(4,3)
obj2.getData()
print(obj2.num1)
print(obj2.summation())