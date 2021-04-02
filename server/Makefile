IMAGE_NAME=
GCS_STATIC_BUCKET_URI=

.PHONY: run
run:
	@docker-compose up -d db;
	@docker-compose up web;

.PHONY: build
build:
	@docker-compose build

.PHONY: push
push:
	@docker push $(IMAGE_NAME):latest

.PHONY: deploy
deploy:
	@docker push $(IMAGE_NAME)
	@kubectl apply -f deployment/kubernetes/db -f deployment/kubernetes/web
	@kubectl scale deploy wuphf-web --replicas=0
	@kubectl scale deploy wuphf-web --replicas=1


.PHONY: set-bucket-cors
set-bucket-cors:
	@echo "Setting bucket CORS"; \
	gsutil cors set deployment/misc/gcs_bucket_cors.json $(GCS_STATIC_BUCKET_URI)


.PHONY: collectstatic
collectstatic:
	@docker-compose run --entrypoint=python web manage.py collectstatic --noinput


.PHONY: deploy-static
deploy-static:
	@echo "Deploying Static Files to Prod";
	@make collectstatic;
	@gsutil -m rsync -R ./src/static $(GCS_STATIC_BUCKET_URI)


.PHONY: migrations
migrations:
	@docker-compose run --entrypoint=python web manage.py makemigrations


.PHONY: migrate
migrate:
	@docker-compose run --entrypoint=python web manage.py migrate
