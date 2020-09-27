# bot.py
import os
import random
import discord
from dotenv import load_dotenv
import re
import csv
import os.path as path

from genCivs import *
from autosplitter import *
from civ_weighting import *
from api_calls import *
from elo import *
from pandas_data import *

# default in discord packages is that user id is an integer

def get_steam_id(discord_id):
    df = pd.read_csv('steam_id.csv',index_col=None)
    print(df['Discord_ID'])
    print('the discord ID is {}'.format(discord_id))
    print("the type is {}".format(type(discord_id)))
    print('the panda data is {}'.format(df['Discord_ID']))
    panda_series = (df['Discord_ID'] == int(discord_id)) #panda opens numbers as ints

    print("the panda series is {}".format(panda_series))

    if panda_series.any:
        #print('ID found: {}'.format(any_true))
        #print('type is: {}'.format(type(any_true)))
        #print('type is: {}'.format(any_true.all()))

        print(f"Discord ID is {discord_id}")
        print("weird string is {}".format(df['Discord_ID'] == int(discord_id), 'Steam_ID'))

        print(df['Discord_ID'])

        steam_id = df[df['Discord_ID'] == int(discord_id)]['Steam_ID'].values[0]

        print("steam ID list is {}".format(str(steam_id)))

        #steam_id = df.loc[df['Discord_ID'] == int(discord_id), 'Steam_ID'].item()

    else:
        steam_id = False

    return steam_id

def print_lst(lst):
    response = ''
    for item in lst:
        response += "{}\n".format(item)

    return response

def rating_handle(rating):
    if rating != None:
        if not str(rating).strip('-').isnumeric():
            response = 'rating must be numeric'
        elif float(rating) < 0:
            response  = 'rating cannot be negative'
        elif float(rating) > 2500:
            response = 'you are not better than the viper'
        else:
            response = True
    else:
        response = True

    return response


def arg_process(msg):
    split_msg = msg.content.split(' ')

    if len(split_msg) > 1:
        args = split_msg[1:]

        arg_lst = []
        for arg in args:
            if arg.startswith('<@!'): # PC @ syntax
                arg = arg[3:-1]
            if arg.startswith('<@'): # PC @ syntax
                arg = arg[2:-1]
            if arg.isnumeric():
                if len(arg) < 10: # process non-IDs as ints
                    arg = int(arg)
                if "//" in str(arg):
                    url = arg.split("//")[1]
                    arg_lst.append(url)


            if arg != '': # don't append excess spaces
                arg_lst.append(arg)


        #if len(arg_lst) == 1:
        #    arg_lst = arg_lst[0]

    else:
        arg_lst = None

    return arg_lst

def strat(civ=None,n=None):

    if civ is None:
        pass

    if n is None:
        n = 1

    strat_lst = ['Dark age rush with militia (drush)',
                 'Build forward towers (trush)',
                 'Scout rush (scrush)','Archer rush (flush)',
                 'Send 3 or 4 man at arms (M@A)',
                 'Fast Castle into dead flank (FC)',
                 'Knight rush (krush)',
                 'Siege + monk rush (smush)',
                 'Fast Imperial (FI)',
                 'Delete your town centre and rebuild it forward (douche)',
                 'Galley rush (grush)']

    strat = strat_lst[random.randint(0, len(strat_lst)) - 1]

    print('The civ is ' + str(civ))
    if civ is not None:
        defined_strat = {'incas': 'trush',
                         'japanese': 'M@A into archers',
                         'khmer': '16 pop scouts (no vills on wood)'}

        if civ not in defined_strat.keys():
            strat = 'This civ has no strat'
        else:
            strat = defined_strat[civ.lower()]


    return strat

