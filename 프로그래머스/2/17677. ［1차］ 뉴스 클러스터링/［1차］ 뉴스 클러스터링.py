from collections import Counter

def solution(str1, str2):
    counter_of_str1 = Counter([str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    counter_of_str2 = Counter([str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()])
    
    val1 = sum((counter_of_str1 & counter_of_str2).values())
    val2 = sum((counter_of_str1 | counter_of_str2).values())
    
    if val2 == 0:
        return 65536
    else:
        return int(val1 / val2 * 65536)
    
    
        

    
    
    
    
    
    
