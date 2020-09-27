import itertools
import more_itertools
import statistics
import random
import re

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
    #return statistics.harmonic_mean(numbers)
    #return statistics.geometric_mean(numbers)


def read_rating(ID_list):

    # at present the input has to be a list of ratings not a single rating.

    ratings = []

    f = open("ratings.txt", "r")
    f_string = f.readlines()

    print("ID list is {}".format((ID_list)))
    print("length of ID list is {}".format(len(ID_list)))

    if len(ID_list) != 1:
        for ID in ID_list:
            for line in f_string:
                if line.startswith(ID):
                    #print("line is" + str(line))
                    #print("ID is " + str(ID))

                    rating = line.split(' ')[1]

                    print('rating is {}'.format(rating))
                    ratings.append(int(rating))
    else:
        ID = ID_list[0]
        for line in f_string:
            if line.startswith(ID):
                print("line is" + str(line))
                print("ID is " + str(ID))

                rating = line.split(' ')[1]
                ratings.append(int(rating))


    return ratings

def team_split(ID_list,index = None):

    if index == None:
        index = 0

    ratings = read_rating(ID_list)

    print('IDs are' + str(ID_list))
    print('ratings as' + str(ratings))

    num_teams = 2

    combinations = list(more_itertools.set_partitions(ratings, k=num_teams))
    combinations_ID = list(more_itertools.set_partitions(ID_list, k=num_teams))

    # only equal number of players

    combs = []
    IDs = []
    meanDifs = []
    for comb,ID in zip(combinations,combinations_ID):
        if len(comb[0]) == len(comb[1]):
            combs.append(comb)
            IDs.append(ID)
            meanDifs.append(abs(mean(comb[0]) - mean(comb[1])))

    print("The combinations are:" + str(combs))

    nCombs = len(combs)
    print("number of combinations is " + str(nCombs))

    print(meanDifs)

    sortedDifs = sorted(meanDifs)

    eloDif = sortedDifs[index]

    minInd = meanDifs.index(eloDif)

    #minDif = 999999
    #minInd = None
    #for i in range(nCombs):
    #    if meanDifs[i] < minDif:
    #        minDif = meanDifs[i]
    #        minInd = i

    print("min index is" + str(minInd))

    team_ratings = combs[minInd]
    team_IDs = IDs[minInd]

    # shuffle teams
    team_ID_shuffled = []
    team_ratings_shuffled = []
    for ID,rating in zip(team_IDs,team_ratings):
        z = list(zip(ID,rating))
        random.shuffle(z)
        ID, rating = zip(*z)
        team_ID_shuffled.append(ID)
        team_ratings_shuffled.append(rating)

    eloDif = int(mean(team_ratings_shuffled[1]) - mean(team_ratings_shuffled[0]))

    print("ELO difference is {}".format(eloDif))

    if abs(eloDif) < 40:
        civ_tier_1 = 2
        civ_tier_2 = 2
    if 40 <= eloDif < 80:
        civ_tier_1 = 2
        civ_tier_2 = 3
    if 80 <= eloDif < 120:
        civ_tier_1 = 1
        civ_tier_2 = 3
    if 120 <= eloDif < 150:
        civ_tier_1 = 1
        civ_tier_2 = 4
    if 150 <= eloDif:
        civ_tier_1 = 1
        civ_tier_2 = 5
    if -40 >= eloDif > -80:
        civ_tier_1 = 3
        civ_tier_2 = 2
    if -80 >= eloDif > -120:
        civ_tier_1 = 3
        civ_tier_2 = 1
    if -120 >= eloDif > -50:
        civ_tier_1 = 4
        civ_tier_2 = 1
    if -150 >= eloDif:
        civ_tier_1 = 5
        civ_tier_2 = 1

    civ_tiers = [civ_tier_1, civ_tier_2]

    response = ""

    i_team = 0
    i_player_start = 0
    for sub_team_ID, sub_team_rating, civ_tier in zip(team_ID_shuffled,team_ratings_shuffled,civ_tiers):
        i_player_start += 1
        i_player = i_player_start
        i_team += 1
        response += "TEAM {} - avg elo: {} (civ tier {})\n".format(i_team,round(mean(sub_team_rating)),civ_tier)
        for ID, iRating in zip(sub_team_ID,sub_team_rating):
            response += "P{}: <@!{}> ({})\n".format(i_player,ID,iRating)
            i_player += 2

        response += '\n'

    return response

