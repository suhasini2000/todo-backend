from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build a React app", "done": False}
]

@app.route('/')
def home():
    return "ToDo API is running!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build a React app", "done": False}
]

@app.route('/')
def home():
    return "ToDo API is running!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.json
    # Validation: check if "task" exists and is not empty
    if not new_todo or "task" not in new_todo or not new_todo["task"].strip():
        return jsonify({"error": "Task is required"}), 400

    new_todo["id"] = len(todos) + 1
    new_todo["done"] = new_todo.get("done", False)
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.json
    
    new_todo["id"] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return '', 204


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def edit_todo(todo_id):
    data = request.json
    # Validation: check if "task" exists and is not empty
    if not data or "task" not in data or not data["task"].strip():
        return jsonify({"error": "Task is required"}), 400

    for todo in todos:
        if todo["id"] == todo_id:
            todo["task"] = data["task"]
            if "done" in data:
                todo["done"] = data["done"]
            return jsonify(todo), 200

    return jsonify({"error": "Todo not found"}), 404



if __name__ == '__main__':
    app.run(debug=True)
