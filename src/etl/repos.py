from dagster import repository
from src.etl.jobs import sample_job
from src.etl.schedules import sample_job_schedule


@repository
def etl():
    return {
        "jobs": {
            "sample_job": sample_job
        },
        "schedules": {
            "sample_job_schedule": sample_job_schedule,
        }
    }
