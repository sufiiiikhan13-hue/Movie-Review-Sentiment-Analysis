# 🎬 IMDb Movie Review Sentiment Analysis

### Comparative Study of Four Supervised Machine Learning Classifiers

A Machine Learning project that predicts whether an IMDb movie review expresses a **Positive** or **Negative** sentiment using four different machine learning algorithms.

The project uses Python, TF-IDF vectorization, Scikit-learn, and Streamlit to provide an interactive web application for sentiment prediction.

---

## 📌 Project Overview

The IMDb Movie Review Sentiment Analysis system automatically analyzes written movie reviews and classifies them into two categories:

- **Positive:** The review expresses a favorable opinion.
- **Negative:** The review expresses an unfavorable opinion.

Users can select different machine learning models and compare their predictions through a simple web interface.

## 🎯 Project Objectives

- Analyze movie reviews using Natural Language Processing (NLP).
- Convert text into numerical features using TF-IDF.
- Train and compare four supervised machine learning classifiers.
- Predict positive and negative movie reviews.
- Develop an interactive web application using Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning algorithms |
| TF-IDF | Text feature extraction |
| Joblib | Saving and loading trained models |
| Streamlit | Web application interface |

## 🤖 Machine Learning Models

This project uses four supervised machine learning algorithms:

1. **Logistic Regression** – Classifies reviews using learned feature weights.
2. **Multinomial Naive Bayes** – Uses probability to classify text.
3. **Support Vector Machine (SVM)** – Separates positive and negative reviews using a decision boundary.
4. **Random Forest** – Combines multiple decision trees to make predictions.

## 📂 Project Structure

```text
IMDb-Sentiment-Analysis/
│
├── app.py
├── tfidf_vectorizer.pkl
├── log_reg.pkl
├── nb_model.pkl
├── svm_model.pkl
├── rf_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## 📊 Dataset Information

The project report describes a balanced IMDb dataset containing:

- Total Reviews: 50,000
- Positive Reviews: 25,000
- Negative Reviews: 25,000
- Training Data: 80% (40,000 reviews)
- Testing Data: 20% (10,000 reviews)
- TF-IDF Features: Maximum 5,000

**Dataset Sources:**

- [Kaggle IMDb Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- [Stanford IMDb Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)
- [Hugging Face IMDb Dataset](https://huggingface.co/datasets/stanfordnlp/imdb)

Note: The original dataset and training script were not supplied for independent verification. The dataset configuration above reflects the project report.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

### 2. Open the Project Folder

```bash
cd IMDb-Sentiment-Analysis
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install streamlit scikit-learn joblib numpy scipy pandas
```

### 5. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

## 🚀 How to Use the Application

1. Run the Streamlit application.
2. Select a machine learning model from the sidebar.
3. Enter a movie review in the text box.
4. Click the prediction button.
5. The system analyzes the review.
6. View the predicted sentiment: **POSITIVE** or **NEGATIVE**.

## 📈 Model Evaluation

The original project report provides the following accuracy results:

| Model | Reported Accuracy |
|---|---:|
| Logistic Regression | 88.89% |
| Multinomial Naive Bayes | 85.08% |
| Support Vector Machine | Not Provided |
| Random Forest | Not Provided |

**Note:** The SVM and Random Forest accuracy scores have not been verified. A complete comparison requires testing all four models on the same test dataset.

## 🔄 Project Workflow

```text
IMDb Movie Reviews
        |
        v
 Text Preprocessing
        |
        v
   TF-IDF Vectorizer
        |
        v
 Machine Learning Models
        |
        v
  Select ML Algorithm
        |
        v
  Sentiment Prediction
        |
        v
 POSITIVE / NEGATIVE
```

## ✨ Main Features

- Four machine learning models.
- Positive and negative sentiment classification.
- TF-IDF text feature extraction.
- Interactive Streamlit interface.
- Model selection through a sidebar.
- Real-time review prediction using saved models.
- Easy-to-use interface.

## ⚠️ Limitations

- Supports English movie reviews.
- Only two sentiment classes: Positive and Negative.
- May have difficulty understanding sarcasm and mixed opinions.
- Complete evaluation results for all four models are not available.

## 👨‍💻 Project Team

**University:** Dawood University of Engineering & Technology, Karachi

**Department:** BS Artificial Intelligence

**Subject:** Machine Learning (AI-3202)

**Project:** Complex Computing Activity (CCA)

| Student Name | Roll Number |
|---|---|
| Sufyan Khan | 24F-AI-205 |
| Iqbal Ahmed | 24F-AI-208 |
| Asif Raza | 24F-AI-210 |
| Adeel | 24F-AI-209 |

## 🎓 Conclusion

The IMDb Movie Review Sentiment Analysis project demonstrates how machine learning and Natural Language Processing can be used to analyze movie reviews automatically.

By comparing Logistic Regression, Multinomial Naive Bayes, Support Vector Machine, and Random Forest, the project demonstrates different approaches to supervised text classification.

The Streamlit interface makes it easy for users to test movie reviews and view sentiment predictions.

---

**Developed as a Machine Learning CCA Project**

**BS Artificial Intelligence | Dawood University of Engineering & Technology, Karachi**

