import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('technologies_frequencies.csv', index_col=0)
print(df.sort_values(by="Frequency", ascending=True))
mean_data = df["Frequency"].mean()
print(mean_data)
df["Popularity"] = ""

for index, row in df.iterrows():
    if row["Frequency"] > mean_data:
        print(index + " Is more popular than average.")
        df.loc[index, "Popularity"] = "Popular"
    else:
        print(index + " Is less popular than average.")
        df.loc[index, "Popularity"] = "Not Popular"

print(df)
df.plot()
plt.title("Technology Frequencies In My Job Applications")
plt.xlabel("Technology")
plt.ylabel("Frequency")
#plt.savefig("technology_frequency_chart.png")  # Save the plot as a PNG file.
plt.show()