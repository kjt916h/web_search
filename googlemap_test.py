import googlemaps
from dotenv import load_dotenv
import sys
import os
import pprint
import heartrails_json
load_dotenv()

def create_shopinfo(index, result):
    print("""------ No. {} ------
【店名】 {}
【営業情報】 {}
【住所】 {}""".format(index+1, # No.
                        result["results"][index]["name"], # 店名
                        isopen(result["results"][index]),
                        result["results"][index]["vicinity"]
                        ))

def info_output(index, result):
    return """------ No. {} ------
【店名】 {}
【営業情報】 {}
【住所】 {}""".format(index+1, # No.
                        result["results"][index]["name"], # 店名
                        isopen(result["results"][index]),
                        result["results"][index]["vicinity"]
                        )

def isopen(search_result):
    if (search_result.get('opening_hours', None) == None):
        return "営業情報が存在しません"
    elif(search_result["opening_hours"]["open_now"] == True):
        return "営業中"
    else:
        return "営業時間外"

def search(place, type, distance=200):
    key = os.environ.get('GOOGLE_API_KEY') # 上記で作成したAPIキーを入れる
    client = googlemaps.Client(key) #インスタンス生成
    geocode_result = client.geocode(place)
    loc = geocode_result[0]['geometry']['location'] # 軽度・緯度の情報のみ取り出す
    s = "" #string
    if type == "food":
        place_result = client.places_nearby(location=loc, radius=distance, type='restaurant') #半径200m以内のレストランの情報を取得
        search_num = len(place_result["results"])

        for index in range(search_num):
            s += info_output(index, place_result)
            s += "\n"

        return s
    else:
        return heartrails_json.info_search(loc, s)

def main():
    key = os.environ.get("GOOGLE_API_KEY") #上記で作成したAPIキーを入れる
    client = googlemaps.Client(key) #インスタンス生成
    num_of_val = len(sys.argv)
    geocode_result = client.geocode(sys.argv[1])
    loc = geocode_result[0]['geometry']['location'] # 軽度・緯度の情報のみ取り出す
    #print(loc['lat']) #緯度
    #print(loc['lng']) #経度
    #print(loc)
    breakpoint()
    if (num_of_val >= 3 and sys.argv[2] == "food"):
        place_result = client.places_nearby(location=loc, radius=200, type='restaurant') #半径200m以内のレストランの情報を取得
        search_num = len(place_result["results"])

        for index in range(search_num):
            create_shopinfo(index, place_result)
    else:
        heartrails_json.heartrailsAPI(loc)

if __name__ == "__main__":
    main()