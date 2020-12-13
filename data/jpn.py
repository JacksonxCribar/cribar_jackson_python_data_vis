import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

values = [13, 14]

colors =['#FF0000', '#FFE65C']

labels = ["Japan", "China"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)


plt.show()