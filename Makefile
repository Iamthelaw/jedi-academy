# These targets are not files
.PHONY: test lint todo

clean:
	@echo '💩 CleanUp'
	@find . -type f -name "*.pyc" -delete
	@rm -f .coverage
	@rm -rf .cache __pycache__

todo:
	# Look for areas of the code that need updating when some event has taken place
	grep -rnH TODO

## Python
test:
	py.test
lint:
	flake8 .

## Django
serve:
	python manage.py runserver
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations $(app)
su:
	python manage.py createsuperuser
check:
	python manage.py check
shell:
	python manage.py shell

## Dependencies
install:
	@echo '✅ Installing dependencies'
	@pip install -r requirements.txt

upgrade:
	@echo '✨ Upgrading dependencies'
	@pip install --upgrade -r requirements.txt

freeze:
	@echo '❄️  Freezing'
	@pip freeze | tr A-Z a-z | sort > requirements.txt

## Deployment
deploy_production:
	git push --tag origin master
	git push heroku master

migrate_production:
	heroku run python manage.py migrate --remote heroku

collectstatic_production:
	./manage.py collectstatic --noinput

# shortcuts for deploy to the production
dp: deploy_production
dmp: deploy_production migrate_production
cp: collectstatic_production
