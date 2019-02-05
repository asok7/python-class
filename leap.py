Y=int(input('enter a year: '))

if Y % 400 == 0:
    print("leap year")
elif Y % 100 == 0:
    print("not leap year")
elif Y % 4 == 0:
    print("leap year")
else:
    print("not leap year")


