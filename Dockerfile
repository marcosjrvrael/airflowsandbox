FROM apache/airflow
LABEL mantainer="moj"

ARG AIRFLOW_USER_HOME=/opt/airflow
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}

COPY config/entrypoint.sh /entrypoint.sh
COPY config/airflow.cfg ${AIRFLOW_USER_HOME}/airflow.cfg
COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ARG GIT_TOKEN

USER root

RUN chmod u+x /entrypoint.sh

RUN chown airflow: /entrypoint.sh

USER airflow

ENV PYTHONPATH=/opt/airflow
ENV ENVIRONMENT=''
ENV GIT_TOKEN=${GIT_TOKEN}

EXPOSE 8080 5555 8793

USER airflow

WORKDIR ${AIRFLOW_USER_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"] # set default arg for entrypoint