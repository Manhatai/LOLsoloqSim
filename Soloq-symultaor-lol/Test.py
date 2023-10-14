from pyprobs import Probability as pr

x = int(input("Podaj liczbę: ")) / 100

 # You can pass float (i.e. 0.5, 0.157), int (i.e. 1, 0) or str (i.e. '60%', '3/11')
print(pr.prob(x))

print(pr.prob("{:.0%}".format(x), num=5))