from models.task import Task


def test_complete_task():

    task = Task("Lay foundation")

    task.complete()

    assert task.status == "Completed"