from flask import Flask, jsonify, request

app = Flask(__name__)

PROGRAMS = [
    {"name": "Strength Training", "duration_minutes": 45},
    {"name": "Cardio", "duration_minutes": 30},
    {"name": "Yoga", "duration_minutes": 60},
]


@app.route("/")
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/programs")
def programs():
    return jsonify({"programs": PROGRAMS})


@app.route("/calculate-calories", methods=["POST"])
def calculate_calories():
    data = request.get_json(silent=True) or {}

    try:
        weight = float(data["weight_kg"])
        duration = float(data["duration_minutes"])
        met = float(data["met"])
    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Provide numeric weight_kg, duration_minutes and met"
        }), 400

    if weight <= 0 or duration <= 0 or met <= 0:
        return jsonify({"error": "Values must be greater than zero"}), 400

    calories = met * 3.5 * weight / 200 * duration

    return jsonify({"calories_burned": round(calories, 2)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
