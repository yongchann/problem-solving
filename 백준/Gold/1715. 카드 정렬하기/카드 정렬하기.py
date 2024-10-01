from heapq import heappop, heappush, heapify
nums = [int(input()) for _ in range(int(input()))]
heapify(nums)

answer = 0
while len(nums)>= 2:
    m = heappop(nums)
    n = heappop(nums)
    heappush(nums, m+n)
    answer += (m+n)
print(answer)