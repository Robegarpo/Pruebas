
from nautobot.extras.jobs import register_jobs
from .my_job import MiPrimerJob

register_jobs(MiPrimerJob)
