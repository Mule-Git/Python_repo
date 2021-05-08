from mathfun.db_connection import StudentDB
import pytest


@pytest.fixture(scope = "module")
def base():
    print(" =======setup=========")

    db = StudentDB()
    db.connection(Python_repo/tests/dataa.json')
    yield db
    print("\n ========tear down =======")


def test_std1(base):

    std1 = base.get_data(100)
    assert std1['name'] == "Mule wol"

def test_std2(base):
    db = base
    std1 = db.get_data(200)
    assert std1['name'] == "Beti mesf"
