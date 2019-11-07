from config.celery import app


@app.task
def get_rate():
    """
    Periodic task that executes once a day at midnight.
    """
    from apps.currency.models import Rate
    Rate.sync()
