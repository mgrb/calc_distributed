from celery import Celery
from controller.calc_controller import CalcController
import config


def make_celery():
    celery = Celery(__name__, broker=config.CELERY_BROKER,
                    include=config.CELERY_TASKS)
    celery.conf.update(config.as_dict())
    return celery


app = make_celery()
