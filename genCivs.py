import random
from civ_weighting import *
import itertools
import numpy as np
import pandas as pd


"""
def civ_rank(pos):
    if pos == 'flank':
        rank_dict = {'Aztecs': 3,
                    'Berbers': 3,
                    'Britons': 1,
                    'Bulgarians': 5,
                    'Burmese': 3,
                    'Byzantines': 2,
                    'Celts': 4,
                    'Chinese': 1,
                    'Cumans': 3,
                    'Ethiopians': 1,
                    'Franks': 4,
                    'Goths': 4,
                    'Huns': 3,
                    'Incas': 2,
                    'Indians': 3,
                    'Italians': 2,
                    'Japanese': 2,
                    'Khmer': 3,
                    'Koreans': 2,
                    'Lithuanians': 4,
                    'Magyars': 2,
                    'Malay': 2,
                    'Malians': 3,
                    'Mayans': 1,
                    'Mongols': 3,
                    'Persians': 4,
                    'Portuguese': 3,
                    'Saracens': 2,
                    'Slavs': 4,
                    'Spanish': 5,
                    'Tatars': 3,
                    'Teutons': 4,
                    'Turks': 3,
                    'Vietnamese': 1,
                    'Vikings': 1}

    elif pos == 'pocket':
        rank_dict = {'Aztecs':5,
                    'Berbers':2,
                    'Britons':5,
                    'Bulgarians':3,
                    'Burmese':2,
                    'Byzantines':3,
                    'Celts':4,
                    'Chinese':2,
                    'Cumans':2,
                    'Ethiopians':5,
                    'Franks':1,
                    'Goths':4,
                    'Huns':1,
                    'Incas':5,
                    'Indians':1,
                    'Italians':3,
                    'Japanese':4,
                    'Khmer':1,
                    'Koreans':5,
                    'Lithuanians':1,
                    'Magyars':2,
                    'Malay':4,
                    'Malians':2,
                    'Mayans':5,
                    'Mongols':4,
                    'Persians':1,
                    'Portuguese':3,
                    'Saracens':3,
                    'Slavs':2,
                    'Spanish':2,
                    'Tatars':3,
                    'Teutons':1,
                    'Turks':3,
                    'Vietnamese':3,
                    'Vikings':5}

    elif pos == '1v1':
        rank_dict = {'Aztecs': 1,
                     'Berbers': 3,
                     'Britons': 1,
                     'Bulgarians': 5,
                     'Burmese': 4,
                     'Byzantines': 3,
                     'Celts': 3,
                     'Chinese': 1,
                     'Cumans': 4,
                     'Ethiopians': 3,
                     'Franks': 3,
                     'Goths': 5,
                     'Huns': 2,
                     'Incas': 3,
                     'Indians': 4,
                     'Italians': 3,
                     'Japanese': 3,
                     'Khmer': 2,
                     'Koreans': 4,
                     'Lithuanians': 3,
                     'Magyars': 4,
                     'Malay': 3,
                     'Malians': 2,
                     'Mayans': 1,
                     'Mongols': 3,
                     'Persians': 3,
                     'Portuguese': 3,
                     'Saracens': 3,
                     'Slavs': 3,
                     'Spanish': 4,
                     'Tatars': 3,
                     'Teutons': 4,
                     'Turks': 4,
                     'Vietnamese': 3,
                     'Vikings': 2}
    else:
        rank_dict = "position not found"

    return rank_dict
    """

def print_civ_rank(pos):

    rank = civ_rank(pos)

    sorted_1v1 = {k: v for k, v in sorted(rank.items(), key=lambda item: item[1])}

    response = 'CIV RANKING {}:\n'.format(str(pos).upper())

    for key in sorted_1v1.keys():
        #print(key)
        #print(sorted_1v1[key])
        response += key + ' ' + str(sorted_1v1[key]) + '\n'

    return response

