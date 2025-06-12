from nautobot.extras.jobs import Job

class MiPrimerJob(Job):
    def run(self, data, commit):
        self.log_success("¡Job ejecutado correctamente!")

