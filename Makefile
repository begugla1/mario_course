up:
	docker-compose up
stop:
	docker-compose stop
down:
	docker-compose down
makemigrations:
	docker-compose exec web_app sh -c "cd trading_course && PYTHONPATH=api alembic -c migrations/alembic.ini revision --autogenerate"
migrate:
	docker-compose exec web_app sh -c "cd trading_course && PYTHONPATH=api alembic -c migrations/alembic.ini upgrade head"
mm: makemigrations migrate
	echo "It's done"
clearm:
	rm -rf trading_course/migrations/versions/*.py
