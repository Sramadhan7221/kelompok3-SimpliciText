from flask import Flask, request, render_template,jsonify
from transformers import pipeline

# Inisialisasi Flask
app = Flask(__name__)

# Inisialisasi pipeline Hugging Face untuk summarization
model_pipeline = pipeline("summarization", model="luisotorres/bart-finetuned-samsum")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    user_input = data.get("user_input", "")

    if not user_input.strip():
        return jsonify({"error": "Input text is required"}), 400

    result = model_pipeline(user_input, max_length=100, min_length=25, do_sample=False)
    summary = result[0]["summary_text"]
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)