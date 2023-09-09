makemigrations:
	docker-compose exec api sh -c "alembic revision --autogenerate"
migrate:
	docker-compose exec api sh -c "alembic upgrade head"
mm: makemigrations migrate

clear_migrations: 
	rm -rf src/migrations/versions/*.py

up:
	docker-compose up -d --remove-orphans
stop:
	docker-compose stop
down: clear_migrations
	docker-compose down
