import pandas as pd
import numpy as np
import pathlib

def player_data():
    column_names = ['discord_id', 'discord_username', 'steam_id', 'rating', 'total_games', 'wins', 'losses', 'win_percentage']

    df = pd.DataFrame(columns=column_names)

    my_discord_id = 550098642871255068
    my_discord_user = '🥚egg🥚#2904'

    my_steam_id = 76561198043890292

    total_games = 0
    wins = 0
    losses = 0
    win_percentage = 0
    rating = 1611

    df.loc[0] = [int(my_discord_id/2), my_discord_user, my_steam_id, rating, total_games, wins, losses, win_percentage]
    df.loc[1] = [my_discord_id, my_discord_user, int(my_steam_id/2), rating, total_games, wins, losses, win_percentage]

    df.to_csv('players.csv',index=False)

    #print(df)

def print_dataframe(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        string = df.to_string(index=False)
        print(string)
    return string


def update_player_info(user_discord_id, target_column, new_info):
    column_names = ['discord_id', 'discord_username', 'steam_id', 'rating', 'total_games', 'wins', 'losses',
                    'win_percentage']

    if target_column not in column_names:
        response = "Error: Target_column not found. Column name must be {}".format(column_names)
        return response

    file_name = 'players.csv'

    df = pd.read_csv(file_name)

    #discord_IDs = pd.Series(column = 'discord_id')

    column_discord_id = df[['discord_id']].values

    if user_discord_id in column_discord_id: # if user discord ID already in data frame then add data to that row

        column_index_user = np.where(column_discord_id == user_discord_id)[0][0]

        print("index is {}".format(column_index_user)) # column_discord_id is numpy array

        df.at[column_index_user, target_column] = new_info

        df.to_csv('players.csv', index=False)
        response = "{} set".format(target_column)
    else:
        response = "discord_id not found"

    return response

def create_user(user_discord_id, user_discord_name):
    column_names = ['discord_id', 'discord_username', 'steam_id', 'rating', 'total_games', 'wins', 'losses',
                    'win_percentage']

    file_name = 'players.csv'
    df = pd.read_csv(file_name)
    column_discord_id = df[['discord_id']].values

    if user_discord_id in column_discord_id:
        response = "Error: User already created"
        return response
    else:
        next_free_index = len(column_discord_id)

        df.loc[next_free_index] = [user_discord_id, user_discord_name, 'None', 'None', 'None', 'None', 'None', 'None'] # None must be string otherwise integers converted to floats in csv
        df.to_csv(file_name, index=False)

        response = "User created"

        return response

def delete_user(user_discord_id):
    file_name = 'players.csv'
    df = pd.read_csv(file_name)
    column_discord_id = df[['discord_id']].values

    if user_discord_id not in column_discord_id:
        response = "Error: User not found"
        return response
    else:
        column_index_user = np.where(column_discord_id == user_discord_id)[0][0]

        df = df.drop(column_index_user,0)# the 2nd argument 0 is to drop a row

        print_dataframe(df)
        df.to_csv(file_name, index=False)
        response = "User deleted"
        return response

def stats(user_discord_id):
    file_name = 'players.csv'
    df = pd.read_csv(file_name)
    column_discord_id = df[['discord_id']].values

    if user_discord_id not in column_discord_id:
        response = "Error: User not found"
        return response
    else:
        column_index_user = np.where(column_discord_id == user_discord_id)[0][0]
        user_stats = df.loc[column_index_user]
        return str(user_stats)

def log_game(game_id, elo_change, winner_lst, loser_lst):
    file_name = 'games.csv'

    # force type
    game_id = int(game_id)

    columns = ['game_id', 'elo_change', 'winner 1', 'winner 2', 'winner 3', 'winner 4', 'loser 1', 'loser 2', 'loser 3', 'loser 4']

    file_exists = pathlib.Path(file_name)

    if not file_exists.is_file():
        df = pd.DataFrame(columns=columns)
        df.to_csv(file_name, index=False)

    df = pd.read_csv(file_name)
    column_game_id = df['game_id'].values

    if game_id in column_game_id.tolist():
        response = "Error: Game already logged"
        return response
    else:
        next_free_index = len(column_game_id)

        winners = ['None', 'None', 'None', 'None']
        losers = ['None', 'None', 'None', 'None']

        for i, winner in enumerate(winner_lst):
            winners[i] = winner
        for i, loser in enumerate(loser_lst):
            losers[i] = loser

        concat_lst = [game_id, elo_change] + winners + losers

        df.loc[next_free_index] = concat_lst
        df.to_csv(file_name, index=False)

        response = "Game logged"

        return response

def delete_game(game_id):
    file_name = 'games.csv'
    df = pd.read_csv(file_name)
    column_game_id = df['game_id'].values

    game_id = int(game_id) # force type

    if game_id not in column_game_id.tolist():
        response = "Error: Game not found"
        return response
    else:
        column_index_game = np.where(column_game_id == game_id)[0][0]

        df = df.drop(column_index_game, 0)  # the 2nd argument 0 is to drop a row
        print_dataframe(df)
        df.to_csv(file_name, index=False)
        response = "Game deleted"
        return response

if __name__ == "__main__":

    """
    player_data()
    target_column = 'total_games'
    new_info = 1

    print_dataframe(pd.read_csv('players.csv'))

    print(update_player_info(target_column, new_info))


    user_discord_id = 1234
    user_discord_name = 'James'
    print(create_user(user_discord_id, user_discord_name))

    print_dataframe(pd.read_csv('players.csv'))

    print(delete_user(user_discord_id))
    print_dataframe(pd.read_csv('players.csv'))
    """

    game_id = '1234'
    elo_change = 22
    winner_lst = ['56']
    loser_lst = ['78']

    response = log_game(game_id, elo_change, winner_lst, loser_lst)
    print(response)

    df = pd.read_csv('games.csv')
    print_dataframe(df)

    response = delete_game(game_id)
    print(response)

    df = pd.read_csv('games.csv')
    print_dataframe(df)
