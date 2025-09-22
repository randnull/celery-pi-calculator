from app.src.celery_jobs.celery_object import celery_engine
from app.src.utils.pi import get_pi


@celery_engine.task(bind=True, name='pi.calculate')
def calculate_pi(self, n: int):

    def trigger(perc: float):
        self.update_state(state='PROGRESS', meta={'progress': perc, 'result': None})

    pi = get_pi(int(n), trigger)

    return pi