if __name__ == "__main__":
    testID = ['756894700413124669', '756896304696918077', '756896832306675813', '756897278303666299']
    response = team_split(testID)
    print(response)


    """
    response += "P1: " + str(team1[0]) + " " + str(rating1[0]) + "\n"
    response += "P3: " + str(team1[1]) + " " + str(rating1[1]) + "\n"
    response += "P5: " + str(team1[2]) + " " + str(rating1[2]) + "\n"
    response += "P7: " + str(team1[3]) + " " + str(rating1[3]) + "\n"
    response += "" + "\n"
    response += "TEAM 2 - avg elo: " + str(rating_team2) + "\n"
    response += "P2: " + str(team2[0]) + " " + str(rating2[0]) + "\n"
    response += "P4: " + str(team2[1]) + " " + str(rating2[1]) + "\n"
    response += "P6: " + str(team2[2]) + " " + str(rating2[2]) + "\n"
    response += "P8: " + str(team2[3]) + " " + str(rating2[3]) + "\n"
    response += "" + "\n"
    response += "The elo difference is " + str(elo_dif)

    #print("average elo difference = " + str(closeness[index_min]))

    return response"""




    """
    # randomise positions
    half_n = num_players//2

    seed_list_1 = list(range(half_n))
    random.shuffle(seed_list_1)

    seed_list_2 = list(range(half_n))
    random.shuffle(seed_list_2)

    rating_team1 = mean(rating[:4])
    rating_team2 = mean(rating[4:])

    team1 = split[0:4]
    team2 = split[4:8]

    rating1 = rating[0:4]
    rating2 = rating[4:8]

    # then shuffle with predefined seeds
    team1 = [team1[i] for i in seed_list_1]
    team2 = [team2[i] for i in seed_list_2]

    rating1 = [rating1[i] for i in seed_list_1]
    rating2 = [rating2[i] for i in seed_list_2]

    elo_dif = abs(rating_team1-rating_team2)

    response = ""

    response += "TEAM 1 - avg elo: " + str(rating_team1) + "\n"
    response += "P1: " + str(team1[0]) + " " + str(rating1[0]) + "\n"
    response += "P3: " + str(team1[1]) + " " + str(rating1[1]) + "\n"
    response += "P5: " + str(team1[2]) + " " + str(rating1[2]) + "\n"
    response += "P7: " + str(team1[3]) + " " + str(rating1[3]) + "\n"
    response += "" + "\n"
    response += "TEAM 2 - avg elo: " + str(rating_team2) + "\n"
    response += "P2: " + str(team2[0]) + " " + str(rating2[0]) + "\n"
    response += "P4: " + str(team2[1]) + " " + str(rating2[1]) + "\n"
    response += "P6: " + str(team2[2]) + " " + str(rating2[2]) + "\n"
    response += "P8: " + str(team2[3]) + " " + str(rating2[3]) + "\n"
    response += "" + "\n"
    response += "The elo difference is " + str(elo_dif)

    #print("average elo difference = " + str(closeness[index_min]))

    return response"""


"""
    # match IDs back to ratings
    for team in team_ratings:
        ID_sub = []
        for rating in team_ratings:
            if rating == 
            ID_sub.append()"""



"""
def old_team_split(ID_list):

    ratings = read_rating(ID_list)

    # ratings
    boo = 1650
    egg = 1550
    flux = 1500
    jeroen = 1500
    young_panda = 1500
    ac = 1100
    hazza = 1100
    jude = 900
    coinhunter = 1200
    usha = 1300
    peace = 1000
    tyranny = 1200

    rating_dict = {}

    num_players = len(ID_list)


    for player in ID_list:
        rating_dict[player] = eval(player)

    iterations = list(itertools.permutations(rating_dict.values()))
    player_splits = list(itertools.permutations(rating_dict.keys()))

    closeness = []

    for item in iterations:
        closeness.append(abs(mean(item[:4]) - mean(item[4:])))


    minVal = min(closeness)
    print('min_elo is' + str(minVal))

    # iterate over possible minima

    index_of_possible_splits = []
    i = 0
    for val in closeness:
        if val == minVal:
            index_of_possible_splits.append(i)
        i += 1


    #index_min = min(range(len(closeness)), key=closeness.__getitem__)
    index_min = random.choice(index_of_possible_splits)



    rating = iterations[index_min]
    split = player_splits[index_min]

    # randomise positions
    half_n = num_players//2

    seed_list_1 = list(range(half_n))
    random.shuffle(seed_list_1)

    seed_list_2 = list(range(half_n))
    random.shuffle(seed_list_2)

    rating_team1 = mean(rating[:4])
    rating_team2 = mean(rating[4:])

    team1 = split[0:4]
    team2 = split[4:8]

    rating1 = rating[0:4]
    rating2 = rating[4:8]

    # then shuffle with predefined seeds
    team1 = [team1[i] for i in seed_list_1]
    team2 = [team2[i] for i in seed_list_2]

    rating1 = [rating1[i] for i in seed_list_1]
    rating2 = [rating2[i] for i in seed_list_2]

    elo_dif = abs(rating_team1-rating_team2)

    response = ""

    response += "TEAM 1 - avg elo: " + str(rating_team1) + "\n"
    response += "P1: " + str(team1[0]) + " " + str(rating1[0]) + "\n"
    response += "P3: " + str(team1[1]) + " " + str(rating1[1]) + "\n"
    response += "P5: " + str(team1[2]) + " " + str(rating1[2]) + "\n"
    response += "P7: " + str(team1[3]) + " " + str(rating1[3]) + "\n"
    response += "" + "\n"
    response += "TEAM 2 - avg elo: " + str(rating_team2) + "\n"
    response += "P2: " + str(team2[0]) + " " + str(rating2[0]) + "\n"
    response += "P4: " + str(team2[1]) + " " + str(rating2[1]) + "\n"
    response += "P6: " + str(team2[2]) + " " + str(rating2[2]) + "\n"
    response += "P8: " + str(team2[3]) + " " + str(rating2[3]) + "\n"
    response += "" + "\n"
    response += "The elo difference is " + str(elo_dif)

    #print("average elo difference = " + str(closeness[index_min]))

    return response

if __name__ == "__main__":
    ID_list = ['boo', 'egg', 'jeroen', 'ac', 'usha', 'peace', 'tyranny', 'flux']
    #print(team_split(ID_list))
"""