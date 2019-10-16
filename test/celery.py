from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery('test_celery',
             broker='amqp://admin:mypass@plrom.niracler.com:5672',  # 中间件
             backend='amqp://admin:mypass@plrom.niracler.com:5672',  # 结果存储
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
