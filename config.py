APP_NAME = "FLASK_DEMO"

# Mongo DB Config

ACTIVE_ENV = 'live'

ENVS = {
    'live': {
        "DB_HOST": 'localhost',
        "DB_USERNAME": '',
        "DB_PASSWORD": '',
        "DB_NAME": 'inventory',
        "DB_PORT": 27017,
    },
    'dev': {
        "DB_HOST": 'localhost',
        "DB_USERNAME": '',
        "DB_PASSWORD": '',
        "DB_NAME": 'inventory',
        "DB_PORT": 27017,
    },
    'test': {
        "DB_HOST": 'localhost',
        "DB_USERNAME": '',
        "DB_PASSWORD": '',
        "DB_NAME": 'inventory',
        "DB_PORT": 27017,
    }
}
