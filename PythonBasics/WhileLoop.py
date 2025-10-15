age = 1

while age<10:
    if age == 3:
        print("Continue Executed")
        age = age + 1
        continue
    if age == 9:
        print("Break Executed")
        break
    print(age)
    age = age+1


print("Execution Done")