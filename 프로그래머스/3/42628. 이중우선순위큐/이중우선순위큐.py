from bisect import insort

def solution(operations):
    l = []
    for op in operations:
        cmd, value = op.split()
        if cmd == 'I':
            insort(l, int(value))
        elif cmd == 'D' and value == '-1':
            l = l[1:]
        elif cmd == 'D' and value == '1':
            l = l[:-1]
    
    if not l:
        return [0, 0]
    else :
        return [l[-1], l[0]]