def solution(records):
    answer = []
    uids = {record.split()[1]: record.split()[2] for record in records if record.split()[0] != 'Leave'}
    
    for record in records:
        log = record.split()
        if log[0] == "Enter":
            answer.append(uids[log[1]]+'님이 들어왔습니다.')     
        elif log[0] == 'Leave':
            answer.append(uids[log[1]]+'님이 나갔습니다.')     
    return answer
