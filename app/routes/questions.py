from flask import Blueprint, request, jsonify


questions_bp = Blueprint('questions', __name__, url_prefix='/questions')
responses_bp = Blueprint('responses', __name__, url_prefix='/responses')

@questions_bp.route('/', methods=['GET'])
def get_questions():
    return f'Hello, flask!'


@questions_bp.route('/', methods=['POST'])
def add_question():
    return f'Add flask!'

