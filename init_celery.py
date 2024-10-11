from celery import Celery
from celery.schedules import crontab


app = Celery('tasks',
             broker='amqp://vikash:vikash@localhost//',
             )

app.autodiscover_tasks(["tasks.celery_tasks"])
app.conf.timezone = "Asia/Kolkata"

app.conf.beat_schedule = {
    # Executes every Monday to Friday, from  9 a.m.
    'add-every-monday-morning': {
        'task': 'nifty_index_stock_data_capturing',
        'schedule': crontab(minute='*/5', hour='9-16', day_of_week='mon-fri'),
        'args': ("NIFTY 50", ),
    },

}
