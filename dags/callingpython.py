from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import logging
import os

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}


def word_to_count(**kwargs):
    """
        Python callable responsável por informar a palavra que tera as voguais contadas.
    """
    logging.info(f"Word to be counted {kwargs['word']}")


dag = DAG('callingpython', 
        default_args=default_args,
        schedule_interval=None)

"""
    Leitura de variavel do airflow words um exemplo de variavel segue abaixo para ser criado,
    Quando a variavel for criada automaticamente a dag ira gerar uma task para cada uma das palavras armazenadas na mesma,
    pois ela tem o comportamento de ser dinamica.
    Para que o programa inicie sem erros existe um default var explicito que só é substituido quando há valor no airflow.
    Exemplo de variavel para criar no airflow:
        Var name = words 
        Var values = {"word_list": ["abracadabra","proparoxitona","dtc","airflow","fiap"]}
"""
words = Variable.get(
    key="words",
    default_var={
        "word_list": ["fiap"]
    },
    deserialize_json=True
)

"""
    DummyOperator não serve para execução de tarefas mas pode ser usado como steps de marcação como inicio e fim da execução da dag.
    Mais informações na documentação oficial.
"""
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

for word in words["word_list"]:
    """
        A cada execução do loop uma palavra é lida e entrege as tasks do airflow.
        a primeira task informa qual a palavra que terá suas vogais contadas,
        a segunda aciona um arquivo .py que contém o metodo que faz a conta de voguais;
    """
    print_world = PythonOperator(
        task_id=f'print_world_{words["word_list"].index(word)}',
        provide_context=True,
        python_callable=word_to_count,
        op_kwargs={'word': word},
        dag=dag,
    )

    call_python = BashOperator(
        task_id=f'word_count_{words["word_list"].index(word)}',
        bash_command=f"python {os.environ['HOME']}/source/python/src/simplefunction.py --word {word}",
        dag=dag)

    
    start >> print_world
    print_world >> call_python
    call_python >> end

