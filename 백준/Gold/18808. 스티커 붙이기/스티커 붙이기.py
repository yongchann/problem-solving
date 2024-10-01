def rotate_sticker(sticker):
    return list(zip(*sticker[::-1]))

def place_sticker(notebook, sticker, start_i, start_j):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                ni, nj = start_i + i, start_j + j
                if ni >= n or nj >= m or notebook[ni][nj]:
                    return False
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                notebook[start_i + i][start_j + j] = 1
    return True

n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]
sticker_count = 0

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    
    for _ in range(4):
        placed = False
        for i in range(n - len(sticker) + 1):
            if placed:
                break
            for j in range(m - len(sticker[0]) + 1):
                if place_sticker(notebook, sticker, i, j):
                    placed = True
                    sticker_count += sum(row.count(1) for row in sticker)
                    break
        if placed:
            break
        sticker = rotate_sticker(sticker)

print(sticker_count)