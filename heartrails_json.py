import sys
import urllib.request
import urllib.parse
import json

def create_station_info(index, station):
    return """------ No, {} ------
【駅名】 {}
【路線名】 {}
【現在地からの距離】 {}""".format(index,
                                    station["name"], #駅名
                                    station["line"], #路線名
                                    station["distance"] #現在地からの距離
                                )


def main():
    url = "http://express.heartrails.com/api/json?{}".format(
        urllib.parse.urlencode(
            {"method" : "getStations",
             "y" : "".join(sys.argv[1]),   # 入力からクエリを生成
             "x" : "".join(sys.argv[2]),   # 入力からクエリを生成
            }))
    #print("URL:",url)
    f_url = urllib.request.urlopen(url).read()
    json_result = json.loads(f_url.decode("utf-8"))

    #output
    print("最寄り駅の一覧を表示します。")
    for index, station in enumerate(json_result["response"]["station"]):
        print(create_station_info(index+1, station))

def heartrailsAPI(loc):
    url = "http://express.heartrails.com/api/json?{}".format(
        urllib.parse.urlencode(
            {"method" : "getStations",
             "x" : loc['lng'],   # 入力からクエリを生成(経度)
             "y" : loc['lat'],   # 入力からクエリを生成(緯度)
            }))
    #print("URL:",url)
    f_url = urllib.request.urlopen(url).read()
    json_result = json.loads(f_url.decode("utf-8"))

    #output
    print("最寄り駅の一覧を表示します。")
    for index, station in enumerate(json_result["response"]["station"]):
        print(create_station_info(index+1, station))

def info_search(loc, s):
    url = "http://express.heartrails.com/api/json?{}".format(
        urllib.parse.urlencode(
            {"method" : "getStations",
             "x" : loc['lng'],   # 入力からクエリを生成
             "y" : loc['lat'],   # 入力からクエリを生成
            }))
    #print("URL:",url)
    f_url = urllib.request.urlopen(url).read()
    json_result = json.loads(f_url.decode("utf-8"))

    #output
    for index, station in enumerate(json_result["response"]["station"]):
        s += create_station_info(index+1, station)
        s += "\n"
    
    return s

if __name__ == "__main__":
    main()