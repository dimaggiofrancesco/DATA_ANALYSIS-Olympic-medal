import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # Splits the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()


# Question 1
# Which country has won the most gold medals in summer games?

def answer_one():
    answer_1 = (df['Gold'].idxmax())
    print ('ANSWER 1: The country that has won the most gold medals in summer games is', answer_1)

answer_one()


# Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?

def answer_two():
    answer_2 = abs(df['Gold']-df['Gold.1']).idxmax()
    print ('ANSWER 2: The country that had the biggest difference between their summer and winter gold medal counts is', answer_2)
answer_two()


# Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?

def answer_three():
    df1 = df[(df['Gold.1'] > 0) & (df['Gold'] > 0)]
    answer_3 = abs((df1['Gold'] - df1['Gold.1']) / df1['Gold.2']).idxmax()
    print ('ANSWER 3: The country that has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count is', answer_3)

answer_three()

# Question 4
# Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points,
# silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column
# (a Series object) which you created, with the country names as indices.

def answer_four():
    answer_4 = df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2']
    print ('ANSWER 4: The answer to the question 4 is \n', answer_4)

answer_four()