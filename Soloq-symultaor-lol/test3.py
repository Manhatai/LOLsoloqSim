import random as rd
from pyprobs import Probability as pr

while True:
    rank_types = {"iron IV": 0, "iron III": 100, "iron II": 200, "iron I": 300, "bronze IV": 400, "bronze III": 500,
                  "bronze II": 600, "bronze I": 700, "silver IV": 800, "silver III": 900, "silver II": 1000,
                  "silver I": 1100, "gold IV": 1200, "gold III": 1300, "gold II": 1400, "gold I": 1500,
                  "platinum IV": 1600, "platinum III": 1700, "platinum II": 1800, "platinum I": 1900,
                  "emerald IV": 2000, "emerald III": 2100, "emerald II": 2200, "emerald I": 2300, "diamond IV": 2400,
                  "diamond III": 2500, "diamond II": 2600, "diamond I": 2700}

    rank_current = input("Enter your rank: ")
    while (rank_current not in rank_types) or (isinstance(rank_current, str) == False):
        print("Rank not found")
        rank_current = input("Enter your rank: ")

    try:
        lp_count = int(input("Enter how much lp you have in your current rank (0 - 99): "))
        while (lp_count > 99) or (lp_count < 0):
            lp_count = int(input("Enter a valid LP count (0 - 99): "))
    except ValueError:
        lp_count = int(input("Enter a valid LP count (0 - 99): "))

    try:
        wr = (int(input("Enter your winrate (1 - 100) (could be global or on your favourite champion): ")) / 100)
        while (wr > 100) or (wr < 1):
            wr = (int(input("Invalid winrate value (should be 1 - 100): ")) / 100)
    except ValueError:
        wr = (int(input("Invalid winrate value (should be 1 - 100): ")) / 100)

    user_input = input("Would you like to calculate how many games it would take to get to a rank?: ")

    if user_input == 'yes':
        print("Your desired rank cant be lower than one rank up.")
        rank_new = input("Enter the rank you would like to obtain: ")
        games_expected = 10000   #there for now
        while rank_types.get(rank_new) < (rank_types.get(rank_current) + 399): # ranked_games() function works on a basis of adding and subtracting from value "lpki" and adding last result to the list, so if you
            print("Your desired rank cant be lower than one rank up.")         # want to calculate the amount games for your new desired rank thats lower than one rank up (especially if lower than 3 divisions)
            rank_new = input("Enter the rank you would like to obtain: ")      # it can create huge loose streaks per sample, resulting in 80 to 300 games needed to go one/two divisions up (if games_expected value is
    else:                                                                      # higher than 10) and messing up the median. The code will stay this way untill I figure out something better.
        try:
            games_expected = int(input("How many games do you want to play?: "))
        except ValueError:
            print("Invalid input.")
            games_expected = int(input("How many games do you want to play?: "))

    game_count_prob = []
    lp_total = []


    def ranked_games():
        games = []
        lpki = 0
        game_count = 0

        while True:
            result = pr.prob(wr) # returns True or False based on "wr" value
            if result:
                lpki += rd.randint(20, 25) # +20lp / +25lp
            else:
                lpki += rd.randint(-22, -18) # -18lp / -22lp

            if user_input == 'yes':
                if lpki + rank_types[rank_current] >= rank_types[rank_new]:
                    game_count_prob.append(game_count)
                    break

            if game_count == games_expected:
                break

            games.append(lpki)
            game_count += 1
        return lpki


    for i in range(1000): # 1000 * "games_expected" samples
        lpki = ranked_games()
        lp_total.append(lpki)

    result = sum(lp_total) / 1000
    result_whole = round(result)

    try:
        result_whole += lp_count + rank_types.get(rank_current) # rank_current is the key bound to lp value
    except TypeError:
        print("Enter a valid rank name.")
        continue


    def rank_gained(result_whole):
        rank_ranges = {(0, 99): "iron IV", (100, 199): "iron III", (200, 299): "iron II", (300, 399): "iron I",
                       (400, 499): "bronze IV", (500, 599): "bronze III", (600, 699): "bronze II",
                       (700, 799): "bronze I", (800, 899): "silver IV", (900, 999): "silver III",
                       (1000, 1099): "silver II", (1100, 1199): "silver I", (1200, 1299): "gold IV",
                       (1300, 1399): "gold III", (1400, 1499): "gold II", (1500, 1599): "gold I",
                       (1600, 1699): "platinum IV", (1700, 1799): "platinum III",
                       (1800, 1899): "platinum II", (1900, 1999): "platinum I", (2000, 2099): "emerald IV",
                       (2100, 2199): "emerald III", (2200, 2299): "emerald II", (2300, 2399): "emerald I",
                       (2400, 2499): "diamond IV", (2500, 2599): "diamond III",
                       (2600, 2699): "diamond II", (2700, 2799): "diamond I"}

        for (start, end), rank in rank_ranges.items():
            proper_lp_count = round(result_whole / 100)
            if start <= result_whole <= end:
                print(f"Your rank should be: {rank} {proper_lp_count}LP")
            if result_whole >= 2800:
                print(f"Your rank should be: master + {proper_lp_count - 2799}LP")
                break


    rank_gained(result_whole)
    print(f"Your total lp after {games_expected} games: {result_whole}")

    if user_input == "yes":
        print(f"Games needed to reach the desired rank: {round((sum(game_count_prob)) / len(game_count_prob))}")

    next_input = input("Do you want to continue (yes/no)?: ")
    if next_input != 'yes' or 'y':
        break
