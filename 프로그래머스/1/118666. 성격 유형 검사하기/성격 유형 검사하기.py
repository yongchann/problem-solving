def solution(survey, choices):
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        check = choices[i] - 4
        if check < 0:
            score[survey[i][0]] += abs(check)
        else:
            score[survey[i][1]] += abs(check)

    def get_dominant_type(type1, type2):
        return type1 if score[type1] >= score[type2] else type2

    types = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    type_score = [get_dominant_type(t1, t2) for t1, t2 in types]
    
    return ''.join(type_score)
