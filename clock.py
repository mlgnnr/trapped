from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=10)
def timed_job():
    subprocess.call(['./manage.py', 'getdata'])


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
