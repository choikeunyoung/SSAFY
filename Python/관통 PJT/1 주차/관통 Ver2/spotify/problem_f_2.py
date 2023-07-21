"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint


def acoustic_artists(artists, genres):
    genre_id = 0
    for genre in genres:
        if genre["name"] == "acoustic":
            genre_id = genre["id"]
    
    artists_name = []

    for artist in artists:
        if genre_id in artist["genres_ids"]:
            artists_name.append(artist["name"])
    
    return artists_name


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    genres_data = open("data/genres.json", encoding="utf-8")
    genres_data = json.load(genres_data)

    artists_data = open("data/artists.json", encoding="utf-8")
    artists_data = json.load(artists_data)

    pprint(acoustic_artists(artists_data, genres_data))
