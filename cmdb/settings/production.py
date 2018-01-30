from .common import *

DEBUG = False
DJANGO_LOG_LEVEL = 'INFO'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'request_id': {
            '()': 'cmdb.filters.RequestIDFilter'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s [%(asctime)s] [%(request_id)s] %(module)s %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filters': ['request_id'],
            'formatter': 'standard',
            'filename': os.path.join(BASE_DIR, 'cmdb.log'),
        },
    },
    'loggers': {
        'cmdb': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "ROUTING": "cmdb.channel_route.routing",
    },
}