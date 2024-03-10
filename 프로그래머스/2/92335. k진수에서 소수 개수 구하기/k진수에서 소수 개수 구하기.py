def solution(n, k):
    my_num = to_n_base(n, k)
    nums = [int(i) for i in my_num.split('0') if len(i) != 0]
    
    return len([num for num in nums if isPrime(num) and num >=2])

def to_n_base(n, k):
    tmp = ""
    while n:
        n, b = divmod(n, k)
        tmp += str(b) 
        
    return tmp[::-1]    


def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        