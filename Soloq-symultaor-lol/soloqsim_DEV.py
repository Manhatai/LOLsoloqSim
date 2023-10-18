import random as rd
import statistics as stat
from pyprobs import Probability as pr
rank_current = input("Enter your rank: ")
lp_count = int(input("Enter how much lp you have in your current rank: ")) # Jesli wiecej niz 99, lub mniej niz 0, zwroc blad (TO DO)
wr = int(input("Enter your winrate (could be global or on your favourite champion): ")) / 100
g_expected = int(input("How many games do you want to play?: "))


#

#rank_new = input("\nEnter the rank you would like to obtain: ") #Kiedyś żeby pisało ile gier zagrać +- aby mieć x range


#skrypt symulujący lp gain, rangi, musi uzyc rolla ktory wybierze miedzy win a loose
#kod wykonuje się 10 razy i wylicza srednia ze sredniego lp gain po 10 x (ilosc gier)

def ranked_games():
    with open ('writeme.txt', 'w') as file: #zapisywanie wyników?
        file.write('writeme')
    games =[]
    lpki = 0
    game_count = 0
    while True:
        result = pr.prob(wr) # returns a True/False value (50% winrate)
        if result == True:
            lpki += rd.randint(20, 25) # +20lp / +25lp
        if result == False:
            lpki += rd.randint(-22, -18) # -18lp / -22lp
        games.append(lpki)
        game_count += 1
        if game_count == g_expected: # how many games played per sample?
            break
    median = stat.median(games)
    #print(games)
    #print(lpki, "- Total amount of LP gained within 1000 games")
    #print(round(median), "- Average LP gained within 1000 games\n")
    return lpki, median


lp_total = []
medians = []

for i in range(1000): # 1000 x 1000 games played
    lpki, median = ranked_games() # saving function results to variables
    lp_total.append(lpki)
    medians.append(round(median))

#print(lp_total, "- To jest lista gainu lp z każdej próbki")
#print(sum(lp_total),"- The total amount of LP after 1000 samples\n")
#print(med#ans, "- To jest lista median z każdej próbki\n")
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
print(f"Your total lp after 1000 games: {result_whole}")

#skrypt rolujący ilość gier na wbicie podanej rangi na podsatwie winratio + wypisanie "your total lp" jako ranga + ilosc lp do 99
