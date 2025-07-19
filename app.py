from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load assets
df = pd.read_csv("final_dataset.csv")
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Filters
unique_cuisines = sorted(df['Cuisine'].dropna().unique().tolist())
time_filters = ['<15', '15-30', '30-60', '>60']
protein_levels = ['Low', 'Medium', 'High']

# Dummy function for protein level
def get_protein_level(ingredients):
    protein_items = ['paneer', 'egg', 'soy', 'dal', 'chicken', 'milk', 'curd']
    count = sum(1 for ing in ingredients if any(p in ing for p in protein_items))
    if count >= 3:
        return 'High'
    elif count == 2:
        return 'Medium'
    else:
        return 'Low'

@app.route('/')
def index():
    #most common top 50 ingredients
    top_ingredients =[
    "onion", "tomato",  "potato", "egg", "cabbage", "green peas", "besan","green chilli",  "coriander leaves", "rice",
    "coconut", "carrot", "spinach", "green beans", "paneer", "curd", "flour", "wheat flour",
    "mint leaves", "lemon", "moong dal", "urad dal", "methi leaves", "bread", "milk powder", "maida",
    "boiled potato", "semolina", "poha", "dal", "soy chunks", "tamarind pulp", "raw banana", "parboiled rice",
    "coconut milk", "gram flour", "beetroot", "puffed rice", "cucumber", "boiled rice", "mango", "oats", "jaggery",
    "brinjal", "rice flour", "cooked rice", "fenugreek leaves", "apple","ginger", "garlic"
]
    return render_template("index.html", cuisines=unique_cuisines, times=time_filters, proteins=protein_levels, ingredients=top_ingredients)


@app.route('/recommend', methods=['POST'])
def recommend():
    selected_ingredients = request.form.getlist("ingredients")
    selected_cuisine = request.form.get("cuisine")
    selected_time = request.form.get("time")
    selected_protein = request.form.get("protein")

    # Vectorize selected ingredients
    query = " ".join(selected_ingredients)
    vec = vectorizer.transform([query])
    distances, indices = model.kneighbors(vec)

    matches = df.iloc[indices[0]].copy()

    def get_score(row):
        score = 0

        # Cuisine match
        if selected_cuisine != "Any" and row['Cuisine'] == selected_cuisine:
            score += 1

        # Time match
        if selected_time != "Any":
            t = row['TotalTimeInMins']
            if (
                (selected_time == '<15' and t <= 15) or
                (selected_time == '15-30' and 15 < t <= 30) or
                (selected_time == '30-60' and 30 < t <= 60) or
                (selected_time == '>60' and t > 60)
            ):
                score += 1

        # Protein match
        if selected_protein != "Any":
            protein_level = get_protein_level(row['Cleaned-Ingredients'].split(', '))
            if protein_level == selected_protein:
                score += 1

        return score

    matches['score'] = matches.apply(get_score, axis=1)

    top_results = (
        matches.sort_values(by='score', ascending=False)
               .head(6).to_dict(orient='records')
    )

    return render_template("results.html", recipes=top_results)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
