import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def healthy_check():
	return jsonify({
        "status": "healthy",
        "uptime": "good",
        "project": os.environ.get("PROJECT_NAME", "Unknown")
        })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
