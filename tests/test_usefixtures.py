import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Clearing books database]")

@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Filling books database]")


@pytest.mark.usefixtures("fill_books_database")
def test_read_books_database():
    ...