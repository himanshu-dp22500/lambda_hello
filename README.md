virtualenv venv 

pip install SQLAlchemy

pip install alembic

cd serverlessHelloCleanArch

alembic init alembic

alembic revision -m "create message table"

Change : sqlalchemy.url = sqlite:///db.db ( Later we put in env vars)

alembic upgrade head
