import matplotlib.pyplot as plt
import pickle

# %matplotlib notebook

with open('g_plot.pkl','rb') as fid:
    ax = pickle.load(fid)
plt.show()