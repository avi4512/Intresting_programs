def prime_range(lower,upper):
    count = 0

    for num in range(lower,upper+1):

        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(num,end=" ")
                count = count + 1
    print()
    print(f'count of prime numbers b/w the {lower} and {upper} is {count}')

l = int(input("Enter the lower:"))
u = int(input("Enter the upper:"))
prime_range(l,u)
