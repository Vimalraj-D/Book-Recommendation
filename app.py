from flask import Flask, render_template, request
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from rapidfuzz import process

app = Flask(__name__)


print("Loading models...")

model = SentenceTransformer("models\\custom_embedding_model")
index = faiss.read_index("models\\book_index.faiss")

with open("models\\book_metadata.pkl", "rb") as f:
    df = pickle.load(f)

df.reset_index(drop=True, inplace=True)
titles = df["Title"].tolist()

print("System ready.")


def find_closest_title(user_input):
    match = process.extractOne(user_input, titles)
    return match[0] if match else None


def recommend_books(book_title, top_k):
    print(f"Received recommendation request for: '{book_title}' with top_k={top_k}")
    if top_k > 5:
        top_k = 5

    matched_title = find_closest_title(book_title)

    if not matched_title:
        return None, []

    book_row = df[df["Title"] == matched_title].iloc[0]
    book_idx = df[df["Title"] == matched_title].index[0]

    query_embedding = model.encode([book_row["document"]], convert_to_numpy=True)
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, top_k + 1)

    recommendations = []

    for idx in indices[0]:
        if idx == book_idx:
            continue

        book = df.iloc[idx]
        recommendations.append({
            "Title": book["Title"],
            "Author": book["Author"],
            "Genre": book["Main Genre"],
            "SubGenre": book["Sub Genre"],
            "Rating": book["Rating"],
            "Price": book["Price"],
            "URL": book["URLs"]
        })

        if len(recommendations) >= top_k:
            break

        selected_book = {
            "Title": book_row["Title"],
            "Author": book_row["Author"],
            "Genre": book_row["Main Genre"],
            "SubGenre": book_row["Sub Genre"],
            "Rating": book_row["Rating"],
            "Price": book_row["Price"],
            "URL": book_row["URLs"]
        }

    return selected_book, recommendations


@app.route("/", methods=["GET", "POST"])
def home():

    selected_book = None
    recommendations = []

    if request.method == "POST":
        title = request.form["title"]
        k = int(request.form["k"])

        selected_book, recommendations = recommend_books(title, k)

    return render_template(
        "index.html",
        selected_book=selected_book,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)