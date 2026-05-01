from flask import Blueprint, jsonify
from app.models.article_model import Article
from app import db
import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.filter_by(is_published=True).order_by(Article.created_at.desc()).all()
    from flask import current_app
    return current_app.response_class(
        response=json.dumps([a.to_dict() for a in articles], ensure_ascii=False),
        mimetype='application/json'
    )

@api_bp.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    article = Article.query.get_or_404(id)
    from flask import current_app
    return current_app.response_class(
        response=json.dumps(article.to_dict(), ensure_ascii=False),
        mimetype='application/json'
    )
