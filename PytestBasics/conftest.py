import pytest

#Session scope fixtures run once per session
#Module scope fixtures run once per file
#Function scope fixtures run once for each tests

@pytest.fixture(scope="session")
def preWork():
    print("Fixture Applied-Session")

@pytest.fixture(scope="module")
def preWork2():
    print("Fixture Applied-Module")
    yield
    print("Teardown Validation")

@pytest.fixture()
def preWork3():
    print("Fixture Applied-Function")
    return "pass"
