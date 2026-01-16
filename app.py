from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Placement Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            min-height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card {
            background: white;
            width: 500px;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 25px;
        }

        .question {
            margin-bottom: 20px;
        }

        .question p {
            font-weight: bold;
            margin-bottom: 8px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            cursor: pointer;
        }

        button {
            width: 100%;
            padding: 12px;
            background: #667eea;
            border: none;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
        }

        button:hover {
            background: #5a67d8;
        }

        .result {
            margin-top: 25px;
            padding: 15px;
            border-radius: 8px;
            background: #f3f4f6;
        }

        .beginner { color: #e53e3e; }
        .intermediate { color: #dd6b20; }
        .advanced { color: #38a169; }
    </style>
</head>

<body>
<div class="card">
    <h1>AI Placement Test</h1>

    <form method="post">

        <div class="question">
            <p>1. What is a neural network?</p>
            <label><input type="radio" name="q1" value="0"> A database</label>
            <label><input type="radio" name="q1" value="1"> A model inspired by the human brain</label>
        </div>

        <div class="question">
            <p>2. Which library is used for deep learning?</p>
            <label><input type="radio" name="q2" value="0"> NumPy</label>
            <label><input type="radio" name="q2" value="1"> PyTorch</label>
        </div>

        <div class="question">
            <p>3. What does overfitting mean?</p>
            <label><input type="radio" name="q3" value="1"> Model memorizes training data</label>
            <label><input type="radio" name="q3" value="0"> Model generalizes well</label>
        </div>

        <div class="question">
            <p>4. What does underfitting mean?</p>
            <label><input type="radio" name="q4" value="1"> Model is too simple to capture patterns</label>
            <label><input type="radio" name="q4" value="0"> Model generalizes poorly</label>
        </div>

        <button type="submit">Submit Test</button>
    </form>

    {% if result %}
    <div class="result">
        <p><b>Score:</b> {{ result.score }}%</p>
        <p class="{{ result.level | lower }}">
            <b>Level:</b> {{ result.level }}
        </p>
        <p><b>Recommended Start:</b> {{ result.recommendation }}</p>
    </div>
    {% endif %}

</div>
</body>
</html>
"""


def placement_test(score_percent):
    if score_percent < 40:
        return "Beginner"
    elif score_percent < 70:
        return "Intermediate"
    else:
        return "Advanced"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        score = 0
        for q in ["q1", "q2", "q3", "q4"]:
            score += int(request.form.get(q, 0))

        score_percent = int((score / 4) * 100)

        level = placement_test(score_percent)

        if level == "Beginner":
            recommendation = "Python & Programming Basics"
        elif level == "Intermediate":
            recommendation = "Neural Networks Basics"
        else:
            recommendation = "Deep Learning & Transformers"

        result = {
            "score": score_percent,
            "level": level,
            "recommendation": recommendation
        }

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
