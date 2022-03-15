from flask import Flask, redirect, render_template, request, url_for
import utils

app = Flask(__name__)


@app.get("/")
def index():
    questions = utils.read_questions()[:5]
    return render_template("index.html", questions=questions)


@app.get("/questions")
def index_all():
    questions = utils.read_questions()
    return render_template("index.html", questions=questions)


@app.get("/question/<id>")
def get_question(id):
    question = [
        question
        for question in utils.read_questions()
        if int(question["id"]) == int(id)
    ]

    answers = [
        answer
        for answer in utils.read_answers()
        if int(answer["question_id"]) == int(id)
    ]

    if not question:
        return render_template("404.html")

    return render_template(
        "question.html",
        id=question[0].get("id"),
        title=question[0].get("title"),
        message=question[0].get("message"),
        answers=answers,
    )


@app.get("/question/<id>/answer")
def get_answer(id):
    return render_template("add_answer.html", id=id)


@app.post("/question/<id>/answer")
def post_answer(id):
    message = request.form.get("message")
    utils.add_answer(id, message)
    return redirect(url_for("get_question", id=id))


if __name__ == "__main__":
    app.run(debug=True)
