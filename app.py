import streamlit as st
import joblib
import os

# 1. Page Configuration (Must be first)
st.set_page_config(page_title="IMDb Sentiment Analysis", page_icon="🎬", layout="centered")

st.title("🎬 IMDb Movie Review Sentiment Analysis")
st.write("Enter a movie review below to predict if it is **Positive** or **Negative**.")

# 2. Load Models & Vectorizer with Error Handling
@st.cache_resource
def load_assets():
    try:
        # Load the vectorizer
        tfidf = joblib.load("tfidf_vectorizer.pkl")
        
        # Load the 4 models
        loaded_models = {
            "Logistic Regression": joblib.load("log_reg.pkl"),
            "Naive Bayes": joblib.load("nb_model.pkl"),
            "Support Vector Machine": joblib.load("svm_model.pkl"),
            "Random Forest": joblib.load("rf_model.pkl")
        }
        return tfidf, loaded_models
    except FileNotFoundError as e:
        return None, str(e)

# Attempt to load assets
vectorizer, models = load_assets()

# 3. CRITICAL CHECK: Stop if files are missing
if models is None:
    st.error("🚨 **Critical Error: Model files not found!**")
    st.warning(f"Error Details: {models}") # 'models' holds the error message here
    st.info("👉 **Solution:** You must run this app from the same folder where your .pkl files are located.")
    st.code("cd \"c:/Users/Ameet Computers/Desktop/Movie Review Website/\"\nstreamlit run app.py", language="bash")
    st.stop()  # STOPS execution here so no NameError occurs

# 4. Sidebar - Model Selection
st.sidebar.header("Settings")
model_choice = st.sidebar.selectbox(
    "Choose a Classification Model:",
    list(models.keys())
)

# 5. Main Interface - Text Input
st.subheader(f"Predicting with: {model_choice}")
review_text = st.text_area(
    "Type your movie review here:",
    height=150,
    placeholder="Example: This movie was absolutely fantastic! The acting was great."
)

# 6. Prediction Logic
if st.button("Predict Sentiment"):
    if review_text.strip() == "":
        st.warning("⚠️ Please enter some text first.")
    else:
        try:
            # A. Transform user input to numbers
            vectorized_input = vectorizer.transform([review_text])

            # B. Get the chosen model
            selected_model = models[model_choice]

            # C. Predict (1=Positive, 0=Negative)
            prediction = selected_model.predict(vectorized_input)[0]

            # D. Display Result
            if prediction == 1:
                st.success("✅ **Sentiment: POSITIVE** 😀")
                st.balloons()
            else:
                st.error("❌ **Sentiment: NEGATIVE** 😞")
        
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# Footer
st.markdown("---")
st.caption("Developed for Sentiment Analysis Assignment")