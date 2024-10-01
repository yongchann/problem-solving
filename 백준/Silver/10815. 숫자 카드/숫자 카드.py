_ = int(input())
s = set(map(int, input().split()))
_ = int(input())
l = list(map(int, input().split()))
for i in l:
    print(1 if i in s else 0, end=' ')
