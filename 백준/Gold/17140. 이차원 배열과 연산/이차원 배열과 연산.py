from collections import Counter

def op_r(arr):
    #각 행을 카운트해서 (등장횟수, 수) 기준으로 정렬 
    for i, row in enumerate(arr):
        row_data = sorted([(k, v) for k, v in Counter(row).items() if k], key=lambda x: (x[1], x[0]))
        arr[i] = [item for kv in row_data for item in kv][:50]
    
    max_length = len(max(arr, key=lambda x: len(x)))
    for i in range(len(arr)):
        if len(arr[i]) < max_length:
            arr[i] += [0]*(max_length-len(arr[i]))
    return arr
            
def op_c(arr):
    tarr = list(map(list, zip(*arr)))
    return list(map(list, zip(*op_r(tarr))))

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

answer = -1
for i in range(101):
    if r-1<len(arr) and c-1<len(arr[0]):
        if arr[r-1][c-1] == k:
            answer = i
            break
    
    row, column = len(arr), len(arr[0])
    if row >= column:
        arr = op_r(arr)
    else:
        arr = op_c(arr)
    
print(answer)