import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

print(series.values)
print(series.index)
# [10 20 30 40 50]
# RangeIndex(start=0, stop=5, step=1)

print("Highest:", series.values.max())
print("Lowest:", series.values.min())
# Highest: 50
# Lowest: 10

series.index = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(series)
# Mon    10
# Tue    20
# Wed    30
# Thu    40
# Fri    50
# dtype: int64

data = {
    "Name": ["Ollie", "Sam", "Luke", "Liam"],
    "Age": [32, 27, 27, 30],
    "City": ["Reading", "London", "The North", "London"]
}

df = pd.DataFrame(data)
print(df)
#     Name  Age       City
# 0  Ollie   32    Reading
# 1    Sam   27     London
# 2   Luke   27  The North
# 3   Liam   30     London

data = {
    "Name": ["Sofa", "Chair", "Table"],
    "Price": [499.99, 25.50, 80.00],
    "Quantity": [1, 4, 2]
}
df = pd.DataFrame(data)
print(df)
#     Name   Price  Quantity
# 0   Sofa  499.99         1
# 1  Chair   25.50         4
# 2  Table   80.00         2

df['Total Value'] = df['Price'] * df['Quantity']
print(df)
#     Name   Price  Quantity  Total Value
# 0   Sofa  499.99         1       499.99
# 1  Chair   25.50         4       102.00
# 2  Table   80.00         2       160.00