def fibonacci(k):
    if k == 1 or k == 2:
        return 1
    return fibonacci(k -1) + fibonacci(k - 2)

print(fibonacci(6))