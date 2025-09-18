import pandas as pd
df = pd.read_csv("thursday/messy_cars.csv")
df["Miles"] = df["Miles"].fillna(df["Miles"].mean())
df["Money"] = df["Money"].fillna(df["Money"].mean())
df["Color"] = df["Color"].fillna("Unknown")
df["Brand"] = df["Brand"].fillna("Unknown")

df_clean = df.rename(columns={
    'Car_num': 'CarID',
    'Brand': 'Brand',
    'Mod': 'Model',
    'Yr': 'Year',
    'Money': 'Price',
    'Miles': 'Mileage',
    'Color': 'Color'
})

brand_totals = df_clean.groupby("Brand")["Mileage"].mean()
brand_totals
# Brand
# BMW          113058.800000
# Chevrolet     90362.600000
# Ford          98097.848485
# Honda        106102.848485
# Toyota        20527.000000
# Unknown      125466.750000
# Name: Mileage, dtype: float64

brand_totals.reset_index(name="Average Mileage")
# 	Brand	Average Mileage
# 0	BMW	113058.800000
# 1	Chevrolet	90362.600000
# 2	Ford	98097.848485
# 3	Honda	106102.848485
# 4	Toyota	20527.000000
# 5	Unknown	125466.750000

grouped_mod_colour = df_clean.groupby(["Model", "Color"]).agg(
    avg_prices=("Price", "mean"),
    total_cars=("CarID", "count")
)
grouped_mod_colour
# avg_prices	total_cars
# Model	Color		
# Convertible	Blue	44976.000	1
# Red	29253.000	1
# Unknown	28247.000	1
# Coupe	Black	22905.000	2
# Blue	42065.000	1
# Unknown	31240.950	1
# White	31240.950	1
# Hatchback	Blue	26271.000	1
# Green	46910.000	2
# Unknown	22262.000	1
# White	34127.000	1
# Yellow	35001.975	2
# SUV	Black	19886.000	2
# Blue	31240.950	1
# Red	31557.000	1
# White	43044.000	1
# Yellow	17185.000	1
# Sedan	Black	31240.950	1
# Green	14268.000	1
# Red	44099.000	1
# Yellow	29300.000	1

grouped_mod_colour.reset_index()
# Model	Color	avg_prices	total_cars
# 0	Convertible	Blue	44976.000	1
# 1	Convertible	Red	29253.000	1
# 2	Convertible	Unknown	28247.000	1
# 3	Coupe	Black	22905.000	2
# 4	Coupe	Blue	42065.000	1
# 5	Coupe	Unknown	31240.950	1
# 6	Coupe	White	31240.950	1
# 7	Hatchback	Blue	26271.000	1
# 8	Hatchback	Green	46910.000	2
# 9	Hatchback	Unknown	22262.000	1
# 10	Hatchback	White	34127.000	1
# 11	Hatchback	Yellow	35001.975	2
# 12	SUV	Black	19886.000	2
# 13	SUV	Blue	31240.950	1
# 14	SUV	Red	31557.000	1
# 15	SUV	White	43044.000	1
# 16	SUV	Yellow	17185.000	1
# 17	Sedan	Black	31240.950	1
# 18	Sedan	Green	14268.000	1
# 19	Sedan	Red	44099.000	1
# 20	Sedan	Yellow	29300.000	1

average_mileage_by_colour = df_clean.groupby("Color")["Mileage"].mean().reset_index(name="Average Mileage")
average_mileage_by_colour
# Color	Average Mileage
# 0	Black	79548.400000
# 1	Blue	93134.386364
# 2	Green	40199.181818
# 3	Red	88273.000000
# 4	Unknown	162601.666667
# 5	White	141208.666667
# 6	Yellow	105952.886364

average_price_by_brand = df_clean.groupby("Brand")["Price"].mean().reset_index(name="Max price")
average_price_by_brand
# Brand	Max price
# 0	BMW	31488.380000
# 1	Chevrolet	35584.390000
# 2	Ford	29977.666667
# 3	Honda	26584.991667
# 4	Toyota	49629.000000
# 5	Unknown	24239.737500

grouped_brand_colour = df_clean.groupby(["Brand", "Color"]).agg(
    total_cars=("CarID", "count")
)
grouped_brand_colour.reset_index()
# Brand	Color	total_cars
# 0	BMW	Black	2
# 1	BMW	Red	1
# 2	BMW	White	1
# 3	BMW	Yellow	1
# 4	Chevrolet	Blue	2
# 5	Chevrolet	Green	1
# 6	Chevrolet	Unknown	1
# 7	Chevrolet	Yellow	1
# 8	Ford	Black	1
# 9	Ford	Red	1
# 10	Ford	Yellow	1
# 11	Honda	Black	2
# 12	Honda	Blue	1
# 13	Honda	Green	1
# 14	Honda	Red	1
# 15	Honda	White	1
# 16	Toyota	Green	1
# 17	Toyota	White	1
# 18	Unknown	Blue	1
# 19	Unknown	Unknown	2
# 20	Unknown	Yellow	1

average_mileage_and_total_price_by_brand = df_clean.groupby("Brand").agg(
    Average_Mileage=("Mileage", "mean"),
    Total_Price=("Price", "sum")
)
average_mileage_and_total_price_by_brand
# Average_Mileage	Total_Price
# Brand		
# BMW	113058.800000	157441.90
# Chevrolet	90362.600000	177921.95
# Ford	98097.848485	89933.00
# Honda	106102.848485	159509.95
# Toyota	20527.000000	99258.00
# Unknown	125466.750000	96958.95

average_mileage_and_total_price_by_brand.reset_index()
# Brand	Average_Mileage	Total_Price
# 0	BMW	113058.800000	157441.90
# 1	Chevrolet	90362.600000	177921.95
# 2	Ford	98097.848485	89933.00
# 3	Honda	106102.848485	159509.95
# 4	Toyota	20527.000000	99258.00
# 5	Unknown	125466.750000	96958.95