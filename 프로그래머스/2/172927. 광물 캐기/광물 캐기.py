import heapq

def solution(picks, minerals):
    answer = 0

    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks)*5]
        
    picks = ["stone"]*picks[2] + ["iron"]*picks[1] + ["diamond"]*picks[0]
    info = {
        "diamond":{"diamond":1, "iron":1, "stone":1},
        "iron":{"diamond":5, "iron":1, "stone":1},
        "stone":{"diamond":25, "iron":5, "stone":1}
    }
    
    # 5개 단위로 묶음
    bulks = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    
    # 묶음별 가중치 합 오름차순 정렬
    bulks.sort(key=lambda x : sum(info["stone"][i] for i in x))
    
    # 가중치가 가장 높은 묶음에 상위 곡괭이 사용
    while bulks and picks:
        bulk = bulks.pop()
        pick = picks.pop()
    
        for b in bulk:
            answer += info[pick][b]
    
    return answer
