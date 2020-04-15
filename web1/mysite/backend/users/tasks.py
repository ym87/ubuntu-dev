from django.core import management

from mysite import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
