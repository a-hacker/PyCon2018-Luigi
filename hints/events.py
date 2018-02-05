import luigi

@luigi.Task.event_handler(luigi.Event.SUCCESS)
def celebrate_success(task):
    # do a thing
    pass


@luigi.Task.event_handler(luigi.Event.FAILURE)
def mourn_failure(task, exception):
    # do a thing
    pass


@TaskClass.event_handler(luigi.Event.FAILURE)
def mourn_failure(task, exception):
    # do a thing
    pass