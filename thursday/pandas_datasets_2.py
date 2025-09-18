import pandas as pd

df = pd.read_csv("thursday/students_data_messy.csv")
df.head()
# Name	School	Grade	Score	Age	Attendance	Extracurricular	Email
# 0	Student1	South High	B	58.2	18.0	97.0	Sports	NaN
# 1	Student2	NaN	F	35.5	17.0	78.0	NaN	student2@school.edu
# 2	Student3	NaN	C	77.7	17.0	87.0	Art	student3@school.edu
# 3	Student4	West High	F	23.1	16.0	96.0	Science Club	student4@school.edu
# 4	NaN	North High	F	90.2	16.0	100.0	NaN	NaN

df_dropped = df.dropna()
df_dropped.head()
# Name	School	Grade	Score	Age	Attendance	Extracurricular	Email
# 3	Student4	West High	F	23.1	16.0	96.0	Science Club	student4@school.edu
# 6	Student7	West High	B	48.1	18.0	88.0	Sports	student7@school.edu
# 9	Student10	South High	C	18.3	17.0	91.0	Science Club	student10@school.edu
# 10	Student11	South High	D	16.9	18.0	79.0	Science Club	student11@school.edu
# 13	Student14	North High	C	24.3	17.0	84.0	Science Club	student14@school.edu

df_dropped_cols = df.dropna(subset=["Age"])
df_dropped_cols.head()
# Name	School	Grade	Score	Age	Attendance	Extracurricular	Email
# 0	Student1	South High	B	58.2	18.0	97.0	Sports	NaN
# 1	Student2	NaN	F	35.5	17.0	78.0	NaN	student2@school.edu
# 2	Student3	NaN	C	77.7	17.0	87.0	Art	student3@school.edu
# 3	Student4	West High	F	23.1	16.0	96.0	Science Club	student4@school.edu
# 4	NaN	North High	F	90.2	16.0	100.0	NaN	NaN

df["Age_Filled"] = df["Age"].fillna(0)
df.head(20)
# Name	School	Grade	Score	Age	Attendance	Extracurricular	Email	Age_Filled
# 0	Student1	South High	B	58.2	18.0	97.0	Sports	NaN	18.0
# 1	Student2	NaN	F	35.5	17.0	78.0	NaN	student2@school.edu	17.0
# 2	Student3	NaN	C	77.7	17.0	87.0	Art	student3@school.edu	17.0
# 3	Student4	West High	F	23.1	16.0	96.0	Science Club	student4@school.edu	16.0
# 4	NaN	North High	F	90.2	16.0	100.0	NaN	NaN	16.0
# 5	NaN	West High	F	88.8	18.0	99.0	NaN	NaN	18.0
# 6	Student7	West High	B	48.1	18.0	88.0	Sports	student7@school.edu	18.0
# 7	Student8	West High	C	7.8	16.0	NaN	NaN	student8@school.edu	16.0
# 8	Student9	South High	D	68.0	17.0	99.0	NaN	student9@school.edu	17.0
# 9	Student10	South High	C	18.3	17.0	91.0	Science Club	student10@school.edu	17.0
# 10	Student11	South High	D	16.9	18.0	79.0	Science Club	student11@school.edu	18.0
# 11	Student12	North High	F	37.5	17.0	NaN	Art	student12@school.edu	17.0
# 12	Student13	North High	F	69.7	18.0	96.0	NaN	student13@school.edu	18.0
# 13	Student14	North High	C	24.3	17.0	84.0	Science Club	student14@school.edu	17.0
# 14	Student15	South High	F	72.7	17.0	96.0	NaN	student15@school.edu	17.0
# 15	Student16	North High	A	62.6	18.0	100.0	NaN	student16@school.edu	18.0
# 16	Student17	South High	B	11.7	17.0	NaN	Sports	student17@school.edu	17.0
# 17	Student18	South High	B	85.7	17.0	95.0	Art	student18@school.edu	17.0
# 18	Student19	South High	F	51.8	16.0	82.0	NaN	student19@school.edu	16.0
# 19	Student20	NaN	A	NaN	NaN	84.0	Art	student20@school.edu	0.0

