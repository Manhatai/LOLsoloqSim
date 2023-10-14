import random as rd
import statistics as stat
from pyprobs import Probability as pr
rank_current = input("Enter your rank: ")
lp_count = int(input("Enter how much lp you have in your current rank: "))
wr = int(input("Enter your winrate (could be global or on your favourite champion): ")) / 100
g_expected = int(input("How many games do you want to play?: "))



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



if rank_current == "iron IV": #dodaje ilość lp z rangi jaką posiadasz do wyniku rangi którą otrzymasz po x grach (DRY - TO DO)
    result_whole = result_whole + lp_count + 0
elif rank_current == "iron III":
    result_whole = result_whole + lp_count + 100
elif rank_current == "iron II":
    result_whole = result_whole + lp_count + 200
elif rank_current == "iron I":
    result_whole = result_whole + lp_count + 300
elif rank_current == "bronze IV":
    result_whole = result_whole + lp_count + 400
elif rank_current == "bronze III":
    result_whole = result_whole + lp_count + 500
elif rank_current == "bronze II":
    result_whole = result_whole + lp_count + 600
elif rank_current == "bronze I":
    result_whole = result_whole + lp_count + 700
elif rank_current == "silver IV":
    result_whole = result_whole + lp_count + 800
elif rank_current == "silver III":
    result_whole = result_whole + lp_count + 900
elif rank_current == "silver II":
    result_whole = result_whole + lp_count + 1000
elif rank_current == "silver I":
    result_whole = result_whole + lp_count + 1100
elif rank_current == "gold IV":
    result_whole = result_whole + lp_count + 1200
elif rank_current == "gold III":
    result_whole = result_whole + lp_count + 1300
elif rank_current == "gold II":
    result_whole = result_whole + lp_count + 1400
elif rank_current == "gold I":
    result_whole = result_whole + lp_count + 1500
elif rank_current == "platinum IV":
    result_whole = result_whole + lp_count + 1600
elif rank_current == "platinum III":
    result_whole = result_whole + lp_count + 1700
elif rank_current == "platinum II":
    result_whole = result_whole + lp_count + 1800
elif rank_current == "platinum I":
    result_whole = result_whole + lp_count + 1900
elif rank_current == "emerald IV":
    result_whole = result_whole + lp_count + 2000
elif rank_current == "emerald III":
    result_whole = result_whole + lp_count + 2100
elif rank_current == "emerald II":
    result_whole = result_whole + lp_count + 2200
elif rank_current == "emerald I":
    result_whole = result_whole + lp_count + 2300
elif rank_current == "diamond IV":
    result_whole = result_whole + lp_count + 2400
elif rank_current == "diamond III":
    result_whole = result_whole + lp_count + 2500
elif rank_current == "diamond II":
    result_whole = result_whole + lp_count + 2600
elif rank_current == "diamond I":
    result_whole = result_whole + lp_count + 2700




def rank_gained(result_whole): #wypisuje rangę którą powinieneś otrzymać (DRY - TO DO)
    if result_whole < 0:
        print("Your rank should be: iron IV")
    if result_whole in range(0, 99):
        print("Your rank should be: iron IV")
    if result_whole in range(100, 199):
        print("Your rank should be: iron III")
    if result_whole in range(200, 299):
        print("Your rank should be: iron II")
    if result_whole in range(300, 399):
        print("Your rank should be: iron I")
    if result_whole in range(400, 499):
        print("Your rank should be: bronze IV")
    if result_whole in range(500, 599):
        print("Your rank should be: bronze III")
    if result_whole in range(600, 699):
        print("Your rank should be: bronze II")
    if result_whole in range(700, 799):
        print("Your rank should be: bronze I")
    if result_whole in range(800, 899):
        print("Your rank should be: silver IV")
    if result_whole in range(900, 999):
        print("Your rank should be: silver III")
    if result_whole in range(1000, 1099):
        print("Your rank should be: silver II")
    if result_whole in range(1100, 1199):
        print("Your rank should be: silver I")
    if result_whole in range(1200, 1299):
        print("Your rank should be: gold IV")
    if result_whole in range(1300, 1399):
        print("Your rank should be: gold III")
    if result_whole in range(1400, 1499):
        print("Your rank should be: gold II")
    if result_whole in range(1500, 1599):
        print("Your rank should be: gold I")
    if result_whole in range(1600, 1699):
        print("Your rank should be: platinum IV")
    if result_whole in range(1700, 1799):
        print("Your rank should be: platinum III")
    if result_whole in range(1800, 1899):
        print("Your rank should be: platinum II")
    if result_whole in range(1900, 1999):
        print("Your rank should be: platinum I")
    if result_whole in range(2000, 2099):
        print("Your rank should be: emerald IV")
    if result_whole in range(2100, 2199):
        print("Your rank should be: emerald III")
    if result_whole in range(2200, 2299):
        print("Your rank should be: emerald II")
    if result_whole in range(2300, 2399):
        print("Your rank should be: emerald I")
    if result_whole in range(2400, 2499):
        print("Your rank should be: diamond IV")
    if result_whole in range(2500, 2599):
        print("Your rank should be: diamond III")
    if result_whole in range(2600, 2699):
        print("Your rank should be: diamond II")
    if result_whole in range(2700, 2799):
        print("Your rank should be: diamond I")
    if result_whole > 2800:
        print("Your rank should be: master +")





rank_gained(result_whole)

print(f"Your total lp after 1000 games: {result_whole}")

#skrypt rolujący ilość gier na wbicie podanej rangi na podsatwie winratio + wypisanie "your total lp" jako ranga + ilosc lp do 99
