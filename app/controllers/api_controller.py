from flask import Blueprint, jsonify, request
from app.models.article_model import Article
from app import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.filter_by(is_published=True).order_by(Article.created_at.desc()).all()
    return jsonify([a.to_dict() for a in articles])

@api_bp.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    article = Article.query.get_or_404(id)
    return jsonify(article.to_dict())

@api_bp.route('/categories', methods=['GET'])
def get_categories():
    cats = db.session.query(Article.category).distinct().all()
    return jsonify([c[0] for c in cats])
