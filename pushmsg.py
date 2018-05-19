from apscheduler.schedulers.blocking import BlockingScheduler
import requests

API_ENDPOINT = "https://todo-list-by-gique.herokuapp.com:443/pushMsg"

sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes=1)
#def timed_job():
    #print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='*', hour=2, minute=49)
def scheduled_job():
    print('This job is run every day at 12pm.')
    r = requests.post(url = API_ENDPOINT, data = '')
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)

@sched.scheduled_job('cron', day_of_week='*', hour=12)
def scheduled_job():
    print('This job is run every day at 12pm.')
    r = requests.post(url = API_ENDPOINT, data = '')
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)

@sched.scheduled_job('cron', day_of_week='*', hour=18)
def scheduled_job():
    print('This job is run every day at 18pm.')
    r = requests.post(url = API_ENDPOINT, data = '')
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)

sched.start()