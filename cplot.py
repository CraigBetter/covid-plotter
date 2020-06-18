import matplotlib.pyplot as plt
#TODO: rate and total on different subplots

# data is like this:
# 0     1      2        3    4       5       6         7        8         9          10             11         12       13           
# pruid,prname,prnameFR,date,numconf,numprob,numdeaths,numtotal,numtested,numrecover,percentrecover,ratetested,numtoday,percentoday
# 12,Nova Scotia,Nouvelle-Écosse,11-03-2020,0,0,0,0,103,N/A,,,0,0.000

def attempt(arg, index):
    try:
        dummy = int(arg[index])
    except:
        dummy = 0
    return dummy

x = []
rate = []
total = []
nominal = [] # this is rate - (recover + deaths)
recover = []
deaths = []
death_rate = []
recover_rate = []
nominal = []
def datalyzer():
    dataline = []
    with open("covid19.csv") as f:
        for line in f:
            dataline.append(line)

    # print(dataline[0])

    for count, line in enumerate(dataline):
        container = line.split(",")
        if container[0] == "12":
            #x.append(count)
            rate.append(attempt(container, 12))
            total.append(attempt(container, 7))
            recover.append(attempt(container, 9))
            deaths.append(attempt(container, 6))
    for count, foo in enumerate(rate):
        x.append(count)

    for index, death in enumerate(deaths):
        if index == 0:
            death_rate.append(0)
        else:
            death_rate.append(deaths[index]-deaths[index-1])

    for index, item in enumerate(recover):
        if index == 0:
            recover_rate.append(0)
        else:
            recover_rate.append(recover[index]-recover[index-1])


    for index, item in enumerate(total):
        if index == 0:
            nominal.append(0)
        else:
            nominal.append(nominal[index-1] + rate[index] - (recover_rate[index] + death_rate[index]))

def f_rate():
    plt.plot(x, rate)
def f_total():
    plt.plot(x, total)
def f_nominal():
    plt.plot(x, nominal)
def f_deaths():
    plt.plot(x, deaths) # not a rate
def f_death_rate():
    plt.plot(x, death_rate)
def f_recover_rate():
    plt.plot(x, recover_rate) #this data is weird

def main():
    datalyzer()
    f_rate()
    #f_total()
    #f_nominal()
    # plt.yscale("log")
    plt.show()

if __name__ == "__main__":
    main()
