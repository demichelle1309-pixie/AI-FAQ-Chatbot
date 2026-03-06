# 🤖 AI FAQ Chatbot

## 📌 Project Overview

This project implements an AI-powered FAQ chatbot that answers user questions by matching them with the most relevant question from a predefined FAQ dataset. The chatbot uses Natural Language Processing (NLP) techniques and cosine similarity to find the best answer.

The application includes a simple and interactive chat interface built with Streamlit where users can ask questions and receive responses in real time.

This project was developed as part of the **Artificial Intelligence Internship at SoftGrowTech**.

---

## 🚀 Features

* AI-powered FAQ matching
* Natural Language Processing for text cleaning
* Cosine similarity to find the closest question
* Interactive chat interface
* Confidence score for each response
* Real-time chatbot experience using Streamlit

---

## 🛠 Technologies Used

* Python
* Streamlit
* NLTK
* Scikit-learn
* NumPy
* TF-IDF Vectorization
* Cosine Similarity

---

## 📂 Project Structure

```
faq_chatbot
│
├── app.py                  # Streamlit chatbot interface
├── chatbot_engine.py       # NLP processing and similarity matching
├── preprocess_dataset.py   # Dataset preprocessing script
├── cleaned_faq.json        # Processed FAQ dataset
├── qa_Appliances.json      # Raw FAQ dataset
├── setup_nltk.py           # NLTK setup script
├── requirements.txt        # Project dependencies
```

---

## ⚙ Installation

1. Clone the repository

```
git clone <your-repository-link>
```

2. Navigate to the project folder

```
cd faq_chatbot
```

3. Install required dependencies

```
pip install -r requirements.txt
```

---

## ▶ Running the Chatbot

Start the Streamlit application:

```
streamlit run app.py
```

The chatbot interface will open in your browser.
Or simply click [https](http://localhost:8501/)
You can now ask appliance-related questions and the chatbot will return the most relevant answer from the FAQ dataset.

---

## 🧠 How It Works

1. The chatbot loads a dataset of FAQ questions and answers.
2. Text is cleaned using NLP techniques:

   * Lowercasing
   * Removing punctuation
   * Tokenization
   * Stopword removal
   * Lemmatization
3. Questions are converted into numerical vectors using **TF-IDF vectorization**.
4. When a user asks a question, the chatbot:

   * Preprocesses the query
   * Converts it into a TF-IDF vector
   * Computes cosine similarity with stored FAQ questions
5. The most similar question is selected and its answer is returned.

---

## 📷 Demo

<img width="1078" height="836" alt="image" src="https://github.com/user-attachments/assets/c571a927-02df-4623-a501-2b68398bfc7a" />


Example output:

User:
"How do I clean my microwave?"

Chatbot:
"To clean your microwave, wipe the interior with a damp cloth and mild detergent."

Confidence:
0.87

---

## 📚 Learning Outcomes

This project helped demonstrate:

* Natural Language Processing techniques
* Text preprocessing and tokenization
* TF-IDF feature extraction
* Cosine similarity for question matching
* Building AI chat interfaces using Streamlit

---

## 📌 Internship Information

This project was completed as part of the **Artificial Intelligence Internship at SoftGrowTech**, where interns build practical AI applications involving NLP, machine learning, and computer vision.

---

## 👨‍💻 Author

Developed by:
**Michelle De Melo**

