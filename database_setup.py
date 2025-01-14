import pandas as pd
import sqlite3

# 1. Reading the CSV file
file_path = "Player_stats_franchise.csv"  # Replace with your file name
data = pd.read_csv(file_path)

# 2. Creating a connection to the SQLite database
db_path = 'valorant_stats.db'  # Database file name
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 3. Creating a table according to the dataset
cursor.execute('''
CREATE TABLE IF NOT EXISTS players_stats (
    Tournament TEXT,
    Stage TEXT,
    Match_Type TEXT,
    Player TEXT,
    Teams TEXT,
    Agents TEXT,
    Rounds_Played INTEGER,
    Rating REAL,
    Average_Combat_Score INTEGER,
    Kills_Deaths REAL,
    Kill_Assist_Trade_Survive_Percentage TEXT,
    Average_Damage_Per_Round REAL,
    Kills_Per_Round REAL,
    Assists_Per_Round REAL,
    First_Kills_Per_Round REAL,
    First_Deaths_Per_Round REAL,
    Headshot_Percentage TEXT,
    Clutch_Success_Percentage TEXT,
    Clutches_Won_Played TEXT,
    Maximum_Kills_in_a_Single_Map INTEGER,
    Kills INTEGER,
    Deaths INTEGER,
    Assists INTEGER,
    First_Kills INTEGER,
    First_Deaths INTEGER
)
''')
conn.commit()  # Save changes

# 4. Inserting data from CSV into the SQLite table
data.to_sql('players_stats', conn, if_exists='replace', index=False)

# 5. Checking the number of entries in the table
cursor.execute("SELECT COUNT(*) FROM players_stats")
count = cursor.fetchone()[0]
print(f"Number of entries in the table: {count}")

# Closing the connection
conn.close()
