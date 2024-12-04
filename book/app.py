import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Load the dataset
df = pd.read_csv("initial_dataset1.csv")
df.fillna('', inplace=True)

# Combine relevant columns into a single feature for each book
df['combined_features'] = (
    df['Title'] + ' ' +
    df['Author'] + ' ' +
    df['Main Genre'] + ' ' +
    df['Sub Genre'] + ' ' +
    df['Type']
)

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend books based on a given book name
def recommend_books(book_name, top_n=3):
    indices = pd.Series(df.index, index=df['Title']).drop_duplicates()

    if book_name not in indices:
        return "Book not found in the dataset!"

    book_index = indices[book_name]

    similarity_scores = list(enumerate(cosine_sim[book_index].tolist()))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    top_books = similarity_scores[1:top_n + 1]

    recommendations = []
    for idx, score in top_books:
        recommendations.append({
            "Title": df.iloc[idx]['Title'],
            "Author": df.iloc[idx]['Author'],
            "Rating": df.iloc[idx]['Rating'],
            "URLs": df.iloc[idx]['URLs']
        })

    return recommendations

# Route for the home page
@app.route('/')
def index():
    return render_template('index1.html')

# Route to handle the book recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    book_name = request.form['book_name']
    recommendations = recommend_books(book_name)
    if isinstance(recommendations, str):  # If no book found, return an error message
        return jsonify({"error": recommendations})

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
