def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 유효한 위치만 인덱스와 함께 관리
    deliveries = [[i+1, deliveries[i]] for i in range(n) if deliveries[i] != 0]
    pickups = [[i+1, pickups[i]] for i in range(n) if pickups[i] != 0]
    
    while True:
        # 왕복 거리 확인 또는 탈출
        dist = 0
        if deliveries:
            dist = max(dist, deliveries[-1][0])
        if pickups:
            dist = max(dist, pickups[-1][0])
            
        if dist == 0:
            break
        
        answer += dist*2
        
        # 최대 배달
        delivery_cnt = 0
        while deliveries and delivery_cnt < cap:
            # 다 담을 수 있는 경우
            if deliveries[-1][1] <= (cap - delivery_cnt):
                delivery_cnt += deliveries[-1][1]
                deliveries.pop()
            else:
                deliveries[-1][1] -= (cap - delivery_cnt)
                delivery_cnt = cap
        
        # 최대 수거
        pickup_cnt = 0
        while pickups and pickup_cnt < cap:
            # 다 담을 수 있는 경우
            if pickups[-1][1] <= (cap - pickup_cnt):
                pickup_cnt += pickups[-1][1]
                pickups.pop()
            else:
                pickups[-1][1] -= (cap - pickup_cnt)
                pickup_cnt = cap
    
    return answer

