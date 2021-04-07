# birthdays.py
import datetime
import mysql.connector
from celery import Celery
from celery.schedules import crontab
app = Celery('birthdays', broker="pyamqp://guest@localhost//")
# disable UTC so that Celery can use local time
app.conf.enable_utc = False
@app.task
def birthdays_today():
    print("la puta que lo pario")
    return 666
# add "birthdays_today" task to the beat schedule
app.conf.beat_schedule = {
    "birthday-task": {
        "task": "birthdays.birthdays_today",
        "schedule": crontab(minute=52)
    }
}