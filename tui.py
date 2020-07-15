import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pplot import pplot
# TODO: fix the bad section
#       add error checking to make sure user can only input numbers in the
#       menus
#       remove the options from the second menu that are pointless
#       


data = pplot().data
names = pplot().names

for count, name in enumerate(names):      # this is all bad
    print(str(count).ljust(5) , name)     #
userinput = input("pick a number: ")      #
print(names[int(userinput)])              #
                                          #
datas = data.axes[1]                      #
for count, name in enumerate(datas):      #
    print(str(count).ljust(5) , name)     #
userinput2 = input("pick a number: ")     #
print(datas[int(userinput2)])             #

data[data.prname == names[int(userinput)]].plot(x='date',y=datas[int(userinput2)])
plt.show()
