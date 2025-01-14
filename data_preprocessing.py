import pandas as pd
import sqlite3
from sklearn.preprocessing import MinMaxScaler

# SQLite database location
db_path = r"C:\Users\Ubaidil\Downloads\FadhlanCode\PlayerstatsValorant\valorant_stats.db"

# Reading data from the database
conn = sqlite3.connect(db_path)
query = "SELECT * FROM players_stats"
df = pd.read_sql(query, conn)
conn.close()

# print("Available columns in the dataset:", df.columns)

# 1. Handling Missing Values
# Fill missing values in numerical columns with the mean
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

# Fill missing values in categorical columns with the mode
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

# Save the preprocessed data to a new file (optional)
output_path = 'preprocessed_players_stats.csv'
df.to_csv(output_path, index=False)
print(f"Preprocessed data has been saved to: {output_path}")
