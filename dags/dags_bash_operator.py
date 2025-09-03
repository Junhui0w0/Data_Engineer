from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


import datetime
import pendulum

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *", # 분 시 일 월 요일
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, #구간에 누락된 값을 전부 다 돌릴 것 인가 ?

) as dag:
    bash_t1 = BashOperator(
        task_id = "bash_t1", # 네모 박스 안에 있는 태스크 명
        bash_command = "echo whoami", # 어떤 스크립트를 실행할 것인지
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2", # 네모 박스 안에 있는 태스크 명
        bash_command = "echo $HOSTNAME", # 어떤 스크립트를 실행할 것인지
    )

    bash_t1 >> bash_t2 #bash_t1 다음 bash_t2 작업을 수행