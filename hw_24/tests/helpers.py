BASE_URL = "http://127.0.0.1:8080"


def build_query_params(sort_by, limit):
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit
    return params


def get_cars(session, params):
    return session.get(f"{BASE_URL}/cars", params=params)


def assert_status_code(response, expected=200):
    assert response.status_code == expected


def assert_limit(data, limit):
    if limit:
        assert len(data) == limit


def assert_sorted(data, sort_by):
    values = [car[sort_by] for car in data]
    assert values == sorted(values)
