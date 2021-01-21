# Flask Starter with SQLAlchemy and Marshmallow.

- Simple Flask Starter with Factory Pattern.
- CRUD User
- Migration with flask-migrate

## Installation

Use the [pip](https://pypi.org/project/pip/) to install.

```bash
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
python app.py
```

Use [Docker](https://www.docker.com/)

```bash
docker build -t flask-starter .
docker run -dp 8080:8080 flask-starter
```

## Technologies

- Flask
- Flask-SqlAlchemy
- Flask-Migrate
- Flask-Marshmallow