def gen_civ(num_player = None, tier = None, pos = None):

    if num_player == None:
        num_player = 1

    #if tier == None:


    all_civs = ['Aztecs','Berbers','Britons','Bulgarians','Burmese','Byzantines','Celts','Chinese','Cumans','Ethiopians',
                'Franks','Goths','Huns','Incas','Indians','Italians','Japanese','Khmer','Koreans','Lithuanians','Magyars',
                'Malay','Malians','Mayans','Mongols','Persians','Portuguese','Saracens','Slavs','Spanish','Tatars',
                'Teutons','Turks','Vietnamese','Vikings']

    not_pocket = ['Britons','Ethiopians','Aztecs','Mayans','Incas','Koreans','Vikings','Celts']
    pocket_civs = [ele for ele in all_civs if ele not in not_pocket]

    not_flank = ['Spanish','Bulgarians']
    flank_civs = [ele for ele in all_civs if ele not in not_flank]

    # TEAM GAME CODE

    print("num play is {}".format(num_player))
    if num_player in [4,6,8]:
        shuffled_pockets = pocket_civs
        shuffled_flanks = flank_civs

        random.shuffle(shuffled_pockets)
        random.shuffle(shuffled_flanks)

        # prevent repeat civs
        for flank in shuffled_flanks[:4]:
            if flank in shuffled_pockets[:4]:
                shuffled_flanks.remove(flank)

        response = ""

        if num_player == 4:
            response += 'TEAM 1 CIVS\n'
            response += 'Player 1 is {} (tier {} flank)\n'.format(flank_civs[0],civ_rank('flank',flank_civs[0]))
            response += 'Player 3 is {} (tier {} pocket)\n'.format(pocket_civs[0],civ_rank('pocket',pocket_civs[0]))

            response += '\n'

            response += 'TEAM 2 CIVS' + "\n"
            response += 'Player 2 is {} (tier {} flank)\n'.format(flank_civs[1],civ_rank('flank',flank_civs[1]))
            response += 'Player 4 is {} (tier {} pocket)\n'.format(pocket_civs[1], civ_rank('pocket', pocket_civs[1]))


        elif num_player == 6:
            response += 'TEAM 1 CIVS\n'
            response += 'Player 1 is ' + flank_civs[0] + "\n"
            response += 'Player 3 is ' + pocket_civs[0] + "\n"
            response += 'Player 7 is ' + flank_civs[1] + "\n"

            response += '\n'

            response += 'TEAM 2 CIVS\n'
            response += 'Player 2 is ' + flank_civs[2] + "\n"
            response += 'Player 4 is ' + pocket_civs[1] + "\n"
            response += 'Player 8 is ' + flank_civs[3] + "\n"

        elif num_player == 8:
            response += 'TEAM 1 CIVS' + "\n"
            response += 'Player 1 is ' + flank_civs[0] + "\n"
            response += 'Player 3 is ' + pocket_civs[0] + "\n"
            response += 'Player 5 is ' + pocket_civs[1] + "\n"
            response += 'Player 7 is ' + flank_civs[1] + "\n"

            response += '\n'

            response += 'TEAM 2 CIVS' + "\n"
            response += 'Player 2 is ' + flank_civs[2] + "\n"
            response += 'Player 4 is ' + pocket_civs[2] + "\n"
            response += 'Player 6 is ' + pocket_civs[3] + "\n"
            response += 'Player 8 is ' + flank_civs[3] + "\n"

    if tier in [1,2,3,4,5]:
        civ_dict = civ_rank(pos)

        all_civs

        for civ,rank in zip(civ_dict.keys(),civ_dict.values()):
            if rank == tier:
                all_civs

    if num_player not in [4, 6, 8]:
        random.shuffle(all_civs)
        civ_picks = all_civs[:num_player]
        response = ''
        for civ in civ_picks:
            response += str(civ)
            response += '\n'

    return response

def find_subsets(input_set, size_subset):
    return list(itertools.combinations(input_set, size_subset))

def sampler(size_team, target_score, top_tier, bottom_tier):
    # https://stackoverflow.com/questions/40231094/generate-n-positive-integers-within-a-range-adding-up-to-a-total-in-python

    range_list = [top_tier,bottom_tier]

    assert range_list[0]<range_list[1], "Range should be a list, the first element of which is smaller than the second"
    arr = np.random.rand(size_team)
    sum_arr = sum(arr)

    new_arr = np.array([int((item/sum_arr) * target_score) if (int((item / sum_arr) * target_score) > range_list[0] and int((item / sum_arr) * target_score) < range_list[1]) \
                            else np.random.choice(range(range_list[0],range_list[1]+1)) for item in arr])
    difference = sum(new_arr) - target_score
    while difference != 0:
        if difference < 0 :
                for idx in np.random.choice(range(len(new_arr)),abs(difference)):
                    if new_arr[idx] != range_list[1] :
                        new_arr[idx] +=  1

        if difference > 0:
                for idx in np.random.choice(range(len(new_arr)), abs(difference)):
                    if new_arr[idx] != 0 and new_arr[idx] != range_list[0] :
                        new_arr[idx] -= 1
        difference = sum(new_arr) - target_score
    return new_arr

