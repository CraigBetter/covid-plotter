# pplot.py <- pandas covid plotter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pplot():
    data = pd.read_csv('covid19.csv')
    names = data['prname'].unique()
    return data

def main():
    data = pplot()
    NS = data.prname == "Nova Scotia"
    NS_data = data[NS]
    NS_data.plot(x='date',y='numtoday')
    plt.show()

if __name__ == "__main__":
    main()

