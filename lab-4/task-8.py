import pandas as pd

df = pd.read_csv("countries.csv")

print(df.nsmallest(10, "area"))
print(df.nlargest(10, "area"))

print(df.nsmallest(10, "population"))
print(df.nlargest(10, "population"))

print(df[df["languages"].str.contains("French", na=False)])

df.to_excel("result.xlsx")