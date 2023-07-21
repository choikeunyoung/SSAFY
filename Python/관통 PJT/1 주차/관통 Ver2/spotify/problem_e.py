import json
from pprint import pprint as print

def dec_artists(artists):

    art_dict = {}
    for artist in artists:
        art_id = artist["id"]
        art_id_popular = open(f'data/artists/{art_id}.json', encoding="utf-8")
        art_id_popular = json.load(art_id_popular)
        art_dict[art_id] = (art_id_popular["name"], art_id_popular["followers"] , art_id_popular["uri"].split(":"))
    
    return_list = []

    for art_detail in art_dict.values():
        if art_detail[1]["total"] > 10000000:
            return_artist = {}
            return_artist["name"] = art_detail[0]
            return_artist["uri-id"] = art_detail[2][-1]
            return_list.append(return_artist)

    return return_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
