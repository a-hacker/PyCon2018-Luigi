import luigi

class TaskClass(luigi.Task):
    def requires(self):
        # I specify dependencies for this task
        return AnotherTaskClass()

    def output(self):
        # I specify an output file for task data
        return luigi.LocalTarget("target_file")

    def run(self):
        # I run code!
        pass
