# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv


filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE
with open(filename) as file:
    lines=csv.reader(file)
    headers=next(lines)
    years_date_mean=[dict(zip(headers,line)) for line in lines]
GC_dic={}
GI_dic={}
#将不同source的数据分别存储在两个字典中
for e in years_date_mean:
    if e['Source']== 'GCAG':
        GC_dic.setdefault((e['Date'][0:4],e['Date'][5:7]),e['Mean'])
    else:
        GI_dic.setdefault((e['Date'][0:4],e['Date'][5:7]),e['Mean'])
def get_month(m):
    month={'January':'01','February':'02','March':'03','April':'04','May':'05',\
           'June':'06','July':'07','August':'08','September':'09','October':'10',\
           'November':'11','December':'12'
           }
    if m not in month.keys():
        print('Error input!')
        sys.exit()
    return month[m]
def compute_mean(dic,y1,y2,m):
    sum_mean=0
    for e in dic.keys():
        if int(e[0])<=max(y1,y2) and int(e[0])>=min(y1,y2) and e[1]==get_month(m):
            sum_mean += float(dic[e])
    mean= sum_mean/(abs(y2-y1)+1)
    return mean
def get_year_input(y_str):
    new_y=''.join(y_str.split())
    if '-' in new_y:
        print (int(new_y[0:4]),int(new_y[new_y.rindex('-')+1:new_y.rindex('-')+5]))
        return int(new_y[0:4]),int(new_y[new_y.rindex('-')+1:new_y.rindex('-')+5])
    else:
        print (int(new_y),int(new_y))
        return int(new_y),int(new_y)       
def record_above_years(dic,y1,y2,m):
    years_l=[]
    for e in dic.keys():
        if int(e[0])<=max(y1,y2) and int(e[0])>=min(y1,y2) and e[1]==get_month(m):
            if float(dic[e])>compute_mean(dic,y1,y2,m):
                years_l.append(int(e[0]))
    return years_l
y1,y2=get_year_input(year_or_range_of_years)
if source=='GCAG':
    average=round(compute_mean(GC_dic,y1,y2,month),2)
    years_above_average=sorted(record_above_years(GC_dic,y1,y2,month))
elif source=='GISTEMP':
    average=round(compute_mean(GI_dic,y1,y2,month),2)
    years_above_average=sorted(record_above_years(GI_dic,y1,y2,month))
else:
    print('Error input!')
    sys.exit()
print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
