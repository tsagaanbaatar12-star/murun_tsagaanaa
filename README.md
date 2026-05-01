cat > ~/SoftwareEngineering/Lab07_Project/README.md << 'EOF'
# Lab07 - Мэдээний сайт (Flask MVC)

## Технологи
- **Backend**: Flask (Python) - REST API
- **Frontend**: HTML + Bootstrap 5
- **Database**: MySQL (Docker)
- **Architecture**: MVC Pattern

## Төслийн бүтэц
Lab07_Project/
├── app/
│   ├── init.py              # Flask app тохиргоо
│   ├── models/
│   │   ├── init.py
│   │   ├── admin_model.py       # Админ Model
│   │   └── article_model.py     # Мэдээ Model
│   ├── controllers/
│   │   ├── init.py
│   │   ├── user_controller.py   # Хэрэглэгчийн routes
│   │   ├── admin_controller.py  # Админ CRUD routes
│   │   └── api_controller.py    # REST API routes
│   ├── templates/
│   │   ├── base.html            # Үндсэн загвар
│   │   ├── user/
│   │   │   ├── index.html       # Нүүр хуудас
│   │   │   └── detail.html      # Мэдээний дэлгэрэнгүй
│   │   └── admin/
│   │       ├── login.html       # Нэвтрэх хуудас
│   │       ├── base_admin.html  # Админ үндсэн загвар
│   │       ├── dashboard.html   # Dashboard
│   │       ├── articles.html    # Мэдээний жагсаалт
│   │       └── article_form.html # Нэмэх/Засах форм
│   └── static/
│       └── uploads/             # Зургууд хадгалагдах газар
├── docker/
│   └── init.sql                 # DB үүсгэх
├── docker-compose.yml           # Docker тохиргоо
├── Dockerfile                   # Flask container тохиргоо
├── requirements.txt             # Python сангууд
└── run.py                       # Эхлүүлэгч
## Ажиллуулах

```bash
docker-compose up --build
```

Хөтөч дээр:
- Нүүр хуудас: http://localhost:5000
- Админ: http://localhost:5000/admin/login
- API: http://localhost:5000/api/articles

## Админ нэвтрэх
- Хэрэглэгч: `admin`
- Нууц үг: `admin123`

## API Endpoints
| Method | URL | Тайлбар |
|--------|-----|---------|
| GET | /api/articles | Бүх мэдээ JSON хэлбэрээр |
| GET | /api/articles/:id | Нэг мэдээ JSON хэлбэрээр |

## Admin CRUD
| Үйлдэл | URL |
|--------|-----|
| Нэвтрэх | /admin/login |
| Dashboard | /admin/ |
| Мэдээнүүд | /admin/articles |
| Нэмэх | /admin/articles/create |
| Засах | /admin/articles/edit/:id |
| Устгах | /admin/articles/delete/:id |
EOF
echo "README бэлэн боллоо!"