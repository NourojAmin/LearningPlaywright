class Calculator:
    num1 = 100

    def getData(self):
        print("Method Executed from Class")

obj = Calculator()
obj.getData()
print(obj.num1)