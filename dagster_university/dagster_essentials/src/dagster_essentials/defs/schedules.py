from typing import Union
import dagster as dg

# src/dagster_essentials/defs/schedules.py
from dagster_essentials.defs.jobs import trip_update_job

trip_update_schedule = dg.ScheduleDefinition(
    job=trip_update_job,
    cron_schedule="0 0 5 * *", # every 5th of the month at midnight
)

# src/dagster_essentials/defs/schedules.py
from dagster_essentials.defs.jobs import weekly_update_job

weekly_update_schedule = dg.ScheduleDefinition(
    job=weekly_update_job,
    cron_schedule="0 0 * * 1", # every Monday at midnight
)