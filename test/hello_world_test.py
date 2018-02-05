from unittest import mock

import luigi
from luigi.mock import MockTarget

from dags.hello_world import ResourceTask
from dags.hello_world import HelloWorldTask
from dags.hello_world import format_salutation


class ResourceMock(ResourceTask):

    def output(self):
        target = MockTarget('{}.txt'.format(self.resource_name))
        with target.open('w') as t:
            t.write(str(self.resource_name))
        return target


@mock.patch('dags.hello_world.HelloWorldTask.requires')
@mock.patch('dags.hello_world.HelloWorldTask.output')
def test_hello_world_uses_resources(hw_out, hw_req):
    hw_req.return_value = {
            'greeting': ResourceMock('This is'),
            'subject': ResourceMock('a test')
        }
    hw_out.return_value = luigi.LocalTarget(is_tmp=True)
    test_task = HelloWorldTask()
    luigi.build([test_task], local_scheduler=True)

    with test_task.output().open('r') as test_file:
        assert test_file.read() == 'This is a test!\n'


@mock.patch('dags.hello_world.HelloWorldTask.requires')
@mock.patch('dags.hello_world.HelloWorldTask.output')
def test_hello_world_empty_resources(hw_out, hw_req):
    hw_req.return_value = {
        'greeting': ResourceMock(''),
        'subject': ResourceMock('')
    }
    hw_out.return_value = luigi.LocalTarget(is_tmp=True)
    test_task = HelloWorldTask()
    luigi.build([test_task], local_scheduler=True)

    with test_task.output().open('r') as test_file:
        assert test_file.read() == 'Hello World!\n'


def test_format_salutation():
    assert format_salutation('Hello', 'World') == 'Hello World!\n'
