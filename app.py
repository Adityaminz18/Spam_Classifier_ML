import streamlit as st
import pickle
import string
from PIL import Image
from streamlit_lottie import st_lottie
import json

# Load model and vectorizer
clf = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

# Function to clean text
def transform_text(text):
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer

    ps = PorterStemmer()
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum() and i not in stopwords.words('english') and i not in string.punctuation:
            y.append(ps.stem(i))

    return " ".join(y)

# Function to load Lottie animation from local file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load Lottie animation from your local file
lottie_spam = load_lottiefile("Animation_spam.json")

# Page Config
st.set_page_config(page_title="SMS Spam Detector", page_icon="📩", layout="centered")

# Header Section
st.title("📩 SMS Spam Classifier")
st.write("🔎 Enter a message below to check whether it's **Spam** or **Not Spam**.")

# Lottie Animation
if lottie_spam:
    st_lottie(lottie_spam, height=200, key="spam")
else:
    st.warning("Failed to load animation.")

# Input Text Area
input_sms = st.text_area("💬 Your Message Here:")

# Predict Button
if st.button('🚀 Predict'):
    
    if input_sms.strip() == "":
        st.warning("Please enter a valid message.")
    else:
        # Preprocess
        transformed_sms = transform_text(input_sms)

        # Vectorize
        vector_input = tfidf.transform([transformed_sms]).toarray()

        # Predict
        result = clf.predict(vector_input)[0]

        # Display Result
        if result == 1:
            st.error("🚫 This message is **SPAM**.")
        else:
            st.success("✅ This message is **NOT Spam**. Safe to open.")

# Footer
st.markdown("---")
st.caption("🔒 This tool is built for educational purposes using machine learning.")
