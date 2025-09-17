import numpy as np
import pandas as pd

df = pd.read_csv('gold_price_data.csv')
gold_price = np.array(df["close"])

print("Mean closing price:", np.mean(gold_price))
print("Median closing price:", np.median(gold_price))
print("Standard Deviation closing price:", np.std(gold_price))
max_close = np.max(gold_price)
print("Max closing price:", max_close)
print("Min closing price:", np.min(gold_price))
print("Range closing price:", max_close - np.min(gold_price))
print("Date of max close:", np.array(df[df["close"] == max_close]["date"])[0])

print("First month:", gold_price[:30])
print("Last month:", gold_price[-30:])
monthly_chunks = np.array_split(gold_price, len(gold_price) // 30 + (len(gold_price) % 30 != 0))
monthly_means_30 = np.mean(monthly_chunks[:-5], axis=1)
# print(monthly_means_30)
monthly_means_29 = np.mean(monthly_chunks[-5:], axis=1)
# print(monthly_means_29)
monthly_means = np.append(monthly_means_30, monthly_means_29)
print(monthly_means)
print(f"The first month's mean closing price is {monthly_means[0]}, whereas the last month's mean closing price is {monthly_means[-1]}")

differences = np.diff(gold_price, axis=0)
print("Daily close differences:", differences)
# >0 means increase from one day to the next
# <0 means decrease from one day to the next
max_increase = np.max(differences)
max_decrease = np.min(differences)
print("Largest increase:", max_increase)
print("Largest decrease:", max_decrease)
max_inc_index = np.argmax(differences)
max_dec_index = np.argmin(differences)
print(f"Largest increase dates: {np.array(df["date"])[max_inc_index]} to {np.array(df["date"])[max_inc_index+1]}")
print(f"Largest decrease dates: {np.array(df["date"])[max_dec_index]} to {np.array(df["date"])[max_dec_index+1]}")