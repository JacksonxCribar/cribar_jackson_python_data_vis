import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

Sports = ["Skiing", "Skating"]

color = ('#75CDFF', '#FF2727')

Medals = [35, 28]

plt.barh(Sports, Medals, color=color, linewidth=6.0)

plt.ylabel("Sports")

plt.xlabel("Medals Won")

plt.title("Skiing VS Skating", pad="20", **hfont)

plt.show()

