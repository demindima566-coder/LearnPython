def min_del(n):
    for div in range(2, n+1):
        if n % div == 0:
            return div

n = int(input())
res =  int(min_del(n))
print(res)