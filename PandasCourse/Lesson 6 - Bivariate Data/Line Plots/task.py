import pandas as pd
import matplotlib.pyplot as plt

#read in data and reset index
data = pd.read_csv("temperature.csv")
data.set_index('Time', inplace=True)


#create plot
# TODO


plt.show()
