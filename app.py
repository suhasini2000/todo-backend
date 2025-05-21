from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = {
    1: {"id": 1, "task": "Learn Flask", "done": False},
    2: {"id": 2, "task": "Build a React app", "done": False}
}
next_id = 3

@app.route('/')
def home():
    return "ToDo API is running!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(list(todos.values()))

@app.route('/todos', methods=['POST'])
def create_todo():
    global next_id
    new_todo = request.json
    # Validation: check if "task" exists and is not empty
    if not new_todo or "task" not in new_todo or not new_todo["task"].strip():
        return jsonify({"error": "Task is required"}), 400

    todo = {
        "id": next_id,
        "task": new_todo["task"],
        "done": new_todo.get("done", False)
    }
    todos[next_id] = todo
    next_id += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id in todos:
        del todos[todo_id]
        return '', 204
    return jsonify({"error": "Todo not found"}), 404

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def edit_todo(todo_id):
    data = request.json
    # Validation: check if "task" exists and is not empty
    if not data or "task" not in data or not data["task"].strip():
        return jsonify({"error": "Task is required"}), 400

    if todo_id in todos:
        todos[todo_id]["task"] = data["task"]
        if "done" in data:
            todos[todo_id]["done"] = data["done"]
        return jsonify(todos[todo_id]), 200

    return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)