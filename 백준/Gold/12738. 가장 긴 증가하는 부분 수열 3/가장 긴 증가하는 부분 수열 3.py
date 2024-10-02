from bisect import bisect_left
_ = int(input())
nums = list(map(int, input().split()))

arr = [-float('inf')]
for num in nums:
    if arr[-1] < num:
        arr.append(num)
    else:
        idx = bisect_left(arr, num)
        arr[idx] = num
print(len(arr)-1)
        