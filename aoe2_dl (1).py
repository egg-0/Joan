import requests

def main():

    url = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=10000"

    response = requests.get(url)

    as_json = response.json()

    leaders = as_json["leaderboard"]

    print(leaders)

if __name__=="__main__":
    main()

