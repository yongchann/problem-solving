def solution(sizes):
    for size in sizes:
        size.sort()
        
    widths = list(zip(*sizes))[0]
    heights = list(zip(*sizes))[1]
    return max(widths) * max(heights)