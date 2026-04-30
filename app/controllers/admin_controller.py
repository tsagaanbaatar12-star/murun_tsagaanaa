from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models.admin_model import Admin
from app.models.article_model import Article
from app import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('admin.dashboard'))
        flash('Нэвтрэх нэр эсвэл нууц үг буруу байна!', 'danger')
    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

@admin_bp.route('/')
@login_required
def dashboard():
    total = Article.query.count()
    published = Article.query.filter_by(is_published=True).count()
    articles = Article.query.order_by(Article.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html', total=total, published=published, articles=articles)

@admin_bp.route('/articles')
@login_required
def articles():
    all_articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('admin/articles.html', articles=all_articles)

@admin_bp.route('/articles/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'POST':
        article = Article(
            title=request.form['title'],
            content=request.form['content'],
            category=request.form.get('category', 'Ерөнхий'),
            author=request.form.get('author', current_user.username),
            is_published=bool(request.form.get('is_published'))
        )
        db.session.add(article)
        db.session.commit()
        flash('Нийтлэл амжилттай нэмэгдлээ!', 'success')
        return redirect(url_for('admin.articles'))
    return render_template('admin/article_form.html', article=None, action='Нэмэх')

@admin_bp.route('/articles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']
        article.category = request.form.get('category', 'Ерөнхий')
        article.author = request.form.get('author', article.author)
        article.is_published = bool(request.form.get('is_published'))
        db.session.commit()
        flash('Нийтлэл амжилттай шинэчлэгдлээ!', 'success')
        return redirect(url_for('admin.articles'))
    return render_template('admin/article_form.html', article=article, action='Засах')

@admin_bp.route('/articles/delete/<int:id>', methods=['POST'])
@login_required
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('Нийтлэл устгагдлаа!', 'success')
    return redirect(url_for('admin.articles'))
