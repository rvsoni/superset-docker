from celery.schedules import crontab

FEATURE_FLAGS = {
    "ALERT_REPORTS": True
}

class CeleryConfig:
#    BROKER_URL = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
    CELERY_IMPORTS = ('superset.sql_lab', "superset.tasks", "superset.tasks.thumbnails", )
#    CELERY_RESULT_BACKEND = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_ACKS_LATE = True
    CELERY_ANNOTATIONS = {
        'sql_lab.get_sql_results': {
            'rate_limit': '100/s',
        },
        'email_reports.send': {
            'rate_limit': '1/s',
            'time_limit': 600,
            'soft_time_limit': 600,
            'ignore_result': True,
        },
    }
    CELERYBEAT_SCHEDULE = {
        'reports.scheduler': {
            'task': 'reports.scheduler',
            'schedule': crontab(minute='*', hour='*'),
        },
        'reports.prune_log': {
            'task': 'reports.prune_log',
            'schedule': crontab(minute=0, hour=0),
        },
    }
CELERY_CONFIG = CeleryConfig


SQLALCHEMY_DATABASE_URI = 'postgresql://superset:superset@192.168.29.151:5432/superset'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'

SCREENSHOT_LOCATE_WAIT = 100
SCREENSHOT_LOAD_WAIT = 600

SMTP_HOST = "localhost" #change to your host
#SMTP_STARTTLS = false
#SMTP_SSL = False
#SMTP_USER = "your_user"
SMTP_PORT = 25 # your port eg. 587
#SMTP_PASSWORD = "your_password"
SMTP_MAIL_FROM = "ravi.soni@GB8TRF2"

WEBDRIVER_TYPE = "chrome"
WEBDRIVER_OPTION_ARGS = [
    "--force-device-scale-factor=2.0",
    "--high-dpi-support=2.0",
    "--headless",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-extensions",
]

# This is for internal use, you can keep http
WEBDRIVER_BASEURL="http://superset:8088"
# This is the link sent to the recipient, change to your domain eg. https://superset.mydomain.com
WEBDRIVER_BASEURL_USER_FRIENDLY="http://localhost:8088"

ENABLE_SCHEDULED_EMAIL_REPORTS = True