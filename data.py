N= input("Enter your name: ")
A= int(input("Enter your age: "))
M= input("Enter your mobile number: ")

if N.isalpha()== True:
    print(N)
if A>18:
    print(A)
if M.isdigit()==True:
    print(M)

else:
    print("invalid input")