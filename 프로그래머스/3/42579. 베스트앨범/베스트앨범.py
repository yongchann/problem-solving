from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # 장르별 노래 관리 (인덱스, 곡 별 재생 수)
    genre_song_dict = defaultdict(list)
    # 장르별 총 재생 수 관리
    genre_cnt_dict = defaultdict(int)
    
    for idx, song_info in enumerate(list(zip(genres, plays))):
        genre_song_dict[song_info[0]].append([idx, song_info[1]])
        genre_cnt_dict[song_info[0]] += song_info[1]
        

    # 조건 1. 속한 노래가 많이 재생된 장르 순
    ordered_genres = sorted(list(genre_cnt_dict.items()), key=lambda x: -x[1])
    for genre, _ in ordered_genres:
        # 조건 2+3. 장르 내에서 많이 재생된 노래 순(-x[1]), 동일한 경우 고유 번호 낮은 순(x[0])
        top_two_songs = sorted(genre_song_dict[genre], key=lambda x: (-x[1], x[0]))[:2]
        
        for song in top_two_songs:
            answer.append(song[0])
    
    return answer