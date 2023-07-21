import json
from pprint import pprint


def artist_info(artist, genres):
    art_dict = {}
    art_dict["id"] = artist["id"]
    art_dict["name"] = artist["name"]
    art_dict["genres_name"] = artist["genres_ids"]
    art_dict["images"] = artist["images"]
    art_dict["type"] = artist["type"]

    genres_list = []

    for genres_id in art_dict["genres_name"]:
        for genre in genres:
            if genres_id == genre["id"]:
                genres_list.append(genre["name"])
    
    art_dict["genres_name"] = genres_list

    return art_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
