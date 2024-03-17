def solution(arr):
    answer = []
    while arr:
        item = arr.pop()
        if len(answer) == 0 or answer[-1] != item:
            answer.append(item)

    return answer[::-1]