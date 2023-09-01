makemigrations:
	docker-compose exec web_app sh -c "cd src && alembic -c migrations/alembic.ini revision --autogenerate"
migrate:
	docker-compose exec web_app sh -c "cd src && alembic -c migrations/alembic.ini upgrade head"
mm: makemigrations migrate

clear_migrations: 
	rm -rf src/migrations/versions/*.py

up:
	docker-compose up -d
stop:
	docker-compose stop
down: clear_migrations
	docker-compose down
