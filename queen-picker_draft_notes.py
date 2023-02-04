import pandas as pd

#queens = pd.read_csv(r'C:\Users\15023\Code-Louisville\rupaul\Queens - Sheet1.csv')
#print(queens)

#example below is how to read in a csv and only show certain columns

#.iloc[1:]will exclude first results

queens = pd.read_csv(r'C:\Users\15023\Code-Louisville\rupaul\Queens - Sheet1.csv')
totals = pd.DataFrame (queens, columns=['Queens', 'Total'])
print(totals.to_string(header=False))
print(queens)

#Print all stats for winners 
winners = queens[queens['Winners'] == 1]
print(winners['Queens'])


#winnerscol = pd.DataFrame (queens, columns=['Winners'])
#print(winnerscol.to_string(header=False))

#if winnerscol = t
#print(winnerscol)
queens = pd.read_csv(r'C:\Users\15023\Code-Louisville\rupaul\Queens - Sheet1.csv')
print(queens)

meanstat1 = queens['Stat 1'].mean()
meanstat2 = queens['Stat 2'].mean()
meanstat3 = queens['Stat 3'].mean()
meanstat4 = queens['Stat 4'].mean()
meantotal = queens['Total'].mean()

print("Average Stat 1 points per Queen: " + str(meanstat1) + "\nAverage Stat 2 points per Queen: " + str(meanstat2) + "\nAverage Stat 3 points per Queen: " + str(meanstat3) + "\nAverage Stat 4 points per Queen: " + str(meanstat4) + "\nAverage points per Queen: " + str(meantotal))
      
statistics = ("Average Stat 1 points per Queen: " + str(meanstat1) + "\nAverage Stat 2 points per Queen: " + str(meanstat2) + "\nAverage Stat 3 points per Queen: " + str(meanstat3) + "\nAverage Stat 4 points per Queen: " + str(meanstat4) + "\nAverage points per Queen: " + str(meantotal))
print(statistics)

list_of_inputs = ["All the Queens Names!", "Only the winners betch", "Gimme them averages", "Fuck the data, tell me what to do"]
options = '\n'.join('\t' + option for option in list_of_inputs)
first_question = input('What Would you like to know?\n\n' + options)


print(queens)

top_picks = queens[queens['Total']>30][['Queens', 'Total']]
print(top_picks)

top_picks = queens[queens['Total']>meantotal][['Queens', 'Total']]
print(top_picks)

running_top =[top_picks]
print(top_picks)

#import random
#top_picks_sample = top_picks.sample(n=3)
#print(top_picks_sample)

result = totals.to_string(header=False)

print(totals)
print(result)

import random

def pick_random_sample(df):
    return df.sample(n=3)

top_picks_sample = pick_random_sample(top_picks)
print(top_picks_sample)

pick random sample()

def hello():
    print('Hello')

hello()