from dagster import ScheduleDefinition
from src.etl.jobs import sample_job


sample_job_schedule = ScheduleDefinition(
    job=sample_job,
    cron_schedule="0 8 * * *", 
    execution_timezone="Asia/Singapore",
)
