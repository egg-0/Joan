
def mean(list):
    return sum(list)/len(list)

def elo_change(elo_lst1, elo_lst2, winner):
    if len(elo_lst1) != len(elo_lst2):
        print("number of players in each team must be the same")

    K = 32

    if winner == 1:
        score = 1
    if winner == 2:
        score = 0

    mean_elo1 = mean(elo_lst1)
    mean_elo2 = mean(elo_lst2)

    #print(mean_elo1)
    #print(mean_elo2)

    expected_score1 = 1/(1 + 10**((mean_elo2-mean_elo1)/400))
    expected_score2 = 1 / (1 + 10**((mean_elo1 - mean_elo2) / 400))

    #print(expected_score1)
    #print(expected_score2)

    rating_change1 = int(K*(score - expected_score1))
    rating_change2 = int(K*(1 - score - expected_score2))

    #print(rating_change1)
    #print(rating_change2)

    new_elo_lst1 = []
    new_elo_lst2 = []

    for elo1, elo2 in zip(elo_lst1,elo_lst2):
        new_elo_lst1.append(elo1 + rating_change1)
        new_elo_lst2.append(elo2 + rating_change2)

    if rating_change1 > 0:
        rating_str1 = "+" + str(rating_change1)
    else:
        rating_str1 = str(rating_change1)

    if rating_change2 > 0:
        rating_str2 = "+" + str(rating_change2)
    else:
        rating_str2 = str(rating_change2)

    rating_change = int(abs(rating_change1))

    return new_elo_lst1, new_elo_lst2, rating_str1, rating_str2, rating_change

if __name__ == '__main__':
    elo_lst1 = [1000, 1200, 1300]
    elo_lst2 = [1100, 1300, 1500]
    winner = 2

    [new_elo_lst1, new_elo_lst2] = elo_change(elo_lst1, elo_lst2, winner)

    print(new_elo_lst1)
    print(new_elo_lst2)

