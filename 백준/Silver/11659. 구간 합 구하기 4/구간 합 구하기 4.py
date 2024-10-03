import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
p_sums = [0]

for i in range(1, n+1):
    p_sums.append(p_sums[-1] + arr[i-1])

for _ in range(m):
    start, end = map(int, input().split())
    print(p_sums[end] - p_sums[start-1])