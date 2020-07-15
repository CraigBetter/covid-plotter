# pplot.py <- pandas covid plotter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class pplot():
    def __init__(self):
        self.data = pd.read_csv('covid19.csv')
        self.names = self.data['prname'].unique()

def main():
    data = pplot().data
    NS = data.prname == "Nova Scotia"
    NS_data = data[NS]
    return data
    #NS_data.plot(x='date',y='numtoday')
    #plt.show()

if __name__ == "__main__":
    main()
