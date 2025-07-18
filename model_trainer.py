import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle

# Load data
df = pd.read_csv("Cleaned_Indian_Food_Dataset.csv")

# Fill missing values
df['Cleaned-Ingredients'] = df['Cleaned-Ingredients'].fillna("")

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Cleaned-Ingredients'])

# KNN Model
knn = NearestNeighbors(n_neighbors=10, metric='cosine')
knn.fit(X)

# Save model and vectorizer
pickle.dump(knn, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
df.to_csv("final_dataset.csv", index=False)  # Save clean version
