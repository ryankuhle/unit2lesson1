#Needed imports: pandas and scipy.stats
import pandas as pd
import scipy
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

#Answers