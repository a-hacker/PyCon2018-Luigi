import datetime

import luigi

# check out all the parameters: http://luigi.readthedocs.io/en/stable/api/luigi.parameter.html

class ParameterizedTask(luigi.Task):
    example_str = luigi.Parameter(default='foo')
    example_bool = luigi.BoolParameter(default=True)
    example_int = luigi.IntParameter(default=0)
    example_float = luigi.FloatParameter(default=10.5)
    example_dict = luigi.DictParameter(default={'fizz': 'buzz'})
    example_date = luigi.DateParameter(default=datetime.date.today())
    example_choice = luigi.ChoiceParameter(choices=[1, 2, 3], var_type=int)

