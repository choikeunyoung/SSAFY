"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular(artists):

    art_dict = {}
    for artist in artists:
        art_id = artist["id"]
        art_id_popular = open(f'data/artists/{art_id}.json', encoding="utf-8")
        art_id_popular = json.load(art_id_popular)
        art_dict[art_id] = (art_id_popular["name"], art_id_popular["followers"] , art_id_popular["uri"].split(":"))
    
    return_list = []

    for art_detail in art_dict.values():
        if art_detail[1]["total"] >= 5000000 and art_detail[1]["total"] < 10000000:
            return_artist = {}
            return_artist["name"] = art_detail[0]
            return_artist["followers"] = art_detail[1]["total"]
            return_list.append(return_artist)

    return return_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    pprint(get_popular(artists_list))