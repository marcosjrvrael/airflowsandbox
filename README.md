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
### Como funciona o projeto.

A dag tutorial pode ser vista na documentação do airflow [tutorial](https://airflow.apache.org/docs/stable/tutorial.html)

A dag callingpython foi desenvolvida pra dar um passo inicial no desenvolvimento de fluxos com tarefas segregadas de suas dags,
nela temos um exemplo de python operator e o exemplo de um bashOperator chamando um outro .py e passando parametros, outro ponto dessa dag é que ela funciona de forma dinamica para gerar as tasks o que é uma otima forma de trabalhar com dags.

Obs.: Para um entendimento mais profundo recomendo a leitura da documentação [airflow_concepts](https://airflow.apache.org/docs/stable/concepts.html) e dos comentários nas classes.

#### Tasks dinamicas

As dags com task dinamicas são escritas dentro de 1 for para que uma lista alimente os parametros da mesma e processos diferentes sejam executados,
para uma explicação mais a fundo consultar [Dynamic_tasks](https://blog.pythian.com/creating-dynamic-tasks-using-apache-airflow/)

#### Variaveis do airflow

Variaveis do airflow podem ser usadas para passar parametros variados já que um dicionario json é aceito,
no exemplo contido nesse repositorio utilizamos para passar uma lista de itens que vão servir pra gerar as tasks dinamicas,
para criar uma variavel no airflow seguir o link [Variables](https://airflow.apache.org/docs/stable/concepts.html#variables)




#### Sugestões, criticas (construtivas), duvidas, e/ou contribuições são bem vindas!!!

Qualquer problema que encontrarem podem abrir uma issue.