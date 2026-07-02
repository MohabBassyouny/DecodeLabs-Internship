import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

file_path = 'raw_skills.csv'

if not os.path.exists(file_path):
    data = {
        'Role': ['Data Scientist', 'DevOps Engineer', 'Backend Developer', 'Cloud Architect'],
        'Skills': ['Python SQL Machine Learning', 'AWS Docker Kubernetes CI/CD', 'Java Python SQL APIs', 'AWS Cloud Automation Linux']
    }
    pd.DataFrame(data).to_csv(file_path, index=False)

df = pd.read_csv(file_path)

print("--- Tech Stack Recommender ---")
user_skills = input("Enter your skills separated by spaces: ")

user_df = pd.DataFrame({'Role': ['User Profile'], 'Skills': [user_skills]})
df_combined = pd.concat([df, user_df], ignore_index=True)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df_combined['Skills'])

cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

df['Similarity_Score'] = cosine_sim[0]

top_n = 3
recommended_roles = df.sort_values(by='Similarity_Score', ascending=False).head(top_n)

print("\n--- Top Recommended Roles ---")
for index, row in recommended_roles.iterrows():
    match_percentage = row['Similarity_Score'] * 100
    print(f"Role: {row['Role']} | Match Score: {match_percentage:.1f}%")