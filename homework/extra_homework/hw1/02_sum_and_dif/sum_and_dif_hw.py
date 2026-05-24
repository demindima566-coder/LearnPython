def digits_sum_v1(n):
    kol = 0
    while n > 0:
        kol += n % 10
        n //= 10
    return  kol

def digits_sum_v2(n):
    kol = 0
    for digit in str(n):
        kol += int(digit)
    return kol

def digits_count_v1(n):
    kol = 0
    while n > 0:
        kol += 1
        n //= 10
    return kol

def digits_count_v2(n):
    return len(str(n))

n = int(input())

summa1 = digits_sum_v1(n)
summa2 = digits_sum_v2(n)

count1 = digits_count_v1(n)
count2 = digits_count_v2(n)

print("sum -", summa1, "or", summa2)
print("count -", count1, "or", count2)
print("sum-count", summa1 - count1, "or", summa2 - count2)