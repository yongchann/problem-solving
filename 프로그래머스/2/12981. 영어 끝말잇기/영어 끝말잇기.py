from collections import deque

def solution(n, words):
    # 초기화
    players = {i:0 for i in range(1, n+1)}
    words, exist = deque(words), set()
    
    who, word = 1, words.popleft()
    players[who] += 1
    exist.add(word)
    
    while words:
        who = who % n + 1
        players[who] += 1
        
        new_word = words.popleft()
        
        if word[-1] != new_word[0] or new_word in exist:
            return [who, players[who]]
            
        word = new_word
        exist.add(word)
        
    return [0, 0]
