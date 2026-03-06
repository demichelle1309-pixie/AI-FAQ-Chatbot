import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')


import json
import re
import numpy as np
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
with open("cleaned_faq.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# NLP tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# ---------------- TEXT CLEANING ----------------
def preprocess(text):

    text = text.lower()

    text = re.sub(r"[^a-z0-9\s]", "", text)

    tokens = nltk.word_tokenize(text)

    tokens = [w for w in tokens if w not in stop_words]

    tokens = [lemmatizer.lemmatize(w) for w in tokens]

    return " ".join(tokens)

# Preprocess all questions
clean_questions = [preprocess(q) for q in questions]

# TF-IDF
vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(clean_questions)

# ---------------- CHATBOT FUNCTION ----------------
def get_answer(user_question):

    clean_query = preprocess(user_question)

    user_vec = vectorizer.transform([clean_query])

    similarity = cosine_similarity(user_vec, faq_vectors)

    best_index = np.argmax(similarity)

    confidence = similarity[0][best_index]

    if confidence < 0.50:
        return "Sorry, I couldn't find a relevant answer.", confidence

    return answers[best_index], confidence