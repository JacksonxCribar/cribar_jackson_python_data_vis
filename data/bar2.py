import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

Years = [1956, 1972, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]


Medals = [1, 3, 1, 1, 1, 12, 10, 13, 2, 1, 7, 11]

plt.bar(Years, Medals, color=(0/255, 100/255, 100/255), linewidth=5.0)

plt.ylabel("Medals")

plt.xlabel("Years")

plt.title("Comparing Japan's Olympics", pad="20", **hfont)

plt.show()