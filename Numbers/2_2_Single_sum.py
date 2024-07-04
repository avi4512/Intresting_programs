n = int(input("Enter the number:"))
result = 0
a_n = abs(n)   #convertinf negative to positive number
n_s = str(a_n) #converting int to string
while a_n > 9:
    for i in n_s:
        result = result + int(i)
    a_n = result       #upating a_n as result fro next iteration 
    n_s = str(result)  #again chaging the int to string
    result = 0         #For next iterstion chaning result as 0
if n < 0:
    main_ans = -a_n
else:
    main_ans = a_n
print(main_ans)
