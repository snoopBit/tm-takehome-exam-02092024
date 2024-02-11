from dagster import repository
from src.etl.jobs import bank_etl_job
from src.etl.schedules import sample_job_schedule


@repository
def etl():
    return {
        "jobs": {
            "sample_job": bank_etl_job,
        },
        "schedules": {
            "sample_job_schedule": sample_job_schedule,
        }
    }
