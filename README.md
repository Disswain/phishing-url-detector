# 🔐 Phishing URL Detection System

A machine learning-based web application that detects whether a given URL is **phishing or legitimate** using a Random Forest model.

---

## 🚀 Features

* 🔍 Detects phishing URLs in real-time
* 🌐 Simple web interface (Flask)
* 🧠 Machine Learning model (Random Forest)
* ⚙️ Automatic feature extraction from URLs
* 📊 Displays model accuracy

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **scikit-learn**
* **Pandas**
* **NumPy**
* **HTML + Bootstrap**

---

## 📂 Project Structure

```
phishing-url-detector/
│
├── app.py
├── train_model.py
├── feature_extraction.py
├── model.pkl
├── dataset_url.csv
├── requirements.txt
│
└── templates/
    ├── index.html
    └── result.html
```

---

## ⚙️ How It Works

1. User enters a URL in the web app
2. Backend extracts security-related features
3. Features are passed to the trained ML model
4. Model predicts:

   * ⚠️ Phishing Website
   * ✅ Legitimate Website

---

## ▶️ Installation & Run

### 1. Clone the repository

```
git clone https://github.com/Disswain/phishing-url-detector.git
cd phishing-url-detector
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Train the model

```
python train_model.py
```

### 4. Run the Flask app

```
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Model Details

* Algorithm: **Random Forest Classifier**
* Input: Extracted URL features
* Output: Binary classification (Phishing / Legitimate)

---

## 📈 Example Features Used

* URL length
* Presence of IP address
* HTTPS usage
* Suspicious keywords
* Subdomain count
* URL redirection patterns

---

## ⚠️ Limitations

* Uses a small dataset (prototype-level)
* Accuracy depends on feature quality
* Does not include advanced features like WHOIS or DNS

---

## 🔮 Future Improvements

* Larger dataset (10,000+ URLs)
* WHOIS & domain age integration
* Chrome extension
* Deployment on cloud (AWS / Render)
* Deep learning models

---

## 🧠 Key Learning

This project demonstrates how **machine learning can be integrated into a web application** for real-time cybersecurity use cases.

---

## 👨‍💻 Author

Disita Swain

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub! happy coding!!!
