import pytest
from hw_14.hw_14_1 import log_event
LOGFILE = "login_system.log"
import logging
logging.basicConfig(filename=LOGFILE, level=logging.DEBUG)

#             Позитивні тести
@pytest.mark.parametrize(
    "status,expected_level",
    [
        ("success", logging.INFO),
        ("expired", logging.WARNING),
        ("failed", logging.ERROR),
    ]
)
def test_log_event_positive(status, expected_level, caplog):
    username = "ivan"

    with caplog.at_level(logging.DEBUG):
        log_event(username, status)

    assert len(caplog.records) == 1
    record = caplog.records[0]

    assert record.levelno == expected_level
    assert f"Username: {username}" in record.message
    assert f"Status: {status}" in record.message


@pytest.mark.parametrize(
    "status",
    [
        None,
        "",
        "unknown123",
    ]
)
def test_log_event_negative(status, caplog):
    username = "ivan"

    with caplog.at_level(logging.DEBUG):
        log_event(username, status)

    assert len(caplog.records) == 1
    record = caplog.records[0]

    # у всіх негативних кейсах має бути ERROR
    assert record.levelno == logging.ERROR

    assert f"Username: {username}" in record.message
    assert f"Status: {status}" in record.message
