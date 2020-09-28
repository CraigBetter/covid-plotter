# pcp.py <- pandas covid plotter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TODO: apend series of total daily cases to dataframe

class pcp():
    def __init__(self):
        self.data      = pd.read_csv('covid19.csv')
        self.names     = self.data['prname'].unique()
        self.provinces = [] #names of provinces to be used as keys
        for count, name in enumerate(self.names):
            self.provinces.append(self.data[self.data["prname"] == name])

    def sicktoday(self):
        #total ( sick - recovered - dead) ?
        sicktoday = []
        for count, province in enumerate(self.provinces):
            foo = self.data['numtotal'] - self.data['numrecover'] - self.data['ratedeaths']
            sicktoday.append(foo)
            pass

def main():
    data = pcp()
    #NS = data.prname == "Nova Scotia"
    #NS_data = data[NS]
    data.data.add(data.data.prname) #wft is this?
    return data
    #NS_data.plot(x='date',y='numtoday')
    #plt.show()

if __name__ == "__main__":
    data = main()
