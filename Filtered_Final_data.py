import pandas as pd

# 1. Read Dataset
file_path = 'filtered_players_all_match_type.csv'  # Replace with your file name
df = pd.read_csv(file_path)

# 2. Ensure Unique Data for Each Player in Each Tournament
# Check if the data is unique
is_unique = df.groupby(['Player', 'Tournament','Rounds Played']).size().max() == 1
if is_unique:
    print("The data is unique per player per tournament.")
else:
    print("The data is not unique. Re-grouping or further checks are needed.")

# Get the row with the maximum rounds played for each player in each tournament
df_max_round = df.loc[df.groupby(['Tournament', 'Player'])['Rounds Played'].idxmax()]

# c. Save Filtered Data (Optional)
df_max_round.to_csv('filtered_data.csv', index=False)
print("The filtered data has been saved to 'filtered_data.csv'")
