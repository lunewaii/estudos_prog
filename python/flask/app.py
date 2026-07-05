from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# como rotas funcionam no flask:
# @app.route("/")
# def mozinho():
#     return "oi momozinho, te amo muitinho!"

# @app.route("/about")
# def about():
#     return "página sobre"

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    tasks.append(new_task)
    print(tasks)
    task_id_control += 1
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for t in tasks:
        if t.id == task_id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Tarefa não encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for t in tasks:
        if t.id == task_id:
            t.title = data.get('title', t.title)
            t.description = data.get('description', t.description)
            t.completed = data.get('completed', t.completed)
            return jsonify({"message": "Tarefa atualizada com sucesso"})
    return jsonify({"message": "Tarefa não encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            return jsonify({"message": "Tarefa deletada com sucesso"})
    return jsonify({"message": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)