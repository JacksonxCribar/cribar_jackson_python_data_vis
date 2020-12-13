import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

values = [1, 3, 1, 1, 1, 12, 10, 13, 2, 1, 7, 11]

colors = ['#6DB5FF', '#B73AFF', '#FF923A', '#58ED12', '#19E682', '#FF00CB', '#FE7C01', '#FF2F00', '#6F00FF', '#A6C33C', '#AA5A55', '#A5AC53']

labels = [1956, 1972, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

plt.pie(values, labels=labels, colors=colors)


plt.show()