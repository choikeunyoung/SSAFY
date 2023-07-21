import json
from pprint import pprint


def artist_info(artist):
    art_dict = {}
    art_dict["id"] = artist["id"]
    art_dict["name"] = artist["name"]
    art_dict["genres_ids"] = artist["genres_ids"]
    art_dict["images"] = artist["images"]
    art_dict["type"] = artist["type"]
    
    return art_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)
    
    pprint(artist_info(artist_dict))
