# pplot.py <- pandas covid plotter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TODO: rename this file to pcp.py and tell git about it

class pplot():
    def __init__(self):
        self.data = pd.read_csv('covid19.csv')
        self.names = self.data['prname'].unique()
        self.datas = []
        for count, name in enumerate(self.names):
            self.datas.append(self.data.prname == name)

def main():
    data = pplot()
    #NS = data.prname == "Nova Scotia"
    #NS_data = data[NS]
    return data
    #NS_data.plot(x='date',y='numtoday')
    #plt.show()

if __name__ == "__main__":
    data = main()
