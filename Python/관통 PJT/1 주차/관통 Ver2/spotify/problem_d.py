import json


def max_revenue(artists):
    art_dict = {}
    for artist in artists:
        art_id = artist["id"]
        art_id_popular = open(f'data/artists/{art_id}.json', encoding="utf-8")
        art_id_popular = json.load(art_id_popular)

        art_dict[art_id] = (art_id_popular["name"], art_id_popular["popularity"])

    max_id = 0
    max_popular = 0

    for k, v in art_dict.items():
        if v[1] > max_popular:
            max_id = k
            max_popular = v[1]
    
    return art_dict[max_id][0]

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(max_revenue(artists_list))