df["Score_Filled"] = df["Score"].fillna(df["Score"].mean())
df.head(20)
# Name	School	Grade	Score	Age	Attendance	Extracurricular	Email	Age_Filled	Score_Filled
# 0	Student1	South High	B	58.2	18.0	97.0	Sports	NaN	18.0	58.200000
# 1	Student2	NaN	F	35.5	17.0	78.0	NaN	student2@school.edu	17.0	35.500000
# 2	Student3	NaN	C	77.7	17.0	87.0	Art	student3@school.edu	17.0	77.700000
# 3	Student4	West High	F	23.1	16.0	96.0	Science Club	student4@school.edu	16.0	23.100000
# 4	NaN	North High	F	90.2	16.0	100.0	NaN	NaN	16.0	90.200000
# 5	NaN	West High	F	88.8	18.0	99.0	NaN	NaN	18.0	88.800000
# 6	Student7	West High	B	48.1	18.0	88.0	Sports	student7@school.edu	18.0	48.100000
# 7	Student8	West High	C	7.8	16.0	NaN	NaN	student8@school.edu	16.0	7.800000
# 8	Student9	South High	D	68.0	17.0	99.0	NaN	student9@school.edu	17.0	68.000000
# 9	Student10	South High	C	18.3	17.0	91.0	Science Club	student10@school.edu	17.0	18.300000
# 10	Student11	South High	D	16.9	18.0	79.0	Science Club	student11@school.edu	18.0	16.900000
# 11	Student12	North High	F	37.5	17.0	NaN	Art	student12@school.edu	17.0	37.500000
# 12	Student13	North High	F	69.7	18.0	96.0	NaN	student13@school.edu	18.0	69.700000
# 13	Student14	North High	C	24.3	17.0	84.0	Science Club	student14@school.edu	17.0	24.300000
# 14	Student15	South High	F	72.7	17.0	96.0	NaN	student15@school.edu	17.0	72.700000
# 15	Student16	North High	A	62.6	18.0	100.0	NaN	student16@school.edu	18.0	62.600000
# 16	Student17	South High	B	11.7	17.0	NaN	Sports	student17@school.edu	17.0	11.700000
# 17	Student18	South High	B	85.7	17.0	95.0	Art	student18@school.edu	17.0	85.700000
# 18	Student19	South High	F	51.8	16.0	82.0	NaN	student19@school.edu	16.0	51.800000
# 19	Student20	NaN	A	NaN	NaN	84.0	Art	student20@school.edu	0.0	50.804444

older_than_seventeen = df[df["Age"] > 17]
older_than_seventeen.head()
# Name	School	Grade	Score	Age	Attendance	Extracurricular	Email	Age_Filled	Score_Filled
# 0	Student1	South High	B	58.2	18.0	97.0	Sports	NaN	18.0	58.2
# 5	NaN	West High	F	88.8	18.0	99.0	NaN	NaN	18.0	88.8
# 6	Student7	West High	B	48.1	18.0	88.0	Sports	student7@school.edu	18.0	48.1
# 10	Student11	South High	D	16.9	18.0	79.0	Science Club	student11@school.edu	18.0	16.9
# 12	Student13	North High	F	69.7	18.0	96.0	NaN	student13@school.edu	18.0	69.7

high_score = df[(df["Age"] > 17) & (df["Score"] > 85)]
high_score.head(20)
# Name	School	Grade	Score	Age	Attendance	Extracurricular	Email	Age_Filled	Score_Filled
# 5	NaN	West High	F	88.8	18.0	99.0	NaN	NaN	18.0	88.8
# 36	Student37	South High	A	99.3	18.0	90.0	Art	NaN	18.0	99.3

df_renamed = df.rename(columns={"Age": "Age_Years", "Score": "Test_Score"})
df_renamed.head()
# Name	School_Name	Grade_Level	Test_Score	Age_Years	Attendance_Rate	Club	Email_Address	Age_Years_Filled	Test_Score_Filled
# 0	Student1	South High	B	58.2	18.0	97.0	Sports	NaN	18.0	58.2
# 1	Student2	NaN	F	35.5	17.0	78.0	NaN	student2@school.edu	17.0	35.5
# 2	Student3	NaN	C	77.7	17.0	87.0	Art	student3@school.edu	17.0	77.7
# 3	Student4	West High	F	23.1	16.0	96.0	Science Club	student4@school.edu	16.0	23.1
# 4	NaN	North High	F	90.2	16.0	100.0	NaN	NaN	16.0	90.2

df.columns = ["Name", "School_Name", "Grade_Level", "Test_Score", "Age_Years", "Attendance_Rate", "Club", "Email_Address", "Age_Years_Filled", "Test_Score_Filled"]
df.head()
# Name	School_Name	Grade_Level	Test_Score	Age_Years	Attendance_Rate	Club	Email_Address	Age_Years_Filled	Test_Score_Filled
# 0	Student1	South High	B	58.2	18.0	97.0	Sports	NaN	18.0	58.2
# 1	Student2	NaN	F	35.5	17.0	78.0	NaN	student2@school.edu	17.0	35.5
# 2	Student3	NaN	C	77.7	17.0	87.0	Art	student3@school.edu	17.0	77.7
# 3	Student4	West High	F	23.1	16.0	96.0	Science Club	student4@school.edu	16.0	23.1
# 4	NaN	North High	F	90.2	16.0	100.0	NaN	NaN	16.0	90.2