def joan():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    client = discord.Client()


    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to Discord!')

    @client.event
    async def on_member_join(member):
        #await member.create_dm()
        #await member.dm_channel.send(

        welcome_channel = client.get_channel(759106868013957174)


        response = "Welcome <@{}>. So that we can balance our team games please type `!my_steam_id ` followed by your steam ID.\n".format(member.id)
        response += "if you don\'t know your steam ID please follow this guide (https://medium.com/@arielmu/how-to-find-your-steam-id-heres-a-complete-guide-8279b2f3a325)\n"

        await welcome_channel.send(response)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        if message.content.startswith('!split '):

            arg_lst = arg_process(message)

            ID_list = []

            n = None
            for arg in arg_lst:
                if arg.startswith('n='):
                    n = int(arg.split("=")[1]) - 1
                    print(f"n is {n}")
                else:
                    ID_list.append(arg)

            response = team_split(ID_list, n)
            await message.channel.send(response)


            """
            string = message.content.split('@!')
            print("the string is " + str(string))
            for item in string[1:]:
                item = item.split('>')[0]

                #print('item is ' + str(item[:-1]))
                ID_list.append(item)

            print(ID_list)

            if ID_list == ID_list_2:
                print('identical')"""

        if message.content == '!hi ':
            userID = message.author.id

            #await message.channel.send(message, '<@!' + str(response) + '>, hi!')
            response = ('<@!{}>, hi!').format(userID)
            await message.channel.send(response)

        if message.content.startswith('!my_rating'):

            """
            userID = message.author.id

            #split_msg = message.content.split(" ",1)

            args = arg_process(message)

            print("args are {}".format(args))

            rating = args

            response = rating_handle(args)
            print("response is {}".format(response))

            if response == True:

                f = open("ratings.txt", "r")
                f_string = f.readlines()

                new_f = ''
                for line in f_string:
                    if not line.startswith(str(userID)): # delete old ratings
                        new_f += line

                #if str(userID) in f_string:
                #    print(f_string.split(str(userID)))

                new_f += str(userID) + ' ' + str(rating) + '\n'

                f.close()
                f = open("ratings.txt", "w")
                f.write(new_f)
                f.close()

                # open and read the file after the appending:
                all_ratings = open("ratings.txt", "r")

                all_ratings = all_ratings.read()

                rating = re.search(str(userID) + ' (.*)' + '\n', all_ratings)

                response = "The rating of <@!{}> is {}".format(userID,str(rating.group(1)))

                print('yes')"""

            response = "This function is no longer in use since it fucked everything up"

            await message.channel.send(response)

        if message.content.startswith('!rating '):

            ID_list = arg_process(message)

            #string = message.content.split('@!')
            #for item in string[1:]:
             #   ID_list.append(item[:18])


            #ID_list = arg_process(message)

            #[1][:-1]

            if type(ID_list) is str:
                print('executed')
                ID_list = [ID_list]

            response = ""

            f = open("ratings.txt", "r")
            f_string = f.readlines()
            for line in f_string:
                if line.startswith(tuple(ID_list)):
                    rating = line.split(' ')[1]
                    ID = line.split(' ')[0]
                    response += "The rating of <@!{}> is {}".format(ID, str(rating))

            if len(response) == 0:
                response += "This user has no rating"

            await message.channel.send(response)

        if message.content.startswith('!set_rating'):
            if message.author.id == 550098642871255068:
                split_msg = message.content.split("> ",1)
                rating = int(split_msg[1])

                targetID = message.content.split("@!", 1)[1]
                #targetID = targetID.split(,1)[0]
                targetID = targetID.split('>')[0]

                print(targetID)

                f = open("ratings.txt", "r")
                f_string = f.readlines()

                new_f = ''
                for line in f_string:
                    if not line.startswith(str(targetID)): # delete old ratings
                        new_f += line

                #if str(userID) in f_string:
                #    print(f_string.split(str(userID)))

                new_f += str(targetID) + ' ' + str(rating) + '\n'

                f.close()
                f = open("ratings.txt", "w")
                f.write(new_f)
                f.close()

                response = 'rating set'
            else:
                response = 'Only :egg: may do this'

            await message.channel.send(response)

        if message.content.startswith('!all_rating'):

            f = open("ratings.txt", "r")
            f_string = f.readlines()


            response = ''
            for line in f_string:
                split_msg = line.split(' ')
                ID = split_msg[0]
                rating = split_msg[1]
                response += "The rating of <@!{}> is {}".format(ID, str(rating))
            await message.channel.send(response)

        if message.content.startswith('!tier'):
            #pos = message.content.split(' ')[0]

            pos = arg_process(message)[0]

            print(f"pos is {pos}")

            if pos == None:
                pos = '1v1'

            response = print_civ_rank(pos)
            print(response)
            await message.channel.send(response)

        if message.content.startswith('!civ' or '!civs'):


            args = arg_process(message)

            if args != None:
                game_type = arg_process(message)[0]
                tier = None
                if len(args) > 1:
                    tier = arg_process(message)[1]
            else:
                game_type = 1
                tier = None



            #if len(msg) == 4:
            #    tier = int(msg[2])
            #    pos = msg[3]

            response = gen_civ(game_type,tier)
            await message.channel.send(response)

        if message.content.startswith('!prob_win'):
            msg = message.content.split(' ')
            elo1 = msg[1]
            elo2 = msg[2]

            print("elo1 is" + str(elo1))

            if elo1.startswith('<@'):
                string = message.content.split('@!')
                user1 = string[1]
                user1 = user1.split('>')[0]
                user2 = string[2]
                user2 = user2.split('>')[0]
                print("user1 is " + str(user1))
                [elo1,elo2] = read_rating([user1,user2])

                print("elo1 is" + str(elo1))
                print("elo2 is" + str(elo2))

            prob_win = 100/(1 + 10**((float(elo2) - float(elo1))/400))
            response = "The win probability is {}%".format(round(prob_win))
            await message.channel.send(response)

        if message.content.startswith('!gif'):

            options = ['https://imgur.com/a/CDSXj49','https://imgur.com/a/dREMflN']

            response = random.choice(options)
            await message.channel.send(response)

        if message.content.startswith('!strat'):
            civ = arg_process(message)[0]
            print(civ)

            response = strat(civ)

            await message.channel.send(response)

        if message.content.startswith('!password'):
            response = 'The password is `potato`'
            await message.channel.send(response)

            commands = ['!split',
                        '!hi',
                        '!rating',
                        '!set_rating',
                        '!all_rating',
                        '!tier',
                        '!civ',
                        '!prob_win',
                        '!zv',
                        '!strat']

            response = commands
            await message.channel.send(response)

        if message.content == '!fc':
            response = 'https://imgur.com/a/rrpBEdg#aCnOnxY'
            await message.channel.send(response)

        if message.content.startswith('!message'):
            response = message.content
            await message.channel.send('`' + response + '`')

        if message.content.startswith('!leader'):

            arg = arg_process(message)[0]

            if arg > 50:
                response = 'message is too big'
            else:
                response = leaderboard(arg)
            await message.channel.send(response)

        if message.content.startswith('!rating_history'):

            args = arg_process(message)

            print(args)

            discord_id = args[0]
            if len(args) > 1:
                num_rec = args[1]
            else:
                num_rec = 10

            steam_id = get_steam_id(discord_id)

            if steam_id == False:
                response = "no steam ID found"
            else:
                print("the steam ID is {}".format(steam_id))

                #if args == '550098642871255068':
                #    args = '76561198043890292'


                response = rating_history(steam_id, num_rec)

            await message.channel.send(response)

        if message.content.startswith('!my_steam_id'):
            discord_id = str(message.author.id)
            steam_id = arg_process(message)[0]

            file_name = 'steam_id.csv'

            columns = ['Discord_ID', 'Steam_ID']

            if path.exists(file_name):
                df = pd.read_csv(file_name, header=0)
            else:
                df = pd.DataFrame(columns=columns)

            print("df is {}".format(df))

            print("data to append is {}".format([discord_id,steam_id]))

            new_df = pd.DataFrame([[discord_id,steam_id]],columns=columns)

            print("new_df is {}".format(new_df))

            #big_df = df.concat(new_df)
            big_df = pd.concat([df, new_df], ignore_index=True, sort=True)
            #big_df = df.append(new_df, ignore_index=True)

            big_df.to_csv(file_name,index=False)

            print("big_df is {}".format(big_df))


        # player info set commands go here

        if message.content.startswith('!create_user'):
            args = arg_process(message)
            discord_id = int(args[0])

            user = client.get_user(discord_id)

            response = create_user(discord_id, user.name)
            await message.channel.send(response)

        if message.content.startswith('!delete_user'):
            args = arg_process(message)
            discord_id = int(args[0])

            response = delete_user(discord_id)
            await message.channel.send(response)

        if message.content.startswith('!set_user'):
            args = arg_process(message)
            discord_id = int(args[0])
            column = args[1]
            new_info = args[2]
            if str(new_info).isnumeric():
                new_info = int(new_info)

            response = update_player_info(discord_id, column, new_info)
            await message.channel.send(response)

        if message.content.startswith('!stats'):
            args = arg_process(message)
            discord_id = int(args[0])
            response = stats(discord_id)
            await message.channel.send(response)

        if message.content.startswith('!set_steam_id'):
            discord_id = arg_process(message)[0]
            steam_id = arg_process(message)[1]
            user_name = client.get_user(int(discord_id))

            file_name = 'steam_id.csv'
            columns = ['Discord_ID', 'Steam_ID','Username']

        if message.content.startswith('!set_steam_id'):
            discord_id = arg_process(message)[0]
            steam_id = arg_process(message)[1]
            user_name = client.get_user(int(discord_id))

            file_name = 'steam_id.csv'

            columns = ['Discord_ID', 'Steam_ID','Username']

            if path.exists(file_name):
                df = pd.read_csv(file_name, header=0)
            else:
                df = pd.DataFrame(columns=columns)

            #print("df is {}".format(df))

            #print("data to append is {}".format([discord_id,steam_id,user_name]))

            new_df = pd.DataFrame([[discord_id,steam_id,user_name]],columns=columns)

            #print("new_df is {}".format(new_df))

            #big_df = df.concat(new_df)
            big_df = pd.concat([df, new_df], ignore_index=True, sort=True)
            #big_df = df.append(new_df, ignore_index=True)

            big_df.to_csv(file_name,index=False)

            response = 'steam ID set'
            await message.channel.send(response)

        if message.content.startswith('!set_steam_id'):
            discord_id = arg_process(message)[0]
            steam_id = arg_process(message)[1]
            user_name = client.get_user(int(discord_id))

            file_name = 'steam_id.csv'

            columns = ['Discord_ID', 'Steam_ID','Username']

            if path.exists(file_name):
                df = pd.read_csv(file_name, header=0)
            else:
                df = pd.DataFrame(columns=columns)

            #print("df is {}".format(df))

            #print("data to append is {}".format([discord_id,steam_id,user_name]))

            new_df = pd.DataFrame([[discord_id,steam_id,user_name]],columns=columns)

            #print("new_df is {}".format(new_df))

            #big_df = df.concat(new_df)
            big_df = pd.concat([df, new_df], ignore_index=True, sort=True)
            #big_df = df.append(new_df, ignore_index=True)

            big_df.to_csv(file_name,index=False)

            response = 'steam ID set'
            await message.channel.send(response)

            #print("big_df is {}".format(big_df))

        if message.content.startswith('!test'):
            response = message.author.mention

            arg = arg_process(message)[0]

            print(int(arg))

            user = client.get_user(int(arg))

            await message.channel.send(user.name)

        if message.content == '!yes_no' or message.content == '!yeno':
            choices = ['yes','no']
            response = random.choice(choices)
            await message.channel.send(response)

        if message.content.startswith('!game'):
            game_ID = arg_process(message)[0]

            #print("game ID is" + str(game_ID))

            #response = str(game_ID)

            response_steam = game_data(game_ID)
            response_inhouse = get_game_data(game_ID)

            response = "STEAM RESPONSE\n" + response_steam + "\n\nINHOUSE RESPONSE\n" + response_inhouse

            await message.channel.send(response)

        if message.content.startswith('!delete_game'):
            game_ID = int(arg_process(message)[0])
            response = delete_game(game_ID)
            await message.channel.send(response)

        #if message.content.startswith('!delete'): how to delete message
        #    await message.delete()

        if message.channel.id == 755505889863139478:
            if not message.content.startswith('aoe2de://'):
                if not message.content.isnumeric():
                    response = "Only game codes in here please"
                    await message.channel.send(response)

                #content.startswith9("!get_channel"):
            #client.get_channel("756900403857195159")

        if message.content.startswith("!update"):
            update_elo()

        if message.content.startswith(("!team_civs", "!team_civ")):

            args = arg_process(message)

            game_type = args[0]

            if game_type == "1v1":
                num_players_per_team = 1
            if game_type == "2v2":
                num_players_per_team = 2
            if game_type == "3v3":
                num_players_per_team = 3
            if game_type == "4v4":
                num_players_per_team = 4

            if len(args) == 1:
                tier1 = 2
                tier2 = 2

            if len(args) >= 2:
                tier1 = args[1]
                tier2 = tier1
                if len(args) == 3:
                    tier2 = args[2]

            response = team_civs(num_players_per_team, tier1, tier2)

            await message.channel.send(response)

        if message.content == "!auto":
            url = 'https://www.youtube.com/watch?v=q879j3ydfw8'
            await message.channel.send(url)

        if message.content.startswith("!result"):
            args = arg_process(message)

            game_id = args[0]

            win_index = args.index("won")
            lost_index = args.index("lost")

            winners = args[win_index+1:lost_index]
            losers = args[lost_index+1:]

            print("winners are {}".format(winners))
            print("losers are {}".format(losers))

            win_elo = read_rating(winners)
            lose_elo = read_rating(losers)

            print(win_elo)
            print(lose_elo)

            [new_elo_lst1, new_elo_lst2, rating_change1, rating_change2, rating_change] = elo_change(win_elo, lose_elo, 1)

            response = ""

            for winner, elo in zip(winners, new_elo_lst1):
                response += "The new rating of <@{}> is {} ({})\n".format(winner, elo, rating_change1)
            for loser, elo in zip(losers, new_elo_lst2):
                response += "The new rating of <@{}> is {} ({})\n".format(loser, elo, rating_change2)

            log_response = log_game(game_id, rating_change, winners, losers)
            response += log_response + "\n"

            elo_response = player_update_after_game(winners, losers, rating_change)
            response += elo_response + "\n"

            await message.channel.send(response)

        if message.content.startswith('!flux_gameplay'):
            response = 'https://imgur.com/a/BTHygvz'
            await message.channel.send(response)

        if message.content.startswith('!map'):
            args = arg_process(message)
            if args != None:
                args = args[0]
            else:
                map = 'all'

            map_open = ['Arabia', 'Cenotes', 'Four Lakes', 'Ghost Lake', 'Gold rush', 'Golden pit', 'Lombardia', 'Steppe', 'Valley']
            map_closed = ['Arena', 'Black Forest']

            response = "The map is {}".format(random.choice(map_open))
            await message.channel.send(response)

        if message.content.startswith('!user'):
            args = arg_process(message)
            args[0]

            user = client.get_user(int(args[0]))

            print(user)

            response = ""
            response += "discord ID: {}\n".format(user.id)
            response += "discord user: {}\n".format(user)
            response += "discord username: {}\n".format(user.name)

            await message.channel.send(response)

        if message.content.startswith("!dab"):
            response = "https://imgur.com/a/uPvyWza"
            await message.channel.send(response)

    client.run(TOKEN)

def update_elo():
    df = pd.read_csv('steam_id.csv', index_col=None)

    for index, row in df.iterrows():#
        print(row)


if __name__ == "__main__":
    joan()
    #update_elo()





