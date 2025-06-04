from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

tasks = []  # Start empty

@app.route('/')
def home():
    return "Welcome to TaskNest!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "due_date": data.get("due_date"),
        "completed": data.get("completed", False)
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    for task in tasks:
        if task["id"] == id:
            task["title"] = data.get("title", task["title"])
            task["due_date"] = data.get("due_date", task["due_date"])
            task["completed"] = data.get("completed", task["completed"])
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
