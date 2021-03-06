# pcp.py <- pandas covid plotter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TODO: 

class pcp():
    def __init__(self):
        self.data      = pd.read_csv('covid19.csv')
        self.names     = self.data['prname'].unique()
        self.provinces = []
        for count, name in enumerate(self.names):
            self.provinces.append(self.data[self.data["prname"] == name])

def main():
    data = pcp()
    #NS = data.prname == "Nova Scotia"
    #NS_data = data[NS]
    return data
    #NS_data.plot(x='date',y='numtoday')
    #plt.show()

if __name__ == "__main__":
    data = main()
