import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Read Dataset
file_path = 'clustered_players.csv'  # Replace with your file name
df = pd.read_csv(file_path)

# 2. Create Performance Label Based on 'Rating'
# Define performance categories: High (>= 0.5), Medium (0.3 - 0.5), Low (< 0.3)
def classify_performance(rating):
    if rating >= 0.5:
        return "Best Perform"
    elif 0.3 <= rating < 0.5:
        return "Normal Perform"
    else:
        return "Under Perform"

df['Performance'] = df['Rating'].apply(classify_performance)

# 3. Select Features and Labels
features = df[['Average Combat Score', 'Kills:Deaths', 'Kill, Assist, Trade, Survive %', 'Average Damage Per Round',
                'Kills Per Round', 'Assists Per Round', 'First Kills Per Round', 'First Deaths Per Round', 'Headshot %', 
                'Clutch Success %', 'Maximum Kills in a Single Map', 'Kills', 'Deaths', 'Assists', 'First Kills', 'First Deaths']]  # Select features
labels = df['Performance']

# 4. Split Data into Train and Test Sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# 5. Build Random Forest Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate the Model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 7. Save the Model (Optional)
import joblib
joblib.dump(model, 'player_performance_model.pkl')
print("The model has been saved to 'player_performance_model.pkl'")
