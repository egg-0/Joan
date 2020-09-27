import requests
import time

def leaderboard(n=None):
    if n == None:
        n = 1

    response = requests.get('https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count={}'.format(n))

    # print(type(data.content))
    # print(data.content)

    as_json = response.json()

    leaders = as_json["leaderboard"]

    print(leaders)
    print(type(leaders))

    response = ''

    for leader in leaders:
        print(type(leader))
        response += "Rank {} - {} ({})\n".format(leader["rank"],leader["name"],leader["rating"])

    return response

def rating_history(player_ID,n=None):
    if n == None:
        n = 10

    req_string = 'https://aoe2.net/api/player/matches?game=aoe2de&steam_id={}&count={}'.format(player_ID,n)

    req_string = 'https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&steam_id={}&count={}'.format(player_ID,n)

    print(req_string)

    data = requests.get(req_string).json()

    response = ""
    for dict in data:
        response += "Rating: {}\n".format(dict["rating"])

    #print("as_json is {}".format(as_json))

    #leaders = as_json["leaderboard"]

    #print("the response is {}".format(as_json))

    return response

def game_data(game_id):

    all_civs = ['Aztecs','Berbers','Britons','Bulgarians','Burmese','Byzantines','Celts','Chinese','Cumans','Ethiopians',
                'Franks','Goths','Huns','Incas','Indians','Italians','Japanese','Khmer','Koreans','Lithuanians','Magyars',
                'Malay','Malians','Mayans','Mongols','Persians','Portuguese','Saracens','Slavs','Spanish','Tatars',
                'Teutons','Turks','Vietnamese','Vikings']

    req_string = "https://aoe2.net/api/match?id={}".format(game_id)

    req_attempt = requests.get(req_string)

    print("req_attempt is {}".format(req_attempt))

    if '404' in str(req_attempt):
        print("404 detected")
        return "Error: 404 request"

    data = req_attempt.json()

    print(data)

    player_data = data["players"]

    response = ""

    current_time = time.time()


    if data['started'] == None:
        response = "The game has not started"

    elif data['finished'] == None:

        elapsed = int(current_time) - int(data['started'])

        #response += "The game is in progress\n"
        response += "It has been {} minutes since start of game\n".format(round((elapsed/60)+12)) # 12 minute delay to aoe2.net
        response += "The players are:\n"
        for player in player_data:
            response += "{} ({})\n".format(player["name"],all_civs[int(player["civ"])])

    else:

        elapsed = int(data['finished'] - int(data['started']))

        #response += "The game is finished\n"
        response += "The game lasted {} minutes\n".format(round(elapsed/60))
        for player in player_data:
            player_name = player["name"]

            if player["won"]:
                result = "won"
            elif player["won"] == None:
                result = "unknown result"
            elif player["won"] == False:
                result = "lost"

            civ = all_civs[int(player["civ"])]

            response += f"{player_name} ({civ}): {result}\n"

    return response

if __name__ == '__main__':
    #leaderboard()
    response = game_data(40121145)
    print(response)