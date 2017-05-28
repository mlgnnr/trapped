from apscheduler.schedulers.blocking import BlockingScheduler
import runpy
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    runpy.run_path("manage.py getdata")


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
