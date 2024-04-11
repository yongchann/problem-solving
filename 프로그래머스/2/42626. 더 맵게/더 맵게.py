from heapq import heappush, heappop, heapify

def solution(scoville, k):
    cnt = 0
    heapify(scoville)
    
    while True:
        if scoville[0] >= k:
            break
        if len(scoville) < 2:
            cnt = -1
            break
    
        # 두개 꺼내서 합치기
        s1, s2 = heappop(scoville), heappop(scoville)
        heappush(scoville, s1 + (s2*2))
        cnt += 1
    
    return cnt    
