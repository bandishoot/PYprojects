import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("heartrates.csv")

# change the DataFrame index
data.set_index('student', inplace=True)

#print out the summary stats
# TODO

#plot the chart
# TODO


#show the plot
plt.show()

