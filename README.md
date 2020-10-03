# Joan

Joan is a bot writen in Python for my Age of Empires 2 Discord server. Every user on the server has a rating (roughly corresponding to their 1v1 rating). This rating is used to automatically balance team games. The bot can be used to generate balanced civs suited to their position (no more Inca pocket). The main packages used are: `discord`, `pandas`, `random`.

## Major Functions

!civs [game_type] [tier_1] [tier_2]
This function randomly generates civilisations to play with

!stats [tag_user]
Get inhouse and AOE2.net API information about a user
Without an argument this returns the users stats

!tier [position = '1v1','2v2','3v3','4v4',integer up to 35]
Get inhouse information about civ rankings

!game
Get inhouse and AOE2.net API information about a game

!set
Used to set data in players.csv

!get
Used to get data from players.csv

!my_steam_id
Used by players on joining the server to associate their steam ID with their Discord ID (required to unlock the rest of the server)
This also creates a user.

!leaderboard [start_index] [end_index]
Sorts users by inhouse elo rating.
By default gets top 20.

!update_players
Updates players.csv with most recent Discord usernames

!result
logs game ID with elo change, winners, losers in games.csv and changes users' ratings

!pick [user1] [user2] ... [n]
Selects n users

!secret_pick [user1] [user2] ... [n]
Secretely selects n users

## Minor functions

!fuedal [number_vills] [loom] [your_time]
Optimal time and idle time for fuedal age

!castle [number_vills] [loom] [your_time]
Optimal time and idle time for castle age

!strat [civ]
Randomly generates a strat (for a given civ)

!yeno
Returns yes or no with 50% probality

!roll [n]
Returns an integer up to an including n. 

# Admin functions
!create_user
Used to create a user

!delete_user
Used to delete a user's information from players.csv after they have been banned from the server

!dm [tag_user] [message]
Direct message a user with the bot.

!revert [game_id]
Reverses everything that !result does
