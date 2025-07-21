
# 🍽️ CookWiseAI - Recipe Recommendation System

This is a smart **Recipe Recommendation Web App** built using **TF-IDF vectorization** and **K-Nearest Neighbors (KNN)** algorithm. The app allows users to input ingredients and apply soft filters like cuisine, time, and protein level(more filters like calorie,spice level,fibre,etc are to be added). It then recommends the top recipes using flexible scoring and semantic similarity.

---

## 🚀 Features

- Select ingredients from most commonly used list
- Optional filters for cuisine, cooking time, and protein level
- Soft filter mechanism: shows nearest results even if exact matches aren't found
- Clean and responsive Flask web interface

---

## 🧠 How it works

### 1. Data Preparation
- Dataset is cleaned and preprocessed (`Cleaned-Ingredients`, `Cuisine`, etc.)
- Most frequent ingredients are extracted for UI display
- Recipes are vectorized using TF-IDF on their cleaned ingredients

### 2. Model Building
- KNN model is trained on TF-IDF vectors of all recipes
- Cosine similarity is used to recommend similar recipes
- 
### 3. Why KNN ?
-We chose KNN (k-Nearest Neighbors) for our recipe recommendation system because it's simple, effective, and interpretable. Since we’re comparing recipes based on ingredients, KNN works well with TF-IDF vectorization to find similar recipes using cosine similarity. It doesn't require model training, which makes it perfect for a static dataset and quick experimentation. Unlike collaborative filtering or deep learning models, KNN is lightweight, doesn't need user history, and is easy to implement — making it the most practical choice for this use case.
- 
### 4. Soft Filtering (Post-processing)
- Recommended results are filtered based on user’s optional preferences (Cuisine, Time, Protein level)
- Even if no exact match is found, the top closest results are returned
Note:Classification algorithms like Naive Bayes or Decision Tree can be more relevent only if you predict cuisine/time given ingredients.
---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌶️
- HTML + CSS + JavaScript (for frontend)
- Scikit-learn (TF-IDF + KNN)
- Pandas, NumPy

---

## 💻 Local Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/CookWiseAI.git
cd CookWiseAI
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
#run once
python model_trainer.py
```

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000`

---

## 🤝 Contributing

1. Fork the repo and create your branch: `git checkout -b feature-name`
2. Make your changes and commit: `git commit -m 'Added feature'`
3. Push to your fork and submit a PR

---

## 📁 Folder Structure

```
CookWiseAI/
│
├── app.py                # Main Flask backend
├── model.pkl             # Trained KNN model
├── vectorizer.pkl        # Trained TF-IDF vectorizer
├── templates/
│   ├── index.html        # Input page UI
│   └── results.html      # Output recommendation UI
├── static/defaul.jpg      # CSS/JS files
├── data/
│   └── Cleaned_Indian_Food_Dataset.csv
├── requirements.txt
|__ model_trainer.py
└── README.md
```

---

## 📬 Contact

Made by [PARTH DUDHE] – Open to contributions and ideas!
MYGITHUB-parthdude07
DATASET-Kaggle(indian recipes).
