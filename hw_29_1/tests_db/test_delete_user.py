import pytest

@pytest.mark.db
def test_delete_user(db_connection):
    cursor = db_connection.cursor()

    cursor.execute(
        "INSERT INTO users (name) VALUES (%s) RETURNING id;",
        ("Петро",)
    )
    user_id = cursor.fetchone()[0]

    cursor.execute(
        "DELETE FROM users WHERE id = %s;",
        (user_id,)
    )

    cursor.execute(
        "SELECT * FROM users WHERE id = %s;",
        (user_id,)
    )

    user = cursor.fetchone()
    assert user is None
