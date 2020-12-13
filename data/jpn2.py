import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

Sports = ["Japan", "China"]

color = ('#FF0006', '#ECFF00')

Medals = [13, 14]

plt.barh(Sports, Medals, color=color, linewidth=6.0)

plt.ylabel("Countries")

plt.xlabel("Medals Won")

plt.title("Japan VS China", pad="20", **hfont)

plt.show()