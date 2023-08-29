import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("subjects.csv")

# change the DataFrame index (this is different to the last task)
# This method causes the subject column to be dropped from the DataFrame except in the index)
data.set_index('subject', inplace=True)

#plot the chart
# TODO


#show the plot
plt.show()

