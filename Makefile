build:
	docker build -t sandbox_puckel_airflow .

start: build
	docker-compose -f local_airflow/docker-compose-CeleryExecutor.yml up -d

stop:
	docker-compose -f local_airflow/docker-compose-CeleryExecutor.yml down
