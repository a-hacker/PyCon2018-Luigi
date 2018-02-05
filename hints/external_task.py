import luigi

class ExternalTaskClass(luigi.ExternalTask):
    def output(self):
        return luigi.LocalTarget("external_file.txt")

