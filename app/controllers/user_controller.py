from flask import Blueprint, render_template
from app.models.article_model import Article

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    articles = Article.query.filter_by(is_published=True).order_by(Article.created_at.desc()).all()
    categories = db_get_categories()
    return render_template('user/index.html', articles=articles, categories=categories)

@user_bp.route('/article/<int:id>')
def article_detail(id):
    article = Article.query.get_or_404(id)
    return render_template('user/detail.html', article=article)

def db_get_categories():
    from app import db
    from app.models.article_model import Article
    cats = db.session.query(Article.category).distinct().all()
    return [c[0] for c in cats]
