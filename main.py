import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from windrose import WindroseAxes

df = pd.read_excel('C:/Users/goop/PycharmProjects/windrose/data.xlsx')
fg = plt.figure()
for i in range (1, 4):
# count_d = 'Direction'+ str([1])
# count_v = 'Velo' + str([1])
# pdd = pd.Series(count_d)
# pdv = pd.Series(count_v)
    plt.clf()
    ax = WindroseAxes.from_ax()
    above_wd = df.loc[df['ST'] == i, 'Direction']
    above_ws = df.loc[df['ST'] == i, 'Velo']
    ax.bar(above_wd, above_ws, normed=True, opening=0.8, edgecolor='white')
    ax.set_xticklabels(['N', 'NW',  'W', 'SW', 'S', 'SE','E', 'NE'])
    ax.set_theta_zero_location('N')
    ax.set_legend()
    plt.savefig('{0}.png'.format(i))
    fg.canvas.draw()  # refresh
    fg.canvas.flush_events()
#print(type(pds))
#print(above_wd)

