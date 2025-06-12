from nautobot.extras.jobs import Job

class HelloJob(Job):
    def run(self, data, commit):
        self.log_success("¡Funciona!")
