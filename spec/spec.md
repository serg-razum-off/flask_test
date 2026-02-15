# Fast Api financial tracker project

## Stack
- Fast API
- Pydantic
- Uvicorn
- SQLAlchemy

## Project structure

```
.
├── fin_app
│   ├── database
│   │   ├── database.py
│   │   ├── schemas
│   │   │   ├── transaction.py
│   │   │   └── user.py
│   │   └── tables_unfolder.py
│   ├── endpoints
│   │   ├── transactions.py
│   │   └── users.py
│   ├── extra
│   │   ├── create_app.py
│   │   └── __pycache__
│   │       └── create_app.cpython-314.pyc
│   ├── __init__.py
│   ├── models
│   │   ├── transaction.py
│   │   └── user.py
│   ├── __pycache__
│   │   └── __init__.cpython-314.pyc
│   ├── routers
│   │   └── base.py
│   └── settings
│       ├── config.py
│       └── __pycache__
│           └── config.cpython-314.pyc
├── pyproject.toml
├── README.md
├── spec
│   └── spec.md
└── uv.lock
```
