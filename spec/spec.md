# Fast Api financial tracker project

## Stack
- Fast API
- Pydantic
- Uvicorn
- SQLAlchemy

## Project structure

```
./
├── data/
│   └── fin_app.db
├── fin_app/
│   ├── db/
│   │   ├── db_manager.py
│   │   ├── db_scripts_DDL.py
│   │   └── __init__.py
│   ├── endpoints/
│   │   ├── transactions.py
│   │   └── users.py
│   ├── extra/
│   │   └── create_app.py
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── transaction.py
│   │   └── user.py
│   ├── routers/
│   │   ├── base.py
│   │   ├── transactions.py
│   │   └── users.py
│   └── settings/
│       └── config.py
├── fin_app.db
├── pyproject.toml
├── README.md
├── server.log
├── spec/
│   └── spec.md
└── uv.lock
```
