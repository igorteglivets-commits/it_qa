import psycopg2
import pytest

@pytest.fixture
def db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="test_db",
        user="test_user",
        password="test_password"
    )

    conn.autocommit = False  # дуже важливо для rollback
    yield conn

    conn.rollback()  # відкочуємо всі зміни
    conn.close()
