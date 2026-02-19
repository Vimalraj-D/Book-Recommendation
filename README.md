<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=📚%20Book%20Recommender&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Discover%20Your%20Next%20Favorite%20Book&descAlignY=55&descSize=18" width="100%"/>

<!-- Typing Animation -->


<br/>

<!-- Badges -->
[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br/>

<!-- Stats / Quick Info Pills -->
![Books](https://img.shields.io/badge/🧠_Algorithm-TF--IDF_+_Cosine_Similarity-blueviolet?style=flat-square)
![Interface](https://img.shields.io/badge/🌐_Interface-Web_Based-blue?style=flat-square)
![Recommendations](https://img.shields.io/badge/📚_Returns-Top_3_Matches-green?style=flat-square)

</div>

---

## 🌟 What Is This?

> *"A reader lives a thousand lives before he dies."* — George R.R. Martin

The **Book Recommendation System** is an intelligent engine that finds books *similar* to the one you love. Powered by **TF-IDF vectorization** and **cosine similarity**, it analyzes book features like Title, Author, Genre, Sub-Genre, and Type to surface the most relevant recommendations — instantly, through a sleek web interface.

---

## ✨ Features at a Glance

```
┌─────────────────────────────────────────────────────────────┐
│  📖  Input any book name                                    │
│  🧠  AI-powered content similarity engine kicks in          │
│  🎯  Returns top 3 most similar books                       │
│  📊  Includes Title · Author · Rating · Links               │
│  🌐  Beautiful Flask web interface                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔬 How It Works — Under the Hood

```mermaid
flowchart LR
    A([📥 User Input\nBook Name]) --> B[🔎 Feature\nExtraction]
    B --> C[📐 TF-IDF\nVectorization]
    C --> D[📊 Cosine\nSimilarity]
    D --> E([🎯 Top 3\nRecommendations])

    style A fill:#4f46e5,color:#fff,stroke:none
    style B fill:#7c3aed,color:#fff,stroke:none
    style C fill:#9333ea,color:#fff,stroke:none
    style D fill:#c026d3,color:#fff,stroke:none
    style E fill:#db2777,color:#fff,stroke:none
```

### Step-by-Step Breakdown

**① Feature Engineering** — Combine all meaningful book attributes into a single rich text field:

```python
df['combined_features'] = (
    df['Title'] + ' ' + df['Author'] + ' ' +
    df['Main Genre'] + ' ' + df['Sub Genre'] + ' ' + df['Type']
)
```

**② TF-IDF Vectorization** — Transform text into meaningful numeric vectors:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_features'])
```

**③ Cosine Similarity** — Measure how "close" each book is to every other:

```python
from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
```

**④ Rank & Return** — Sort by similarity score, return the top N books. Done! 🎉

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
| 🐍 Language | Python 3.7+ | Core engine |
| 🌐 Web Framework | Flask 2.0+ | REST API & UI |
| 🗂️ Data | Pandas 1.3+ | Dataset manipulation |
| 🤖 ML | Scikit-Learn 0.24+ | TF-IDF & Cosine Similarity |

</div>

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/book-recommendation.git
cd book-recommendation
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Your Dataset

Place your dataset file in the project root:
```
📁 book-recommendation/
├── 📄 app.py
├── 📄 requirements.txt
├── 📊 initial_dataset1.csv   ← your dataset goes here
└── 📁 templates/
    └── 🌐 index1.html
```

### 4️⃣ Launch the App

```bash
python app.py
```

### 5️⃣ Open Your Browser

```
http://127.0.0.1:5000/
```

> 🎉 You're live! Start discovering your next great read.

---

## 📝 Usage

### 🌐 Web Interface

```
1.  Open http://127.0.0.1:5000/
2.  🔤  Type a book name into the search field
3.  🖱️  Click "Submit"
4.  📚  Get your 3 personalized recommendations!
```

### 🐍 Python API

You can also use the recommendation engine directly in Python:

```python
from app import recommend_books

recommendations = recommend_books("The Great Gatsby", top_n=3)

for book in recommendations:
    print(f"📖 {book['Title']}")
    print(f"✍️  {book['Author']}")
    print(f"⭐ {book['Rating']}")
    print(f"🔗 {book['URLs']}\n")
```

**Sample Output:**
```
📖 Tender Is the Night
✍️  F. Scott Fitzgerald
⭐ 4.3
🔗 https://example.com/book/123

📖 The Sun Also Rises
✍️  Ernest Hemingway
⭐ 4.1
🔗 https://example.com/book/456
```

---

## 📁 Project Structure

```
📦 book-recommendation/
│
├── 🐍 app.py                  ← Flask app + recommendation logic
├── 📊 initial_dataset1.csv    ← Book dataset
├── 📄 requirements.txt        ← Python dependencies
├── 📄 README.md               ← You are here!
│
└── 📁 templates/
    └── 🌐 index1.html         ← Web UI template
```

---

## 🤝 Contributing

Contributions make the open-source community such an amazing place to learn and grow. Any contributions you make are **greatly appreciated**!

```bash
# Step 1: Fork the project
# Step 2: Create your feature branch
git checkout -b feature/AmazingFeature

# Step 3: Commit your changes
git commit -m '✨ Add some AmazingFeature'

# Step 4: Push to the branch
git push origin feature/AmazingFeature

# Step 5: Open a Pull Request 🚀
```

> Please follow coding standards and include tests where possible.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 🙏 Acknowledgements

A huge thanks to the amazing open-source tools that power this project:

- 🐼 [**Pandas**](https://pandas.pydata.org/) — Data wrangling made easy
- 🤖 [**Scikit-Learn**](https://scikit-learn.org/) — The ML workhorse
- 🌶️ [**Flask**](https://flask.palletsprojects.com/) — Lightweight & powerful web framework

---

<div align="center">

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>

**Made with ❤️ and a love for books**

*If this project helped you, please consider giving it a* ⭐ *— it means the world!*

[![Star on GitHub](https://img.shields.io/github/stars/Vimalraj-D/Book-Recommendation?style=social)](https://github.com/Vimalraj-D/Book-Recommendation)

</div>
