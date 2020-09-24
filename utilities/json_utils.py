import json


class SerializerDeserializer(object):
    """
    Json serializer / deserializer
    """

    @staticmethod
    def string_2_json(j):
        return json.loads(j)

    @staticmethod
    def json_2_dict(filename_path):
        with open(filename_path) as f:
            d = json.load(f)
            return d


class CustomerStatusViewer(object):
    @staticmethod
    def get_customer_status(j) -> str:
        return j['customer']['customer_status']

    @staticmethod
    def get_customer_sms_status(j) -> str:
        return j['customer']['sms_status']

    @staticmethod
    def get_customer_sms_count(j) -> str:
        return j['customer']['sms_count']


if __name__ == '__main__':
    p = "C:\\Users\\Art3m15\\IdeaProjects\\replicant_hw_no_bdd\\fake_json_files" \
        "\\customer_NOTIFIED_DELIVERED.json "

    dd = SerializerDeserializer.json_2_dict(p)
    print(CustomerStatusViewer.get_customer_sms_status(dd))
    print(CustomerStatusViewer.get_customer_status(dd))
    print(CustomerStatusViewer.get_customer_sms_count(dd))
