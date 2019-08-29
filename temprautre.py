"""You are software developer. One of your clients is weather forecasting company.
They asked from you to design a program that allows them to enter the temperature
for the whole week. After that the program will show the hottest day and coldest 
day in that week.
"""

#since this variable is constant
#we going to write it in Capital
NUM_DAYS=7

max_temp=0
min_temp=100

#the for loop will iterate 7 times
#one for each day
for i in range(NUM_DAYS):
    print('enter the temperature for day',i+1)
    temp=int(input())
    if temp>max_temp:
        max_temp=temp
        hottes=i+1
    if temp<min_temp:
        min_temp=temp
        coldest=i+1
    
print('the Hottes day is: day',hottes)
print()
print('the Coldest day is: day',coldest)
