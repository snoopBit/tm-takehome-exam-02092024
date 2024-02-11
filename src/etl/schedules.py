from dagster import ScheduleDefinition
from src.etl.jobs import bank_etl_job


sample_job_schedule = ScheduleDefinition(
    job=bank_etl_job,
    cron_schedule="0 8 * * *", 
    execution_timezone="Asia/Singapore",
)