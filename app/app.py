import logging
import os

from flask import Flask

from api.caltulate_deposits import deposit
from api.common import healthcheck


class App(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_url_rule('/', 'healthcheck', healthcheck)
        self.add_url_rule('/deposit', 'deposit', deposit, methods=['POST'])


app = App(__name__)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


application = app


if __name__ == "__main__":
    port = os.environ.get("APP_PORT", 5000)
    app.run('0.0.0.0', port)
