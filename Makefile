local-up:
	@docker-compose up -d --build

prod-build-up:
	@docker-compose -f docker-compose.prod.yml up -d --build
	@docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

prod-up:
	@docker-compose -f docker-compose.prod.yml up

prod-makemigrations:
	@docker-compose -f docker-compose.prod.yml run web python manage.py makemigrations --noinput

prod-migrate:
	@docker-compose -f docker-compose.prod.yml run web python manage.py migrate --noinput

prod-collectstatic:
	@docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
	
prod-createsuperuser:
	@docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

prod-flush:
	@docker-compose -f docker-compose.prod.yml exec web python manage.py flush

down:
	@docker-compose down --remove-orphans
