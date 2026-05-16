import requests
from behave import given, when, then


@given("the titanic API is running on localhost:5000")
def step_api_is_running(context):
    try:
        response = requests.get("http://localhost:5000/health", timeout=5)
        assert response.status_code == 200, f"API health check failed: {response.status_code}"
    except requests.exceptions.ConnectionError:
        raise AssertionError("Titanic API is not running on localhost:5000")


@when("I send an API request to {url}")
def step_send_api_request(context, url):
    context.response = requests.get(url, timeout=10)


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
