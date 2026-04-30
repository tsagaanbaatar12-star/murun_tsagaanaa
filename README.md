# Lab07 - Flask MVC Web System

## Технологи
- **Backend**: Flask (Python) - REST API
- **Frontend**: HTML + CSS (Bootstrap 5) + JavaScript
- **Database**: MySQL (Docker)
- **Architecture**: MVC Pattern

## Төслийн бүтэц
```
Lab07_project/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models/
│   │   ├── admin_model.py   # Admin Model
│   │   └── article_model.py # Article Model
│   ├── controllers/
│   │   ├── user_controller.py   # User routes
│   │   ├── admin_controller.py  # Admin CRUD routes
│   │   └── api_controller.py    # REST API routes
│   ├── templates/
│   │   ├── base.html
│   │   ├── user/
│   │   │   ├── index.html
│   │   │   └── detail.html
│   │   └── admin/
│   │       ├── base_admin.html
│   │       ├── login.html
│   │       ├── dashboard.html
│   │       ├── articles.html
│   │       └── article_form.html
│   └── static/
│       ├── css/main.css
│       └── js/main.js
├── docker/
│   └── init.sql             # DB seed data
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── run.py
```

## Ажиллуулах

### Docker ашиглан (санал болгох)
```bash
docker-compose up --build
```
Дараа нь: http://localhost:5000

### Локал орчинд (MySQL тусад нь ажиллаж байх ёстой)
```bash
pip install -r requirements.txt
python run.py
```

## Нэвтрэх мэдээлэл
- **Админ URL**: http://localhost:5000/admin/login
- **Хэрэглэгч нэр**: `admin`
- **Нууц үг**: `admin123`

## API Endpoints
| Method | URL | Тайлбар |
|--------|-----|---------|
| GET | /api/articles | Бүх нийтлэл |
| GET | /api/articles/:id | Нэг нийтлэл |
| GET | /api/categories | Категориуд |

## Admin CRUD
| Үйлдэл | URL |
|--------|-----|
| Нэвтрэх | /admin/login |
| Dashboard | /admin/ |
| Нийтлэлүүд | /admin/articles |
| Нэмэх | /admin/articles/create |
| Засах | /admin/articles/edit/:id |
| Устгах | /admin/articles/delete/:id |
