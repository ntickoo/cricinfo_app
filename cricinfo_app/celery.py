from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cricinfo_app.settings')

app = Celery('cricinfo_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    #name of the scheduler

    # 'add-every-2-seconds': {
    #     # task name which we have created in tasks.py

    #     'task': 'add_2_numbers',  
    #     # set the period of running
        
    #     'schedule': 2.0,
    #      # set the args 
         
    #     'args': (16, 16) 
    # },
    # #name of the scheduler

    # 'print-name-every-5-seconds': {  
    #     # task name which we have created in tasks.py

    #     'task': 'print_msg_with_name',  
        
    #     # set the period of running

    #     'schedule': 5.0,  
    #     # set the args

    #    'args': ("DjangoPY", )  
    # },
    'download-game-data-every-300-seconds': {  
        # task name which we have created in tasks.py

        'task': 'load_cricket_event_data_for_today',  
        
        # set the period of running

        'schedule': 300.0,  
        # set the args

    },
}