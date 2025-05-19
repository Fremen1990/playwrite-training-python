import pytest


@pytest.fixture(scope="module")
def beforeAllHook():
    print("----------------\n BEFORE ALL TESTS!!!! \n --------------")
    yield
    print("----------------\n AFTER ALL TESTS!!! \n --------------")


@pytest.fixture()
def beforeEach():
    print("----------------\n BEFORE EACH TESTS!!!! \n --------------")
    yield
    print("----------------\n AFTER EACH TESTS!!! \n --------------")


def test_number_one(beforeAllHook, beforeEach):
    print("Test number 1")


def test_number_two(beforeAllHook, beforeEach):
    print("This is test2!")

# @pytest.fixture()
# def createData():
#     data = {'name':'tomek', 'age': 33}
#     return data


# def test_data(createData):
#     print(f"THE DATA: {createData}")
