from models.manager import Manager


def test_manager_name():

    manager = Manager(
        "John",
        "john@gmail.com"
    )

    assert manager.name == "John"