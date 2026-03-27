# 🎬 Movie Recommendation System

## 📌 Overview
This project is a content-based movie recommendation system that suggests similar movies based on user input.

## 🚀 Features
- Recommends top 5 similar movies
- Uses cosine similarity
- Clean and modular code

## 🛠 Tech Stack
- Python
- Pandas
- Scikit-learn
- NumPy

## 📂 Project Structure
```
Movie_Recommendation_System/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── notebooks/
│   └── movie_recommender.ipynb
│
├── src/
│   └── recommender.py
│
├── requirements.txt
├── README.md
└── .gitignore
```
## Dataset link: 
```
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
```

## ▶️ How to Run

```bash
pip install -r requirements.txt

Run notebook: jupyter notebook
```

## 📊 Example
Input: 
```
Avatar
```
Output:
```
Guardians of the Galaxy
John Carter
...
```
