for _ in range(int(input())):
    iter_cnt, charset = input().split()
    for char in charset:
        print(int(iter_cnt) * char, end='')
    print()