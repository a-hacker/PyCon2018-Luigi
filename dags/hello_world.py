import luigi

DATA_PATH = "/usr/local/luigi/datafiles/"
OUTPUT_PATH = "/usr/local/luigi/output/"

SUCCESS_MESSAGE = """
====================================================================================================
Congratulations on your first dag run!

The result was: {0}

Check out the scheduler UI at http://localhost:8082/static/visualiser/index.html#
====================================================================================================
"""


class ResourceTask(luigi.ExternalTask):
    resource_name = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(DATA_PATH + self.resource_name)


class HelloWorldTask(luigi.Task):

    dependencies = \
        {
            'greeting': ResourceTask('greeting.txt'),
            'subject': ResourceTask('subject.txt')
        }

    def requires(self):
        return self.dependencies

    def run(self):
        greeting = self.read_data('greeting') or 'Hello'
        subject = self.read_data('subject') or 'World'
        with self.output().open('w') as outfile:
            outfile.write(format_salutation(greeting, subject))

    def output(self):
        return luigi.LocalTarget(OUTPUT_PATH + 'hello_world.txt')

    def read_data(self, resource_key):
        with self.input()[resource_key].open('r') as resource:
            return resource.read()


def format_salutation(greeting, subject):
    return '{0} {1}!\n'.format(greeting, subject)


@HelloWorldTask.event_handler(luigi.Event.SUCCESS)
def print_result(task):
    with task.output().open('r') as output:
        result = output.read()
        print(SUCCESS_MESSAGE.format(result))


if __name__ == '__main__':
    luigi.run()
