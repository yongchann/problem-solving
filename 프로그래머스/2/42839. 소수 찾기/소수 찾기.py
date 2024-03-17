from itertools import permutations

def solution(numbers):
    answer = 0
    nums = set()
    
    for digit in range(1, len(numbers)+1):
        nums |= set([int("".join(num)) for num in permutations(numbers, digit)])
    print(nums)
    return len([num for num in nums if isPrime(num)])

        
def isPrime(n):
    if n  < 2: return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True
        