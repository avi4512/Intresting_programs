def sum_digit(n):
    result = 0
    while n != 0:
        rem = n % 10
        result = result + rem
        n = n // 10
    return result
def single_sum(n):
    while n > 9:
        n = sum_digit(n)
    return n

n = 123456
r = single_sum(n)
print(r)
