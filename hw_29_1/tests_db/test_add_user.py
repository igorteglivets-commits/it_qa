import pytest

@pytest.mark.db
def test_add_user(db_connection):
    cursor = db_connection.cursor()

    cursor.execute(
        "INSERT INTO users (name) VALUES (%s) RETURNING id;",
        ("Іван",)
    )
    user_id = cursor.fetchone()[0]

    cursor.execute(
        "SELECT name FROM users WHERE id = %s;",
        (user_id,)
    )

    user = cursor.fetchone()
    assert user[0] == "Іван"
