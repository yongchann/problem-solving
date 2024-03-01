def solution(n):
    bin_n = bin(n)[2:].zfill(20)

    # 오른쪽부터 탐색하여 처음 등장한 '01' -> '10' 으로 수정
    pos = bin_n.rfind('01')
    lbin = list(bin_n)
    lbin[pos], lbin[pos+1] = '1', '0'
    
    next_bin = ''.join(lbin[:pos+2] + sorted(lbin[pos+2:]))
    return int(next_bin, 2)

