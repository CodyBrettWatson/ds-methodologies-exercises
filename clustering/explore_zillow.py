# ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Wrangling
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# Exploring
import scipy.stats as stats

# Visualizing
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
from sklearn.model_selection import learning_curve
%matplotlib inline

pd.options.display.float_format = '{:20,.2f}'.format

import acquire
# import summarize
import prepare_zillow

# df = acquire.get_mallcustomer_data()
# df = prepare.data_prep(df, cols_to_remove=[], prop_required_column=.6, prop_required_row=.75)

def pairplot(df, col):
    sns.pairplot(df.loc[:,col])

def heatmap_func(df):
    plt.figure(figsize=(17,10))
    sns.heatmap(df.corr(), cmap='RdYlBu', annot=True, center=0)

def trisurf_func(df, x, y, z):
    df.columns=[x,y,z]

    # Make the plot
    fig = plt.figure(figsize=(17, 17))
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x, y, z, cmap=plt.cm.viridis, linewidth=0.2)
    plt.show()
    
    # to Add a color bar which maps values to colors.
    surf=ax.plot_trisurf(x, y, z, cmap=plt.cm.viridis, linewidth=0.2)
    fig.colorbar( surf, shrink=0.5, aspect=5)
    plt.show()
    
    # Rotate it
    ax.view_init(30, 45)
    plt.show()
    
    # Other palette
    ax.plot_trisurf(x, y, z, cmap=plt.cm.jet, linewidth=0.01)
    plt.show()

def scatter_3d (df, x ,y, z):
    df.columns=[x,y,z]
    fig = plt.figure(figsize=(17, 17))
    ax = fig.add_subplot(111, projection='3d')

    for c, m, s in [('r', 'x', 1), ('b','^', 1)]:
        xs = x
        ys = y
        zs = z
        ax.scatter(xs, ys, zs, c=c, marker=m, s=s)

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)

    plt.show()


def kde_func(x ,y):
    ax = sns.kdeplot(x, y, shade=True, cmap="cubehelix")
    fig.set_size_inches(11.7, 8.27)