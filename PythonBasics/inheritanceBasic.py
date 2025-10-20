from PythonBasics.basicOOP import class1


class class1Child(class1):
    num2=200

    def __init__(self):
        class1.__init__(self, 2, 10)
    def getData2(self):
        return self.num1 + self.num2 + self.summation()

obj=class1Child()
print(obj.getData2())
