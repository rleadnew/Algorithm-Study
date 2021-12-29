def fibonacci(k):
    if k == 1 or k == 2:
        return 1
    return fibonacci(k -1) + fibonacci(k - 2) #재귀함수 사용

print(fibonacci(6))
