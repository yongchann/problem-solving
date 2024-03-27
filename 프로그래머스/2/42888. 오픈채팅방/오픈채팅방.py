from collections import defaultdict

def solution(records):
    answer = []
    uids = defaultdict(str)
    
    for record in records:
        cmd = record.split()
        if cmd[0] == 'Enter':
            uids[cmd[1]] = cmd[2]
            answer.append(cmd[1]+"님이 들어왔습니다.")
        elif cmd[0] == 'Leave':
            answer.append(cmd[1]+"님이 나갔습니다.")
        elif cmd[0] == 'Change':
            uids[cmd[1]] = cmd[2]
            
    for i in range(len(answer)):
        uid = answer[i].split("님이")[0]
        answer[i] = answer[i].replace(uid, uids[uid])
        
    return answer