def number_of_games(rounds,players):
    if rounds == 0:
        return 0
    if len(players) == 2:
        return all(players)
    games = [players[i:i+2] for i in range(0,len(players)-1,2)]
    next_players = list(map(any,games))
    games_played = sum(map(all,games))+number_of_games(rounds-1, next_players)
    return games_played

test_cases = [(2,[1,1,1,1]), (1,[1,1,1,1]), (2,[0,1,1,0]), (2, [1,0,1,0,1,0,1,0])]
for case in test_cases:
    print(number_of_games(*case))
        


