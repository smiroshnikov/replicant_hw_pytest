import requests
import requests_mock

from utilities.json_utils import SerializerDeserializer, CustomerStatusViewer
from utilities.random_utils import FileUtils

_P = "C:\\Users\\Art3m15\\IdeaProjects\\replicant_hw_no_bdd\\fake_json_files"


# TODO  move to conftest.py as a pytest fixture

def get_fake_rest_api_response_random():
    # get random test result each time
    random_json_file = FileUtils.pick_a_random_file_from_folder(_P)
    print(random_json_file)
    session = requests.Session()
    fake_adapter = requests_mock.Adapter()
    session.mount('mock://', fake_adapter)

    fake_adapter.register_uri('GET', 'mock://replicant.ai/tyrell_corp/sms_bot',
                              json=SerializerDeserializer.json_2_dict(random_json_file),
                              status_code=200)
    resp = session.get('mock://replicant.ai/tyrell_corp/sms_bot')
    return resp


if __name__ == '__main__':
    # print(get_fake_sms_api_response_random().json())

    print(CustomerStatusViewer.get_customer_sms_status(get_fake_rest_api_response_random().json()))
    print("random iteration")
    print(CustomerStatusViewer.get_customer_status(get_fake_rest_api_response_random().json()))
    print(CustomerStatusViewer.get_customer_status(get_fake_rest_api_response_random().json()))
    print(CustomerStatusViewer.get_customer_status(get_fake_rest_api_response_random().json()))
