import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Baca Data Preprocessed
file_path = "clustered_players.csv"  # Nama file untuk menyimpan  
df = pd.read_csv(file_path)

# 2. Pilih Fitur untuk Clustering
features = ['Average Combat Score', 'Kills:Deaths','Kill, Assist, Trade, Survive %', 'Average Damage Per Round',
            'Kills Per Round', 'Assists Per Round', 'First Kills Per Round','First Deaths Per Round', 'Headshot %', 
            'Clutch Success %', 'Maximum Kills in a Single Map', 'Kills','Deaths', 'Assists', 'First Kills', 'First Deaths']  # Sesuaikan dengan nama kolom

# Pastikan kolom tersedia dalam data
for col in features:
    if col not in df.columns:
        raise ValueError(f"Kolom '{col}' tidak ditemukan dalam dataset.")

X = df[features]  # Dataset untuk clustering

# 3. Clustering dengan K-Means
n_clusters = 3  # Tentukan jumlah cluster
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)
df['Cluster'] = df['Cluster'].replace({
    0: 'Normal Perform',
    1: 'Best Perform',
    2: 'Under Perform'})

# 4. Visualisasi Cluster
plt.figure(figsize=(8, 6))
cluster_labels = {
    0: "Best Perform",
    1: "Normal Perform",
    2: "Under Perform"
}
for cluster in range(n_clusters):
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(
        cluster_data['Kills'], 
        cluster_data['Average Combat Score'], 
        label=cluster_labels[cluster] 
    )

plt.xlabel('Kills')
plt.ylabel('ACS)')
plt.title('Clustering Performa Pemain Franchise Valorant di Tahun 2024 (Setiap Turnament)')
plt.legend()
plt.show()

# 5. Analisis Cluster
print("Jumlah pemain di setiap cluster:")
print(df['Cluster'].value_counts())

print("\nStatistik rata-rata untuk setiap cluster:")
print(df.groupby('Cluster')[features].mean())

# 6. Simpan Hasil Clustering ke CSV
output_file = "clustered_players.csv"  # Nama file untuk menyimpan
df.to_csv(output_file, index=False)    # Simpan tanpa index
print(f"Hasil clustering berhasil disimpan ke {output_file}")
