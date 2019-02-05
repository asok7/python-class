def add(x,y):
    return(x+y)
def subtract(x,y):
  return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)

a = input("enter the operation(+,*,/,-):  ")
n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
if a== '+':
    print(n1,"+",n2,"=",add(n1,n2))
elif a== '-':
    print(n1, "-", n2, "=",subtract(n1, n2))
elif a== '*':
    print(n1, "*", n2, "=",multiply(n1, n2))
elif a== '/':
    print(n1, "/", n2, "=",divide(n1, n2))
else:
    print("invalid string")