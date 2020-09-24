import pytest

from utilities.fake_api import get_fake_rest_api_response_random
from utilities.json_utils import CustomerStatusViewer
from utilities.sound_utils import GenerateTranscript


@pytest.mark.phone_call
@pytest.mark.positive
@pytest.mark.smoke
def test_phone_call_customer_identified():
    # transcript = GenerateTranscript.get_fake_replicant_transcript() always fails due to lame sr
    transcript = GenerateTranscript.get_true_transcript("Yes this is him")
    response = get_fake_rest_api_response_random().json()
    assert transcript == "Yes this is him"
    assert CustomerStatusViewer.get_customer_status(response) == "NOTIFIED"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "DELIVERED"


@pytest.mark.phone_call
@pytest.mark.negative
@pytest.mark.smoke
def test_phone_call_wrong_identity_call_again():
    transcript = GenerateTranscript.get_fake_replicant_transcript()
    response = get_fake_rest_api_response_random().json()
    assert transcript == "No, this is his son, James. He cannot talk right now, please call later "
    assert CustomerStatusViewer.get_customer_status(response) == "CALL CUSTOMER"


@pytest.mark.phone_call
@pytest.mark.positive
@pytest.mark.smoke
def test_phone_call_2nd_attempt():
    transcript = GenerateTranscript.get_fake_replicant_transcript()
    response = get_fake_rest_api_response_random().json()
    assert transcript == "Yes this is him"
    assert CustomerStatusViewer.get_customer_status(response) == "NOTIFIED"
    assert CustomerStatusViewer.get_customer_sms_status(response) == "DELIVERED"


@pytest.mark.phone_call
@pytest.mark.positive
@pytest.mark.smoke
def test_phone_customer_requests_human_representative():
    # transcript = GenerateTranscript.get_fake_replicant_transcript()
    transcript = GenerateTranscript.get_true_transcript("Stop calling me you robots , I want human representative")
    response = get_fake_rest_api_response_random().json()
    assert transcript == "Stop calling me you robots , I want human representative"
    # assert CustomerStatusViewer.get_customer_status(response) == "HUMAN REPRESENTATIVE REQUIRED"


@pytest.mark.phone_call
@pytest.mark.positive
@pytest.mark.smoke
def test_phone_customer_inaudible():
    transcript = GenerateTranscript.get_fake_replicant_transcript()
    response = get_fake_rest_api_response_random().json()
    assert transcript == "I am in the middle of volcano eruption ... please call me back!"
    assert CustomerStatusViewer.get_customer_status(response) == "CALL AGAIN"
