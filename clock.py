from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import runpy
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    sys.argv = ['', 'getdata']
    runpy.run_path('manage.py')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
