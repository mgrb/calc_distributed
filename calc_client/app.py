import logging
import os
from flask import Flask
from celery.execute import send_task

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
                        os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

APP_LOGGER = logging.getLogger()


def create_app():
    APP_LOGGER.info(f'Starting app in APP_ENV enviroment')
    app = Flask(__name__)
    app.config.from_object('config')

    # TODO: INSERT INIT API
    # TODO: INSERT INIT DB

    # TODO: ROUTE FILES

    @app.route('/')
    def home():
        for num in range(30000):
            send_task("SOMAR", [num*2, num])

        return f'Home da aplicação. Resultado'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
