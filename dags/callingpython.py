from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import logging

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
    logging.info(f"Word to be counted {kwargs['word']}")


dag = DAG('callingpython', 
        default_args=default_args,
        schedule_interval=None)

#words {"word_list": ["abracadabra","proparoxitona","dtc","airflow","fiap"]}
words = Variable.get(
    key="words",
    default_var={
        "word_list": ["fiap"]
    },
    deserialize_json=True
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

for word in words["word_list"]:

    print_world = PythonOperator(
        task_id=f'print_world_{words["word_list"].index(word)}',
        provide_context=True,
        python_callable=word_to_count,
        op_kwargs={'word': word},
        dag=dag,
    )

    call_python = BashOperator(
        task_id=f'word_count_{words["word_list"].index(word)}',
        bash_command=f'python /source/simplefunction.py {word}',
        dag=dag)

    
    start >> print_world
    print_world >> call_python
    call_python >> end

