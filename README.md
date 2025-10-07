# 📚 Book Recommendation System

[![Python](https://img.shields.io/badge/Python-3.7+-blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-2.0+-green)](https://flask.palletsprojects.com/)  
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-blue)](https://pandas.pydata.org/)  
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24+-orange)](https://scikit-learn.org/stable/)  
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  

---

## ✨ Overview

This **Book Recommendation System** suggests books similar to a user-provided book based on **content similarity**.  
It uses **TF-IDF vectorization** and **cosine similarity** on combined book features such as Title, Author, Main Genre, Sub Genre, and Type.  

**Features:**
- Recommend books based on a single input book  
- Web-based interface using **Flask**  
- Returns book details including Title, Author, Rating, and URLs  

---

## 🛠️ Requirements

- Python ≥ 3.7  
- Flask ≥ 2.0  
- Pandas ≥ 1.3  
- Scikit-learn ≥ 0.24  

Install dependencies:

```bash
pip install -r requirements.txt
🚀 Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/book-recommendation.git
cd book-recommendation
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Place your dataset (initial_dataset1.csv) in the project folder.

Run the Flask app:

bash
Copy code
python app.py
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000/
📝 Usage
Python Function Usage
You can also use the recommendation function directly in Python:

python
Copy code
from app import recommend_books

book_name = "The Great Gatsby"
recommendations = recommend_books(book_name, top_n=3)

for book in recommendations:
    print(f"Title: {book['Title']}, Author: {book['Author']}, Rating: {book['Rating']}, URLs: {book['URLs']}")
Web Interface
Open the home page (index1.html)

Enter a book name in the input field

Click Submit

Get top 3 recommended books

🔍 How it Works
Data Preparation: Combine relevant columns into a single feature:

python
Copy code
df['combined_features'] = df['Title'] + ' ' + df['Author'] + ' ' + df['Main Genre'] + ' ' + df['Sub Genre'] + ' ' + df['Type']
TF-IDF Vectorization: Convert text features into numeric vectors.

python
Copy code
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_features'])
Cosine Similarity: Compute similarity between books:

python
Copy code
from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
Recommendations: Find top similar books based on the cosine similarity score.

🤝 Contributing
Contributions are welcome!

Fork the repository

Create a branch (git checkout -b feature/new-feature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/new-feature)

Open a Pull Request

Please follow coding standards and include tests.

📄 License
MIT License — see LICENSE

🙏 Acknowledgements
Pandas

Scikit-Learn

Flask

⭐ If this project helped you, give it a star!
