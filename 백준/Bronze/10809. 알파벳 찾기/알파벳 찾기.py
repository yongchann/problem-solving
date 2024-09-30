s = input()
alphas = [chr(x) for x in range(ord('a'), ord('z')+1)]
for alpha in alphas:
    print(s.find(alpha), end=' ')