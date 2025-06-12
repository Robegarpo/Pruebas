from nautobot.extras.jobs import Job

class MiJob(Job):
    def run(self, data, commit):
        self.log_success("Job cargado correctamente.")
