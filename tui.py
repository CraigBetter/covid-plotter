import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pplot import pplot

data = pplot().data
names = pplot().names

for count, name in enumerate(names):
    print(str(count).ljust(5) , name)
userinput = input("pick a number: ")
print(names[int(userinput)])
data[data.prname == names[int(userinput)]].plot(x='date',y='numtoday')
plt.show()
