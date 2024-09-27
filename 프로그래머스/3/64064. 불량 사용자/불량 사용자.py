from itertools import permutations

def check(plain, mask):
    if len(plain) != len(mask):
        return False
    
    for i in range(len(plain)):
        if plain[i] != mask[i] and mask[i] != '*':
            return False
    return True

def solution(uids, bids):
    temp = []
    for _uids in permutations(uids, len(bids)):
        valid = True
        for plain, mask in list(zip(_uids, bids)):
            if not check(plain, mask):
                valid = False
        if valid:
            temp.append(_uids)
        
    return len(list(set(tuple(sorted(i)) for i in temp)))