from flask import Flask, render_template, request
import re

app = Flask(__name__)

KEYWORDS = [
    "python", "web development", "ai", "automation", "data",
    "design", "api", "dashboard", "workflow", "user experience",
    "research", "analysis", "application", "system"
]


def summarize_text(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    return sentences[:3]


def extract_keywords(text):
    lower_text = text.lower()
    found = []

    for keyword in KEYWORDS:
        if keyword in lower_text:
            found.append(keyword.title())

    return found


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        text = request.form.get("content", "")

        words = text.split()
        sentences = re.split(r'(?<=[.!?]) +', text.strip())

        result = {
            "summary": summarize_text(text),
            "word_count": len(words),
            "sentence_count": len([s for s in sentences if s.strip()]),
            "keywords": extract_keywords(text),
            "reading_time": max(1, round(len(words) / 200))
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, port=5001)