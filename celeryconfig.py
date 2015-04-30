from __future__ import absolute_import
from celery import Celery

mqhost = '192.168.0.6:5672/dNewsParser'
username = 'dNewsParser'
passwd = '1234'
app = Celery('ParseWorker', 
             broker='amqp://' + username + ':' + passwd + '@' + mqhost, 
             backend='amqp',
             include=['ParseWorker'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=120,
    CELERY_ROUTES = {
        'ParseWorker.parse': {'queue': 'url'},
    },
)
