pils = [0] * 1001
for i in range(int(input())):
    pos, height = map(int, input().split())
    pils[pos] = height

max_pos = pils.index(max(pils))
answer = 0
curr = 0
for i in range(max_pos+1):
    curr = max(curr, pils[i])
    answer += curr

curr = 0
for i in range(1000, max_pos, -1):
    curr = max(curr, pils[i])
    answer += curr

print(answer)