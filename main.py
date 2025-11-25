import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
df= pd.read_csv("fifa_players.csv")
# type_count = df[""].value_counts()
# plt.bar(type_count.index, type_count.values)
# plt.show()

#DATA CLEANING
cols_to_drop = [
    "release_clause_euro", "national_jersey_number", "wage_euro",
    "body_type", "international_reputation(1-5)", "skill_moves(1-5)", "weak_foot(1-5)", "aggression", 
    "interceptions", "standing_tackle", "sliding_tackle", "marking", "national_team_position", 
    "national_rating", "penalties", "stamina", "strength"
]
df = df.drop(columns=cols_to_drop, errors='ignore')
df.replace('', np.nan, inplace=True)
df_cleaned= df.dropna(axis=1, how='any')


#Visualization of Data

plt.hist(df_cleaned["age"], bins=10, edgecolor="black")
plt.title("Age Distribution of Players with Rating")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

top_countries = df_cleaned["nationality"].value_counts().head(10)
plt.bar(top_countries.index, top_countries.values)
plt.xticks(rotation=45)
plt.title("Top 10 Nationalities by Player Count")
plt.show()

foot_counts = df_cleaned["preferred_foot"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(foot_counts.values, labels=foot_counts.index, autopct='%1.1f%%')
plt.title("Preferred Foot Distribution")
plt.show()

plt.hist2d(df['age'], df['overall_rating'], bins=(25, 20))
plt.colorbar()
plt.xlabel("Age")
plt.ylabel("Rating")
plt.title("2D Density of Age vs Rating")
plt.show()
