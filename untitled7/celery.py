from __future__ import absolute_import,unicode_literals
from celery import Celery

import os
# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled7.settings')
from django.conf import settings
# 创建应用
app = Celery('untitled7')

# 酸配置应用
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
