import pytest
import psycopg2
import time

@pytest.fixture
def db_connection():
    for _ in range(10):  # retry
        try:
            conn = psycopg2.connect(
                host="postgres",
                port=5432,
                dbname="test_db",
                user="test_user",
                password="test_password"
            )
            conn.autocommit = False
            yield conn
            conn.rollback()
            conn.close()
            return
        except psycopg2.OperationalError:
            time.sleep(1)

    raise RuntimeError("Could not connect to Postgres")
