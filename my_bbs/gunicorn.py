import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
# bind = '127.0.0.1:8080'
bind = 'unix:/tmp/gunicorn.sock'
daemon = True
worker_class = 'gevent'
timeout = 30
backlog =  2048
access_log_format = '%(h)s %(t)s "%(r)s" %(s)s %(b)s "%(a)s"'
accesslog = '/tmp/my_bbs_access.log'
errorlog = '/tmp/my_bbs_error.log'
loglevel = 'info'
