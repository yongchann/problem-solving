def solution(arr):
    return [x for x, y in zip(arr, [None] + arr) if x != y]