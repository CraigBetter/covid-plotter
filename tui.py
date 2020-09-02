import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pcp import pcp
# TODO: add error checking to make sure user can only input numbers in the
#         menus
#       

# this is too terse?
def tui_menu(lst):
    def opt_fmtr(argv1, argv2):
        return str(argv1).ljust(5) + str(argv2)
    for count, item in enumerate(lst):
        print(opt_fmtr(count+1, item))
    print(opt_fmtr('q', 'quit'))
    choice = input("pick an option: ")
    if choice == 'q':
        exit()
    else:
        return str(int(choice) - 1)

data      = pcp().data
names     = pcp().names     #names of provinces
provinces = pcp().provinces #dataframes of provinces

# ask user to choose a province
userinput = tui_menu(names)
print(names[int(userinput)])

# ask user to choose a data set
datas = data.axes[1][4:]  # axes[0] is row index, axes[1] is column index
userinput2 = tui_menu(datas)
print(datas[int(userinput2)])

# graph the data
data[data.prname == names[int(userinput)]].plot(x='date',y=datas[int(userinput2)])
plt.show()
