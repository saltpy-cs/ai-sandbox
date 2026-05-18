import parse
import requests
from behave import given, register_type, when, then


@parse.with_pattern(r"https?://\S+")
def parse_url(text):
    return text


register_type(URL=parse_url)


@given("the titanic API is running on localhost:5000")
def step_api_is_running(context):
    try:
        response = requests.get("http://localhost:5000/health", timeout=5)
        assert response.status_code == 200, f"API health check failed: {response.status_code}"
    except requests.exceptions.ConnectionError:
        raise AssertionError("Titanic API is not running on localhost:5000")


@when("I send an API request to {url:URL}")
def step_send_api_request(context, url):
    context.response = requests.get(url, timeout=10)


@when("I send an API request to {url:URL} with the query {query}")
def step_send_api_request_with_query(context, url, query):
    key, value = query.split("=", 1)
    context.response = requests.get(url, params={key: value}, timeout=10)


@then("I get the information about the passenger with id {passenger_id:d}")
def step_check_single_passenger(context, passenger_id):
    assert context.response.status_code == 200, (
        f"Expected 200, got {context.response.status_code}"
    )
    passenger = context.response.json()
    assert isinstance(passenger, dict), f"Expected a dict, got {type(passenger)}"
    assert passenger["id"] == passenger_id
    for field in ("name", "age", "sex", "class", "survived"):
        assert field in passenger, f"Missing field: {field}"


@then("I get a 404 response")
def step_check_404(context):
    assert context.response.status_code == 404, (
        f"Expected 404, got {context.response.status_code}"
    )


@given("the titanic API is running")
def step_api_is_running_generic(context):
    try:
        response = requests.get(f"{context.base_url}/health", timeout=5)
        assert response.status_code == 200, f"API health check failed: {response.status_code}"
    except requests.exceptions.ConnectionError:
        raise AssertionError(f"Titanic API is not running at {context.base_url}")


@when("I send an API request to the passenger endpoint with the query {query}")
def step_send_api_request_passenger_with_query(context, query):
    params = dict(pair.split("=", 1) for pair in query.split(","))
    url = f"{context.base_url}/api/1/passenger"
    context.response = requests.get(url, params=params, timeout=10)


@then("I get the information for all surviving passengers")
def step_check_surviving_passengers(context):
    assert context.response.status_code == 200, (
        f"Expected 200, got {context.response.status_code}"
    )
    passengers = context.response.json()
    assert isinstance(passengers, list), f"Expected a list, got {type(passengers)}"
    assert len(passengers) > 0, "Expected at least one surviving passenger"
    for p in passengers:
        assert p["survived"] is True, f"Expected survived=True, got {p['survived']} for passenger {p['id']}"


@then("I get the information for all child passengers")
def step_check_child_passengers(context):
    assert context.response.status_code == 200, (
        f"Expected 200, got {context.response.status_code}"
    )
    passengers = context.response.json()
    assert isinstance(passengers, list), f"Expected a list, got {type(passengers)}"
    assert len(passengers) > 0, "Expected at least one child passenger"
    for p in passengers:
        assert p["age"] is not None, f"Passenger {p['id']} has no age"
        assert 0 <= p["age"] <= 18, f"Expected age between 0 and 18, got {p['age']} for passenger {p['id']}"


@then("I get the information for all male passengers")
def step_check_male_passengers(context):
    assert context.response.status_code == 200, (
        f"Expected 200, got {context.response.status_code}"
    )
    passengers = context.response.json()
    assert isinstance(passengers, list), f"Expected a list, got {type(passengers)}"
    assert len(passengers) > 0, "Expected at least one male passenger"
    for p in passengers:
        assert p["sex"] == "male", f"Expected sex=male, got {p['sex']} for passenger {p['id']}"


@then("I get the information for all female passengers who died on the titanic")
def step_check_female_dead_passengers(context):
    assert context.response.status_code == 200, (
        f"Expected 200, got {context.response.status_code}"
    )
    passengers = context.response.json()
    assert isinstance(passengers, list), f"Expected a list, got {type(passengers)}"
    assert len(passengers) > 0, "Expected at least one matching passenger"
    for p in passengers:
        assert p["sex"] == "female", f"Expected sex=female, got {p['sex']} for passenger {p['id']}"
        assert p["survived"] is False, f"Expected survived=False, got {p['survived']} for passenger {p['id']}"


@then("I get a list of the {count:d} passengers on the titanic when it sank")
def step_check_passenger_count(context, count):
    assert context.response.status_code == 200, (
        f"Expected 200, got {context.response.status_code}"
    )
    passengers = context.response.json()
    assert isinstance(passengers, list), f"Expected a list, got {type(passengers)}"
    assert len(passengers) == count, (
        f"Expected {count} passengers, got {len(passengers)}"
    )
