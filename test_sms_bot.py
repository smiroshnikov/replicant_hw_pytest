import pytest
from utilities.fake_api import get_fake_rest_api_response_random
from utilities.json_utils import CustomerStatusViewer


@pytest.mark.sms
@pytest.mark.positive
@pytest.mark.smoke
def test_sms_delivered():
    response = get_fake_rest_api_response_random().json()
    assert CustomerStatusViewer.get_customer_status(response) == "NOTIFIED"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "DELIVERED"


@pytest.mark.sms
@pytest.mark.negative
@pytest.mark.smoke
def test_sms_not_delivered_first_attempt():
    response = get_fake_rest_api_response_random().json()
    assert CustomerStatusViewer.get_customer_status(response) == "SMS AGAIN"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "NO RESPONSE"
    assert CustomerStatusViewer.get_customer_sms_count(response) == 1


@pytest.mark.sms
@pytest.mark.negative
@pytest.mark.smoke
def test_sms_not_delivered_second_attempt():
    response = get_fake_rest_api_response_random().json()
    assert CustomerStatusViewer.get_customer_status(response) == "CALL CUSTOMER"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "NO RESPONSE"
    assert CustomerStatusViewer.get_customer_sms_count(response) == 2


@pytest.mark.sms
@pytest.mark.negative
@pytest.mark.smoke
def test_sms_not_delivered():
    response = get_fake_rest_api_response_random().json()
    assert CustomerStatusViewer.get_customer_status(response) == "CALL CUSTOMER"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "DELIVERY FAILED"


@pytest.mark.sms
@pytest.mark.negative
@pytest.mark.smoke
def test_sms_wrong_identity():
    response = get_fake_rest_api_response_random().json()
    assert CustomerStatusViewer.get_customer_status(response) == "VERIFY_ID"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "DELIVERED"


@pytest.mark.sms
@pytest.mark.negative
@pytest.mark.smoke
def test_sms_invalid_response_positive():
    response = get_fake_rest_api_response_random().json()
    assert CustomerStatusViewer.get_customer_status(response) == "NO RESPONSE"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "SMS AGAIN"
    assert CustomerStatusViewer.get_customer_sms_count(response) == 1


@pytest.mark.sms
@pytest.mark.negative
@pytest.mark.smoke
def test_sms_invalid_response_negative():
    response = get_fake_rest_api_response_random().json()
    assert CustomerStatusViewer.get_customer_status(response) == "NO RESPONSE"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "CALL CUSTOMER"
    assert CustomerStatusViewer.get_customer_sms_count(response) == 2


def test_add_some_green_to_random():
    assert True


def test_add_some_green_to_random2():
    assert True


def test_add_some_red_to_random2():
    assert False
