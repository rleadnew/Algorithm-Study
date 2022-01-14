import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
numBig1 = data[n - 1]
numBig2 = data[n - 2]

count = (m // (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * numBig1
result += (m - count) * numBig2

print(result)