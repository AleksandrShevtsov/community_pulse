from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from app.models import db, Category
from app.schemas.questions import QuestionCreate, QuestionResponse, CategoryBase

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


@categories_bp.route('/', methods=['POST'])
def add_category():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': "Некорректные данные"}), 400

    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()

    return jsonify({'message': 'Category created', 'id': category.id}), 201


@categories_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    categories_data = [CategoryBase.model_validate() for c in categories]
    return jsonify(categories_data)


@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    category = Category.query.get_or_404(id)
    if 'name' in data:
        category.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Category updated'})


@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted'})
