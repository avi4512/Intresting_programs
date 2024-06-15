n = int(input("Enter the number:"))
result = 0
a_n = abs(n)
n_s = str(a_n)
while a_n >= 10:
    for i in n_s:
        result = result + int(i)
    a_n = result
    n_s = str(result)
    result = 0
if n < 0:
    main_ans = -a_n
else:
    main_ans = a_n
print(main_ans)
