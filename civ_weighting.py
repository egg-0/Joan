import random

def civ_rank(pos,name=None):
    if pos == 'all_civs':
        rank_dict = ['Aztecs','Berbers','Britons','Bulgarians','Burmese','Byzantines','Celts','Chinese','Cumans','Ethiopians',
                'Franks','Goths','Huns','Incas','Indians','Italians','Japanese','Khmer','Koreans','Lithuanians','Magyars',
                'Malay','Malians','Mayans','Mongols','Persians','Portuguese','Saracens','Slavs','Spanish','Tatars',
                'Teutons','Turks','Vietnamese','Vikings']


    elif pos == 'flank':
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
        rank_dict = None

    if name == None:
        return rank_dict
    else:
        return rank_dict[name]

def print_civ_rank(pos):

    rank = civ_rank(pos)

    print(rank)

    if rank == None:
        response = 'tier list not found'
    else:

        sorted_1v1 = {k: v for k, v in sorted(rank.items(), key=lambda item: item[1])}

        response = 'CIV RANKING {}:\n'.format(str(pos).upper())

        for key in sorted_1v1.keys():
            #print(key)
            #print(sorted_1v1[key])
            response += key + ' ' + str(sorted_1v1[key]) + '\n'

    return response

