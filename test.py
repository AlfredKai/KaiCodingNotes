def fibonacci(n):
    if (n == 0):
        return 0

    a = 0
    b = 1

    for _ in range(2, n):
        c = a + b
        a = b
        b = c

    return c

print(fibonacci(5))
# 0 1 1 2 3