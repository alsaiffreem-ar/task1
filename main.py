import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()

print("CSV Data:")
print(df)

plt.bar(df["Name"], df["Age"])
plt.xlabel("Name")
plt.ylabel("Age")
plt.title("Age of People")
plt.show()
