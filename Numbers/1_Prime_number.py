n = int(input("Enter the number:"))
flag = False

if n < 0:
    print("Negative numbers are not consider..")

elif n == 1:
    print("Its is not a Prime number")

elif n > 1:
    for i in range(2,n):
        if n % i == 0:
            flag = True
            break
    if flag:
        print("Its is not a prime")
    else:
        print("It is a Prime Number")

