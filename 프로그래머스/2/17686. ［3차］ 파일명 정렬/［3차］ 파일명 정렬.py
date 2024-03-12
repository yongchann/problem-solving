def solution(files):
    data = [(idx, detail_of(file), file) for idx, file in enumerate(files)] 
    tmp = sorted(data, key=lambda x : (x[1][0].upper(), x[1][1], x[0]))
    _, _, c = zip(*tmp)
    return list(c)

def detail_of(file):
    ret = ["","",""]
    
    while file and (file[0].isalpha() or file[0] in [' ', '.', '-']):
        ret[0] += file[0]
        file = file[1:]
        
    while file and file[0].isdigit() and len(ret[1]) < 5:
        ret[1] += file[0]
        file = file[1:]
        
    ret[2] = file
    ret[1] = ret[1].zfill(5)
    
    return ret
        
