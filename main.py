def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, r):
    if (n > r) and (n > 0) and (r > -1):
        n = int(n)
        r = int(r)
    return factorial(n) / (factorial(r) * factorial((n - r)))


print(combination(7, 3))
