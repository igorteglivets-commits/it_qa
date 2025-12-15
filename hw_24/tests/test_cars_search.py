import pytest
import logging
from helpers import (
    build_query_params,
    get_cars,
    assert_status_code,
    assert_limit,
    assert_sorted
)

logger = logging.getLogger("cars_search_tests")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("test_search.log")

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 1),
        ("brand", 7),
        ("price", None),
        ("year", 10),
    ],
    ids=[
        "sort_by_price_limit_5",
        "sort_by_year_limit_3",
        "sort_by_engine_limit_1",
        "sort_by_brand_limit_7",
        "sort_by_price_no_limit",
        "sort_by_year_limit_10",
    ]
)
class TestCarsSearch:

    def test_search_cars(self, auth_session, sort_by, limit):
        logger.info(f"Start test | sort_by={sort_by}, limit={limit}")

        params = build_query_params(sort_by, limit)
        response = get_cars(auth_session, params)

        assert_status_code(response)

        data = response.json()
        assert_limit(data, limit)
        assert_sorted(data, sort_by)

        logger.info(f"Test passed | returned={len(data)} cars")
