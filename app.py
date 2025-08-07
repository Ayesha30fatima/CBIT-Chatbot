from flask import Flask, render_template, request, jsonify
import chatbot  # Your existing chatbot.py logic

app = Flask(__name__)

# Store user course and year in memory for now
user_context = {
    "course": "",
    "year": ""
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/set_context", methods=["POST"])
def set_context():
    data = request.get_json()
    user_context["course"] = data.get("course", "").upper()
    user_context["year"] = data.get("year", "").title()
    chatbot.user_course = user_context["course"]
    chatbot.user_year = user_context["year"]
    return jsonify({"status": "ok"})

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    response = chatbot.handle_query(user_msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

