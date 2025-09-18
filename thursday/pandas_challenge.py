import pandas as pd

df = pd.read_csv("thursday/sales_with_nans.csv")
df.head()
# Group	Customer_Segment	Sales_Before	Sales_After	Customer_Satisfaction_Before	Customer_Satisfaction_After	Purchase_Made
# 0	Control	High Value	240.548359	300.007568	74.684767	NaN	No
# 1	Treatment	High Value	246.862114	381.337555	100.000000	100.000000	Yes
# 2	Control	High Value	156.978084	179.330464	98.780735	100.000000	No
# 3	Control	Medium Value	192.126708	229.278031	49.333766	39.811841	Yes
# 4	NaN	High Value	229.685623	NaN	83.974852	87.738591	Yes

df["Group"] = df["Group"].fillna("Unknown")
df["Customer_Segment"] = df["Customer_Segment"].fillna("Unknown")
df["Sales_Before"] = df["Sales_Before"].fillna(df["Sales_Before"].mean())
df["Sales_After"] = df["Sales_After"].fillna(df["Sales_After"].mean())
df["Customer_Satisfaction_Before"] = df["Customer_Satisfaction_Before"].fillna(df["Customer_Satisfaction_Before"].mean())
df["Customer_Satisfaction_After"] = df["Customer_Satisfaction_After"].fillna(df["Customer_Satisfaction_After"].mean())
df["Purchase_Made"] = df["Purchase_Made"].fillna("Unknown")
df.head()
# Group	Customer_Segment	Sales_Before	Sales_After	Customer_Satisfaction_Before	Customer_Satisfaction_After	Purchase_Made
# 0	Control	High Value	240.548359	300.007568	74.684767	73.872593	No
# 1	Treatment	High Value	246.862114	381.337555	100.000000	100.000000	Yes
# 2	Control	High Value	156.978084	179.330464	98.780735	100.000000	No
# 3	Control	Medium Value	192.126708	229.278031	49.333766	39.811841	Yes
# 4	Unknown	High Value	229.685623	280.457952	83.974852	87.738591	Yes

total_sales_before = df["Sales_Before"].sum()
print("Total Sales Before:", total_sales_before)
# Total Sales Before: 2037169.9822858854

total_sales_after = df["Sales_After"].sum()
print("Total Sales After:", total_sales_after)
# Total Sales After: 2804579.522065458

average_sales_before = df["Sales_Before"].mean()
print("Average Sales Before:", average_sales_before)
# Average Sales Before: 203.71699822858855

average_sales_after = df["Sales_After"].mean()
print("Average Sales After:", average_sales_after)
# Average Sales After: 280.45795220654577

average_satisfaction_before = df["Customer_Satisfaction_Before"].mean()
print("Average Satisfaction Before:", average_satisfaction_before)
 #Average Satisfaction Before: 70.25207641696217

average_satisfaction_after = df["Customer_Satisfaction_After"].mean()
print("Average Satisfaction After:", average_satisfaction_after)
# Average Satisfaction After: 73.87259310735004

maximum_sales_before = df["Sales_Before"].max()
print("Maximum Sales Before:", maximum_sales_before)
# Maximum Sales Before: 545.4225471380589

minimum_sales_before = df["Sales_Before"].min()
print("Minimum Sales Before:", minimum_sales_before)
# Minimum Sales Before: 24.85296575372195

maximum_sales_after = df["Sales_After"].max()
print("Maximum Sales After:", maximum_sales_after)
# Maximum Sales After: 818.2199974644652

minimum_sales_after = df["Sales_After"].min()
print("Minimum Sales After:", minimum_sales_after)
# Minimum Sales After: 32.414352282538246

print(f"Change in average sales: {average_sales_after-average_sales_before}")
print(f"Change in average customer satisfaction: {average_satisfaction_after-average_satisfaction_before}")
# Change in average sales: 76.74095397795722
# Change in average customer satisfaction: 3.6205166903878734

