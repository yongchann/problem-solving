def solution(brown, yellow):
    # yellow 를 소인수 분해     
    divisors = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            divisors.append(i)
            divisors.append(yellow//i)
            
    divisors = sorted(list(set(divisors)))
    
    while divisors:
        h = divisors[:1][0]
        w = divisors[-1:][0]
        
        if brown == 2 * (h+w) + 4:
            return [w+2, h+2]
        
        divisors = divisors[1:-1]
    