def team_civs(num_player_per_team, tier1=None, tier2=None):
    # Doing every permutation is too computationally expensive
    # Discrete approach it is

    # FOR 1V1
    # only generate from target tier

    # FOR 2V2
    # t1 generation = all civs from t1 if possible (if not possible add civs from tier 2)
    # t2/t3/t4 generation = 50% chance both civs from target tier.
    #                     = 50% chance one civ from tier above, one civ from tier below
    # t5 generation = all civs from t5 if possible (if not add civs from tier 4)

    # FOR 3V3
    # t1 generation = all civs from t1 if possible (if not possible add civs from tier 2)
    # t2/t3/t4 generation = 50% chance both civs from target tier.
    #                     = 50% chance one civ from tier above, one civ from tier below

    if tier1 == None:
        tier1 = 2
    if tier2 == None:
        tier2 = 2

    target_score_1 = num_player_per_team * tier1
    target_score_2 = num_player_per_team * tier2

    bottom_tier = 1
    top_tier = 5

    tier_index_1 = sampler(num_player_per_team, target_score_1, bottom_tier, top_tier)
    tier_index_2 = sampler(num_player_per_team, target_score_2, bottom_tier, top_tier)

    all_civs = civ_rank('all_civs')

    df = pd.read_csv('Civ_Tiers.csv', index_col=0)


    team1_civs = []
    team2_civs = []

    already_selected = []

    if num_player_per_team == 1:
        pos_team = ['1v1']
    if num_player_per_team == 2:
        pos_team = ['flank', 'pocket']
    if num_player_per_team == 3:
        pos_team = ['flank', 'pocket', 'flank']
    if num_player_per_team == 4:
        pos_team = ['flank','pocket','pocket','flank']

    for pos, tier in zip(pos_team,tier_index_1):
        civs_in_tier = list(df[df[pos] == tier].index)
        civs_in_tier_filtered = list(set(civs_in_tier) - set(already_selected))
        choice = random.choice(civs_in_tier_filtered)
        team1_civs.append(choice)
        already_selected.append(choice)

    for pos, tier in zip(pos_team,tier_index_2):
        civs_in_tier = list(df[df[pos] == tier].index)
        civs_in_tier_filtered = list(set(civs_in_tier) - set(already_selected))
        choice = random.choice(civs_in_tier_filtered)
        team2_civs.append(choice)
        already_selected.append(choice)

    response = ""

    if num_player_per_team == 2:
        response += "Warning: Tiers not working well for 2v2"

    response += "TEAM 1 - Civ score = {}\n".format(target_score_1)

    player_i = 1
    for civ, tier in zip(team1_civs,tier_index_1):
        response += "P{}: {} (tier {})\n".format(player_i,civ,tier)
        player_i += 2

    response += "\n"

    response += "TEAM 2 - Civ score = {}\n".format(target_score_2)

    player_i = 2
    for civ, tier in zip(team2_civs,tier_index_2):
        response += "P{}: {} (tier {})\n".format(player_i,civ,tier)
        player_i += 2


    return response



    #shuffled_list = random.shuffle(all_civs)

    #for civ in shuffled_list:
     #   if



    """
    all_civs = ['Aztecs','Berbers','Britons','Bulgarians','Burmese','Byzantines','Celts','Chinese','Cumans','Ethiopians',
                'Franks','Goths','Huns','Incas','Indians','Italians','Japanese','Khmer','Koreans','Lithuanians','Magyars',
                'Malay','Malians','Mayans','Mongols','Persians','Portuguese','Saracens','Slavs','Spanish','Tatars',
                'Teutons','Turks','Vietnamese','Vikings']

    all_civs = range(len(all_civs))

    #subsets = find_subsets(all_civs,num)

    print(subsets)
    print(len(subsets))"""



"""
def gen_civ(pos,num,tier):
    rank = civ_rank(pos)

    if tier is None:
        civs = rank.keys()
    if tier is not None:
        civs = [k for k, v in rank.items() if v == tier]

    random.shuffle(civs)

    return civs[:num]"""

if __name__ == '__main__':
    print(team_civs(4))