control_group = df[df["Group"] == "Control"]
control_group.head()
# Group	Customer_Segment	Sales_Before	Sales_After	Customer_Satisfaction_Before	Customer_Satisfaction_After	Purchase_Made
# 0	Control	High Value	240.548359	300.007568	74.684767	73.872593	No
# 2	Control	High Value	156.978084	179.330464	98.780735	100.000000	No
# 3	Control	Medium Value	192.126708	229.278031	49.333766	39.811841	Yes
# 6	Control	High Value	191.713918	222.409356	89.967827	85.120975	Yes
# 7	Control	Low Value	173.752555	213.168232	66.984711	67.881558	Unknown

above_average_sales = df[(df["Sales_Before"] > df["Sales_Before"].mean()) & (df["Sales_After"] > df["Sales_After"].mean())]
above_average_sales.head()
# Group	Customer_Segment	Sales_Before	Sales_After	Customer_Satisfaction_Before	Customer_Satisfaction_After	Purchase_Made
# 0	Control	High Value	240.548359	300.007568	74.684767	73.872593	No
# 1	Treatment	High Value	246.862114	381.337555	100.000000	100.000000	Yes
# 9	Treatment	High Value	235.071493	352.756872	72.919851	70.753225	No
# 16	Treatment	Unknown	306.701452	485.135424	77.431662	78.361282	Unknown
# 20	Treatment	High Value	225.163165	355.210451	70.252076	95.054317	No

high_sales_and_high_value = df[(df["Sales_Before"] > df["Sales_Before"].mean()) & (df["Sales_After"] > df["Sales_After"].mean()) & (df["Customer_Segment"] == "High Value")]
high_sales_and_high_value.head()
# Group	Customer_Segment	Sales_Before	Sales_After	Customer_Satisfaction_Before	Customer_Satisfaction_After	Purchase_Made
# 0	Control	High Value	240.548359	300.007568	74.684767	73.872593	No
# 1	Treatment	High Value	246.862114	381.337555	100.000000	100.000000	Yes
# 9	Treatment	High Value	235.071493	352.756872	72.919851	70.753225	No
# 20	Treatment	High Value	225.163165	355.210451	70.252076	95.054317	No
# 34	Unknown	High Value	226.643858	355.984459	79.272267	73.872593	No

df_2 = pd.read_csv("thursday/sales_with_nans.csv")
df_dropped_cols = df_2.dropna(subset=["Sales_Before", "Sales_After"])
df_dropped_cols.head()
# Group	Customer_Segment	Sales_Before	Sales_After	Customer_Satisfaction_Before	Customer_Satisfaction_After	Purchase_Made
# 0	Control	High Value	240.548359	300.007568	74.684767	NaN	No
# 1	Treatment	High Value	246.862114	381.337555	100.000000	100.000000	Yes
# 2	Control	High Value	156.978084	179.330464	98.780735	100.000000	No
# 3	Control	Medium Value	192.126708	229.278031	49.333766	39.811841	Yes
# 5	Treatment	NaN	135.573003	218.559988	58.075342	69.404918	No

average_sales_by_customer_segment = df.groupby("Customer_Segment").agg(
    Average_Sales_Before=("Sales_After", "mean"),
    Average_Sales_After=("Sales_After" ,"mean")
)
average_sales_by_customer_segment
# Average_Sales_Before	Average_Sales_After
# Customer_Segment		
# High Value	305.954647	305.954647
# Low Value	254.066006	254.066006
# Medium Value	281.125125	281.125125
# Unknown	281.562844	281.562844

df["Satisfaction_Improvement"] = df["Customer_Satisfaction_After"]-df["Customer_Satisfaction_Before"]
average_satisfaction_improvement_by_group = df[df["Group"] != "Unknown"].groupby("Group").agg(
    Average_Satisfaction_Improvement=("Satisfaction_Improvement", "mean")
)
average_satisfaction_improvement_by_group
# Average_Satisfaction_Improvement
# Group	
# Control	3.620321
# Treatment	3.684737

df["Sales_Increase"] = df["Sales_After"]-df["Sales_Before"]
sales_increase_by_customer_segment = df.groupby("Customer_Segment").agg(
    Sales_Increase=("Sales_Increase", "max")
)
sales_increase_by_customer_segment.sort_values("Sales_Increase", ascending=False).head(1)
# Sales_Increase
# Customer_Segment	
# High Value	475.17816
