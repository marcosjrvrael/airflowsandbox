### Airflow para desenvolvimento e estudos com docker

Objetivo: Disponibilizar uma ferramenta de pipelines usando o Apache Airflow: https://airflow.apache.org/ executando em docker
baseando-se no projeto https://github.com/puckel/docker-airflow

As pastas dags/ e source/ serão mapeadas em volumes dentro do container.

#### Como usar:

Siga a documentação do airflow para entender a UI: https://airflow.apache.org/ui.html


##### Subindo ambiente

Para criar uma imagem local:
```
make build
```

Para iniciar o airflow
```
make start
```

Para terminar o airflow local:
```
make stop
```
