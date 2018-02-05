import luigi

class ExampleTask(luigi.Task):
    foo = luigi.Parameter()
    pass


class SingleDependencyTask(luigi.Task):
    def requires(self):
        return ExampleTask()

    def run(self):
        with self.input().read('r'):
            pass



class MultipleDependenciesTask(luigi.Task):
    def requires(self):
        return [ExampleTask('first'),
                ExampleTask('second')]

    def run(self):
        for dep in self.input():
            with dep.read('r'):
                pass


class DictDependenciesTask(luigi.Task):
    def requires(self):
        return {'first': ExampleTask('first'),
                'second': ExampleTask('second')}

    def run(self):
        with self.input()['first'].open('r'):
            pass
        with self.input()['second'].open('r'):
            pass


class DynamicDependenciesTask(luigi.Task):
    dep_count = luigi.IntParameter(default=5)

    def requires(self):
        return [ExampleTask(x)
                for x
                in range(0, self.dep_count)]

    def run(self):
        for dep in self.input():
            with dep.read('r'):
                pass