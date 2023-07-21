import json
from pprint import pprint


def artist_info(artists, genres):
    artist_info_list = []
    for artist in artists:
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

        artist_info_list.append(art_dict)

    return artist_info_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
