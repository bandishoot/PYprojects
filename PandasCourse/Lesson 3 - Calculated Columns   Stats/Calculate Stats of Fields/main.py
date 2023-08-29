import pandas as pd

data = pd.read_csv('shop.csv')

#create new calculated columns here
data['subtotal'] = data['Qty']*data['Price']
data['GST'] = round(data['subtotal']*0.1,2)
data['total']=data['subtotal']+data['GST']

#print the total of all the order here
print(# TODO)
