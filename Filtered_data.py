import pandas as pd

# 1. Read Dataset
file_path = 'preprocessed_players_stats.csv'  # Preprocessed file
df = pd.read_csv(file_path)

# 2. Filter Data Based on Match Type "All"
filtered_df = df[df['Match Type'] == 'All Match Types']  # Adjust column name 'Match_Type' if different
print(f"Number of data after filtering by Match Type 'All Match Types': {len(filtered_df)}")

# 4. Save the Filtered Data (Optional)
filtered_df.to_csv('filtered_players_all_match_type.csv', index=False)
print("Filtered data has been saved to 'filtered_players_all_match_type.csv'")
