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
    new_todo["id"] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
