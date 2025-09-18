import pandas as pd

df = pd.read_csv("thursday/students_with_scores.csv")
# print(df)

print(df.head())
#        Name      School Grade  Score
# 0  Student1   West High     A     92
# 1  Student2  South High     F      6
# 2  Student3  North High     D     64
# 3  Student4   West High     B     88
# 4  Student5   West High     A     96

print(df.tail())
#          Name      School Grade  Score
# 15  Student16  North High     C     76
# 16  Student17  South High     A     97
# 17  Student18  South High     C     72
# 18  Student19  South High     C     70
# 19  Student20   West High     A     93

print(df.shape) # returns (rows, columns)
# (20, 4)

print(df.columns)
# Index(['Name', 'School', 'Grade', 'Score'], dtype='object')

print(df.describe())
#            Score
# count  20.000000
# mean   80.050000
# std    19.789617
# min     6.000000
# 25%    77.500000
# 50%    83.000000
# 75%    91.250000
# max    99.000000

print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 20 entries, 0 to 19
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   Name    20 non-null     object
#  1   School  20 non-null     object
#  2   Grade   20 non-null     object
#  3   Score   20 non-null     int64 
# dtypes: int64(1), object(3)
# memory usage: 772.0+ bytes
# None

print(df["Score"])
# 0     92
# 1      6
# 2     64
# 3     88
# 4     96
# 5     91
# 6     83
# 7     78
# 8     81
# 9     89
# 10    78
# 11    99
# 12    84
# 13    81
# 14    83
# 15    76
# 16    97
# 17    72
# 18    70
# 19    93
# Name: Score, dtype: int64

print(df[["Name", "School"]])
#          Name      School
# 0    Student1   West High
# 1    Student2  South High
# 2    Student3  North High
# 3    Student4   West High
# 4    Student5   West High
# 5    Student6  South High
# 6    Student7  North High
# 7    Student8  North High
# 8    Student9   West High
# 9   Student10   East High
# 10  Student11   West High
# 11  Student12   West High
# 12  Student13   West High
# 13  Student14   West High
# 14  Student15  South High
# 15  Student16  North High
# 16  Student17  South High
# 17  Student18  South High
# 18  Student19  South High
# 19  Student20   West High

print(df.loc[0])
# Name       Student1
# School    West High
# Grade             A
# Score            92
# Name: 0, dtype: object

print(df.loc[0:2])
#        Name      School Grade  Score
# 0  Student1   West High     A     92
# 1  Student2  South High     F      6
# 2  Student3  North High     D     64

print(df.iloc[0:2])
#        Name      School Grade  Score
# 0  Student1   West High     A     92
# 1  Student2  South High     F      6

print(df.loc[[0, 5]])
#        Name      School Grade  Score
# 0  Student1   West High     A     92
# 5  Student6  South High     A     91

print(df.loc[0:2, "Name"])
# 0    Student1
# 1    Student2
# 2    Student3
# Name: Name, dtype: object

print(df.loc[0:2, ["Name", "Grade"]])
#        Name Grade
# 0  Student1     A
# 1  Student2     F
# 2  Student3     D

print(df.iloc[0])
# Name       Student1
# School    West High
# Grade             A
# Score            92
# Name: 0, dtype: object

print(df.iloc[0:2, 0:2])
#        Name      School
# 0  Student1   West High
# 1  Student2  South High

print(df.loc[0:2, ["Name", "Score"]])
#        Name  Score
# 0  Student1     92
# 1  Student2      6
# 2  Student3     64
print(df[df["School"] == "West High"])
#          Name     School Grade  Score
# 0    Student1  West High     A     92
# 3    Student4  West High     B     88
# 4    Student5  West High     A     96
# 8    Student9  West High     B     81
# 10  Student11  West High     C     78
# 11  Student12  West High     A     99
# 12  Student13  West High     B     84
# 13  Student14  West High     B     81
# 19  Student20  West High     A     93
print(df.iloc[-2:, [0,-1]])
#          Name  Score
# 18  Student19     70
# 19  Student20     93
print(df.loc[::-1])
#          Name      School Grade  Score
# 19  Student20   West High     A     93
# 18  Student19  South High     C     70
# 17  Student18  South High     C     72
# 16  Student17  South High     A     97
# 15  Student16  North High     C     76
# 14  Student15  South High     B     83
# 13  Student14   West High     B     81
# 12  Student13   West High     B     84
# 11  Student12   West High     A     99
# 10  Student11   West High     C     78
# 9   Student10   East High     B     89
# 8    Student9   West High     B     81
# 7    Student8  North High     C     78
# 6    Student7  North High     B     83
# 5    Student6  South High     A     91
# 4    Student5   West High     A     96
# 3    Student4   West High     B     88
# 2    Student3  North High     D     64
# 1    Student2  South High     F      6
# 0    Student1   West High     A     92
print(df.sort_values(by="Score", ascending=False))
#          Name      School Grade  Score
# 11  Student12   West High     A     99
# 16  Student17  South High     A     97
# 4    Student5   West High     A     96
# 19  Student20   West High     A     93
# 0    Student1   West High     A     92
# 5    Student6  South High     A     91
# 9   Student10   East High     B     89
# 3    Student4   West High     B     88
# 12  Student13   West High     B     84
# 6    Student7  North High     B     83
# 14  Student15  South High     B     83
# 13  Student14   West High     B     81
# 8    Student9   West High     B     81
# 7    Student8  North High     C     78
# 10  Student11   West High     C     78
# 15  Student16  North High     C     76
# 17  Student18  South High     C     72
# 18  Student19  South High     C     70
# 2    Student3  North High     D     64
# 1    Student2  South High     F      6
print(df[df["Score"] > 80])
#          Name      School Grade  Score
# 0    Student1   West High     A     92
# 3    Student4   West High     B     88
# 4    Student5   West High     A     96
# 5    Student6  South High     A     91
# 6    Student7  North High     B     83
# 8    Student9   West High     B     81
# 9   Student10   East High     B     89
# 11  Student12   West High     A     99
# 12  Student13   West High     B     84
# 13  Student14   West High     B     81
# 14  Student15  South High     B     83
# 16  Student17  South High     A     97
# 19  Student20   West High     A     93
print("West High:", df[df["School"] == "West High"]["Score"].mean())
print("East High:", df[df["School"] == "East High"]["Score"].mean())
print("North High:", df[df["School"] == "North High"]["Score"].mean())
print("South High:", df[df["School"] == "South High"]["Score"].mean())
# West High: 88.0
# East High: 89.0
# North High: 75.25
# South High: 69.83333333333333