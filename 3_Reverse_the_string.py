n = "Avinash Reddy"

#1.Reverse of string using index

rn1 = n[::-1]
print(rn1)


#2.Reverse the string using join and reverse inbuilt function
rn2 = "".join(reversed(n))
print(rn2)

#3.Reverse the string using loop
rn3 = ""
l = len(n)
for i in range(l-1,-1,-1):
    rn3 = rn3 + n[i]

print(rn3)



