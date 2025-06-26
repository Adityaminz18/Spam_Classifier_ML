# Spam_Classifier_ML
A simple Streamlit app for spam message detection using Machine Learning.


Great! Here's a **complete, ready-to-use `README.md`** for your **Streamlit + Machine Learning Spam Detector** project:

---
# 📢 Spam Detector with Streamlit and Machine Learning

A simple and interactive **Spam Message Detection** web app built using **Streamlit** and **Machine Learning**. The app classifies text messages as either **Spam** or **Not Spam** using a trained Naive Bayes model and TF-IDF vectorization.

---

## 🚀 Features

- 🔎 Detects whether a message is spam or not in real-time
- 🧠 Trained using Naive Bayes classifier
- ✨ Clean and interactive Streamlit web interface
- 📊 Utilizes TF-IDF vectorization for text preprocessing

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit**
- **Scikit-learn**
- **Pandas**
- **TF-IDF Vectorizer**
- **Naive Bayes Classifier**

---

## 📂 Project Structure

```
Spam_Classifier_ML/
├── app.py              # Main Streamlit application
├── model.pkl           # Trained ML model
├── vectorizer.pkl      # Saved TF-IDF vectorizer
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build instructions
├── README.md           # Project overview
└── spam_classifier_ml/ 
```

---

## 🖥️ How to Run the App

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/spam-detector-streamlit.git
   cd spam-detector-streamlit
```

2. **Install Dependencies**

   It is recommended to create a virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

4. **Open in Browser**

   The app will automatically open at `http://localhost:8501`. If not, open the link manually.

---

## 🧠 Model Details

* **Vectorizer**: TF-IDF (Term Frequency - Inverse Document Frequency)
* **Model**: Multinomial Naive Bayes
* The model and vectorizer are pre-trained and loaded using `pickle`.

---

## 💡 Example

Simply enter a message in the text box like:

```
Congratulations! You have won a free iPhone. Click here to claim now.
```

And the app will classify it as:

> **Spam**

---

## 📦 Requirements

Make sure to have these libraries installed:

```
streamlit
scikit-learn
pandas
numpy
pickle
```

---

## ✨ Screenshots (Optional)

*Add screenshots of your app here if available.*

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests.

---

## 📄 License

This project is for educational purposes. Feel free to modify and use as needed.

---

## ❤️ Acknowledgements

Thanks to the open-source community for the tools and libraries that made this project possible.

---

## 🐳 Run with Docker

You can containerize and run this app using Docker:

1. **Build the Docker image**

   ```bash
   docker build -t spam-classifier-app .
   ```

2. **Run the Docker container**

   ```bash
   docker run -p 8501:8501 spam-classifier-app
   ```

3. **Access the app**

   Open your browser and go to [http://localhost:8501](http://localhost:8501)

---

```
