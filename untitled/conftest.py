import pytest
@pytest.fixture(scope="session")
def login_fixture():
    print("前置条件")
    yield
    print("后置条件")


