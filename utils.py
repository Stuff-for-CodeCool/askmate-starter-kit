import os
import csv
import datetime

QF = os.path.join(os.path.dirname(__file__), "data", "question.csv")
AF = os.path.join(os.path.dirname(__file__), "data", "answer.csv")
QH = [
    "id",
    "submission_time",
    "view_number",
    "vote_number",
    "title",
    "message",
    "image",
]
AH = ["id", "submission_time", "vote_number", "question_id", "message", "image"]


def read_file(filename, headers):
    with open(filename, "r") as file:
        reader = csv.DictReader(file, fieldnames=headers)
        return list(reader)[1:]


def write_file(filename, headers, content):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in content:
            writer.writerow(row)


def read_questions():
    return read_file(filename=QF, headers=QH)


def read_answers():
    return read_file(filename=AF, headers=AH)


def write_questions(content):
    write_file(filename=QF, headers=QH, content=content)


def write_answers(content):
    write_file(filename=AF, headers=AH, content=content)


def add_answer(id, message):
    answers = read_answers()
    answers.append(
        {
            "id": max([int(answer["id"]) for answer in answers]) + 1,
            "submission_time": datetime.datetime.now(),
            "vote_number": 0,
            "question_id": id,
            "message": message,
            "image": "",
        }
    )
    write_answers(answers)
