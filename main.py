import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df= pd.read_csv("fifa_players.csv")

#Data Cleaning
cols_to_drop = [
    "release_clause_euro", "national_jersey_number", "wage_euro",
    "body_type", "international_reputation(1-5)", "skill_moves(1-5)", "weak_foot(1-5)", "aggression", 
    "interceptions", "standing_tackle", "sliding_tackle", "marking", "national_team_position", 
    "national_rating", "penalties", "stamina", "strength"
]
df = df.drop(columns=cols_to_drop, errors='ignore')
df.replace('', np.nan, inplace=True)
cols_with_nan = [col for col in df.columns if df[col].isna().any() and col != "value_euro"]
df_cleaned = df.drop(columns=cols_with_nan)
df_cleaned = df_cleaned.dropna(subset=["overall_rating", "value_euro"])


#Visualization of Data

#Distribution
plt.hist(df_cleaned["age"], bins=10, edgecolor="black")
plt.title("Age Distribution of Players with Rating")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

#Bar Graph of Top 10 Nationalities by Player Count
top_countries = df_cleaned["nationality"].value_counts().head(10)
plt.bar(top_countries.index, top_countries.values)
plt.xticks(rotation=45)
plt.title("Top 10 Nationalities by Player Count")
plt.show()

#Pie Chart of Preferred Foot
foot_counts = df_cleaned["preferred_foot"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(foot_counts.values, labels=foot_counts.index, autopct='%1.1f%%')
plt.title("Preferred Foot Distribution")
plt.show()

#2D Heatmap Of Age and Overall Rating
plt.hist2d(df['age'], df['overall_rating'], bins=(25, 20))
plt.colorbar()
plt.xlabel("Age")
plt.ylabel("Rating")
plt.title("2D Density of Age vs Rating")
plt.show()

#Scatterplot for Height in cm and Heading Accuracy
sns.scatterplot(data=df_cleaned, x="height_cm", y="heading_accuracy")
plt.show()

#Stripplot for Weight in KGs and Acceleration
sns.stripplot(data=df_cleaned, x="weight_kgs", y="acceleration")
plt.show()

#Regression Plot for Overall Rating and Value of Players In Euro
sns.regplot(data=df_cleaned, x="overall_rating", y="value_euro")
plt.show()

#Joint Plot
sns.jointplot(data=df_cleaned, x="overall_rating", y="value_euro", hue="preferred_foot")
plt.show()

X = df_cleaned[["overall_rating"]]  # features
y = df_cleaned["value_euro"]        # target

mod= LinearRegression()
mod.fit(X,y)
mod.predict(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Model trained successfully!")
print(f"Test set MSE: {mean_squared_error(y_test, y_pred):.2f}")
print(f"Test set Variance: {r2_score(y_test, y_pred):.4f}")