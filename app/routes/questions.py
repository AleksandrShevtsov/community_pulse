from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from app.models import Question, db
from app.schemas.questions import QuestionCreate, QuestionResponse

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    questions_data = [QuestionResponse.model_validate(q) for q in questions]
    return jsonify(questions_data)


@questions_bp.route('/', methods=['POST'])
def add_question():
    data = request.get_json()

    try:
        question_data = QuestionCreate(**data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

    # if not data or 'text' not in data:
    #     return jsonify({'error': "Некорректные данные"}), 400

    question = question = Question(text=question_data.text, category_id=question_data.category_id)
    db.session.add(question)
    db.session.commit()

    return jsonify({'message': 'Question created', 'id': question.id}), 201


@questions_bp.route('/', methods=['PUT'])
def update_question():
    data = request.get_json()
    questions = Question.query.all()



@questions_bp.route('/', methods=['DELETE'])
def delete_question():
    return 'Delete flask!'
