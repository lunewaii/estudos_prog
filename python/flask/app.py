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

    return jsonify("message": "Nova tarefa criada com sucesso")

if __name__ == "__main__":
    app.run(debug=True)