from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features

app = Flask(__name__)

data = pickle.load(open("model.pkl", "rb"))
model = data["model"]
accuracy = data["accuracy"]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]

        features = extract_features(url)
        pred = model.predict([features])[0]

        result = "⚠️ Phishing Website" if pred == 1 else "✅ Legitimate Website"

        return render_template("result.html", result=result, accuracy=accuracy)

    return render_template("index.html", accuracy=accuracy)

if __name__ == "__main__":
    app.run(debug=True)