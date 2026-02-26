import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "title": [
        "RRR",
        "Baahubali The Beginning",
        "Baahubali The Conclusion",
        "Pushpa The Rise",
        "Ala Vaikunthapurramuloo",
        "Geetha Govindam",
        "Fidaa",
        "Ye Maaya Chesave",
        "Majili",
        "Jathi Ratnalu",
        "F2 Fun and Frustration",
        "Evaru",
        "Hit",
        "Goodachari",
        "Kshanam"
    ],
    "genre": [
        "action drama",
        "action epic",
        "action epic",
        "action thriller",
        "action family",
        "romance drama",
        "romance family",
        "romance drama",
        "romance emotional",
        "comedy drama",
        "comedy family",
        "thriller mystery",
        "thriller crime",
        "thriller spy",
        "thriller mystery"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["genre"])

def recommend_by_genre(user_genre):
    user_vector = vectorizer.transform([user_genre])
    similarity = cosine_similarity(user_vector, tfidf_matrix)
    scores = list(enumerate(similarity[0]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Telugu Movies:")
    for i in scores[:5]:
        print("-", df.iloc[i[0]]["title"])

genre_input = input("Enter a genre (action/romance/comedy/thriller): ")
recommend_by_genre(genre_input)