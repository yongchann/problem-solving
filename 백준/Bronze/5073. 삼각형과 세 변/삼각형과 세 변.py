while True:
    legs = sorted(list(map(int, input().split())))
    if not all(legs):
        break
    if legs[0] + legs[1] <= legs[2]:
        print('Invalid')
    elif len(set(legs)) == 1:
        print('Equilateral')
    elif len(set(legs)) == 2:
        print('Isosceles')
    elif len(set(legs)) == 3:
        print('Scalene')
