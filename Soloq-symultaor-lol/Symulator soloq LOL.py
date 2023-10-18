import random as rd
from pyprobs import Probability as pr

rank_current = input("Enter your rank: ")
lp_count = int(input("Enter how much lp you have in your current rank: "))
wr = int(input("Enter your winrate (could be global or on your favourite champion): ")) / 100
g_expected = int(input("How many games do you want to play?: "))

def ranked_games(): 
    games = []
    lpki = 0
    game_count = 0
    while True:
        result = pr.prob(wr)  
        if result == True:
            lpki += rd.randint(20, 25)  
        if result == False:
            lpki += rd.randint(-22, -18)  
        games.append(lpki)
        game_count += 1
        if game_count == g_expected:  
            break
    return lpki


lp_total = []

for i in range(1000):  
    lpki = ranked_games()  
    lp_total.append(lpki)

result = sum(lp_total) / 1000
result_whole = round(result)

try:
    rank_types = {"iron IV": 0, "iron III": 100, "iron II": 200, "iron I": 300, "bronze IV": 400, "bronze III": 500, "bronze II": 600, "bronze I": 700, "silver IV": 800, "silver III": 900, "silver II": 1000, "silver I": 1100, "gold IV": 1200, "gold III": 1300, "gold II": 1400, "gold I": 1500,"platinum IV": 1600, "platinum III": 1700, "platinum II": 1800, "platinum I": 1900, "emerald IV": 2000, "emerald III": 2100, "emerald II": 2200, "emerald I": 2300, "diamond IV": 2400, "diamond III": 2500, "diamond II": 2600, "diamond I": 2700 }
    result_whole += lp_count + rank_types.get(rank_current)
except TypeError:
    print("Wpisz poprawną nazwę rangi.")
    quit()



def rank_gained(result_whole):
    rank_ranges = { (0, 99): "iron IV", (100, 199): "iron III", (200, 299): "iron II", (300, 399): "iron I", (400, 499): "bronze IV", (500, 599): "bronze III", (600, 699): "bronze II", (700, 799): "bronze I", (800, 899): "silver IV", (900, 999): "silver III", (1000, 1099): "silver II", (1100, 1199): "silver I", (1200, 1299): "gold IV", (1300, 1399): "gold III", (1400, 1499): "gold II", (1500, 1599): "gold I", (1600, 1699): "platinum IV", (1700, 1799): "platinum III",(1800, 1899): "platinum II", (1900, 1999): "platinum I", (2000, 2099): "emerald IV", (2100, 2199): "emerald III", (2200, 2299): "emerald II", (2300, 2399): "emerald I", (2400, 2499): "diamond IV", (2500, 2599): "diamond III", (2600, 2699): "diamond II", (2700, 2799): "diamond I", }
    for (start, end), rank in rank_ranges.items():
        if start <= result_whole <= end:
            print(f"Your rank should be: {rank} {round(result_whole/100)}LP")



rank_gained(result_whole)

