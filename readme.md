# PUSH-MSG
- Run on python app using BlockingScheduler and requests
- This Job run everyday at 12:00pm and 18:00pm in thailand.
- Cron example: http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html

## Running Locally
Make sure you have [python](https://www.python.org) and the [pip](https://pip.pypa.io/en/stable/installing/) installed.

```sh
$ python pushmsg.py
```

## Deploying to Heroku
```
$ heroku create
$ git push heroku master
$ heroku open
```

## Change source code
```
$ heroku git:remote -a {heroku app name}
$ git add .
$ git commit -m "First commit"
$ git push heroku master
```

## Logs
```
$ heroku logs --tail
```