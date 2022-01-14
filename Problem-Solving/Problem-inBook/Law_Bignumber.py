n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
numBig1 = data[n - 1]
numBig2 = data[n - 2]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += numBig1
        m -= 1
    if m == 0:
        break
    result += numBig2
    m -= 1

print(result)