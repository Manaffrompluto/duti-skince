i1 = int(input("Enter a number to proceed: "))
f = False
for i in range(2, i1):
    if i1 % i==0:
        f = False
        break
    else:
        f = True
        break
if f==False:
    print("This is not a prime number.")
if f==True:
    print("This is a prime number.")