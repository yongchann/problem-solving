from itertools import product

def solution(users, emoticons):
    max_join_count, max_sale_amount = 0, 0
    
    # 각 이모티콘에 적용할 할인율 모든 케이스 탐색
    for disc in product([10, 20, 30, 40], repeat=len(emoticons)):
        # 각 케이스별 [가입자 수, 판매액]
        join_count, sale_amount = 0, 0
        
        for sale_std, join_std in users:
            # 할인율 기준에 따라 구매한 총 구매 가격
            tmp_price_sum = sum([(emoticons[i] * (100-disc[i])) // 100 for i in range(len(emoticons)) if disc[i] >= sale_std])
            
            # (총 구매 가격, 이모티콘 플러스 가입 기준가격) 비교하여 처리
            if tmp_price_sum >= join_std:
                join_count += 1
            else:
                sale_amount += tmp_price_sum
        
        # 우선순위 1: 최대 가입자 수
        if join_count > max_join_count:
            max_join_count = join_count
            max_sale_amount = sale_amount
        # 우선순위 2: 최대 판매액
        elif join_count == max_join_count:
            max_sale_amount = max(max_sale_amount, sale_amount)
        else:
            continue

    return [max_join_count, max_sale_amount]