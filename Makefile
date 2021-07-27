airflow-build:
	docker build -t sandbox_airflow .

airflow-run: airflow-build
	docker-compose -f local_airflow/docker-compose.yml up -d

airflow-stop:
	docker-compose -f local_airflow/docker-compose.yml down
