import pytest


@pytest.fixture(scope="module")
def preWork():
    print("Fixture Applied")


def test_initialCheck(preWork):
    print("First Test")


def test_secondCheck(preWork):
    print("Second Test")
