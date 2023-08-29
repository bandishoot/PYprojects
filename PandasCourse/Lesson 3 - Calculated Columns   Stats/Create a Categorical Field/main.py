import pandas as pd

#user defined function to decide on the class depending on bmi value
def bmiClass(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

#read in the csv data
data = pd.read_csv('healthData.csv')

#calculate bmi
data['BMI'] = data['Weight']/(data['Height']**2)

#use the BMI value entered into the user-defined function using the apply method to assign the BMI classes
data['BMIClass'] = data['BMI'].apply(lambda x: bmiClass(x))

print(data[['Name','BMI','BMIClass']])
