import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("play.csv")

# create the plot
data.plot(kind="scatter",x="NumStudents",y="NumTickets")


# perform the linear regression using numpy library
x = data['NumStudents']
y = data['NumTickets']
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# add the trendline to the plot, as a dashed line
plt.plot(x, p(x) ,"r--")

plt.show()
