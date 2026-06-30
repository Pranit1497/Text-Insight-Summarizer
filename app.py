from flask import Flask, render_template, request
import re

app = Flask(__name__)

KEYWORDS = [
    "python", "web development", "ai", "automation", "data",
    "design", "api", "dashboard", "workflow", "user experience",
    "research", "analysis", "application", "system"
]

def summarize_text(text):
    if not text or not text.strip():
        return []

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return sentences[:3]

def extract_keywords(text):
    lower_text = text.lower()
    return [keyword.title() for keyword in KEYWORDS if keyword in lower_text]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        text = request.form.get("content", "")

        words = text.split()
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        sentences = [sentence for sentence in sentences if sentence.strip()]

        result = {
            "summary": summarize_text(text),
            "word_count": len(words),
            "sentence_count": len(sentences),
            "keywords": extract_keywords(text),
            "reading_time": max(1, round(len(words) / 200)) if words else 0
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)