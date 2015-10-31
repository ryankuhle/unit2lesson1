#Needed imports: pandas and scipy.stats
import pandas as pd
from scipy.stats import mode
import scipy.stats

#Raw Data
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

#Convert raw data to pandas data frame
data = data.splitlines() #breaks data into row-based list
data = [i.split(',') for i in data] #for every item in data,  split by comma
column_names = data[0] #remove first  item, the header row, for column naming
data_rows = data[1::] #the remaining data in the list  data
df = pd.DataFrame(data_rows, columns=column_names) #push data into pandas, name columns

#convert values in data frame to float for mathematical use
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#Answers

print "The values for the Alcohol data set are as follows:"
print "Mean: ", df['Alcohol'].mean()
print "Median: ", df['Alcohol'].median()
print "Mode: ", mode(df['Alcohol'])
print "Range: ", max(df['Alcohol']) - min(df['Alcohol'])
print "Variance: ", df['Alcohol'].var()
print "Standard deviation: ", df['Alcohol'].std()
print
print "The values for the Tobacco data set are as follows:"
print "Mean: ", df['Tobacco'].mean()
print "Median: ", df['Tobacco'].median()
print "Mode: ", mode(df['Tobacco'])
print "Range: ", max(df['Tobacco']) - min(df['Tobacco'])
print "Variance: ", df['Tobacco'].var()
print "Standard deviation: ", df['Tobacco'].std()