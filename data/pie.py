import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

values = [50, 13]

colors =['#FAE500', '#2E00AD']

labels = ["Men", "Women"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)


plt.show()

