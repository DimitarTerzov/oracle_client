import requests

from was_service_client.client import JobserviceClient, EventprocessorClient, ReportconsumerClient

host = "test_hostname"


def test_create_jobservice_client():
    js_client = JobserviceClient(host=host)
    assert js_client.host == host


def test_create_eventprocessor_client():
    ep_client = EventprocessorClient(host=host)
    assert ep_client.host == host


def test_create_jobservice_client_no_host():
    js_client = JobserviceClient()
    assert js_client.host == 'https://localhost:7443'


def test_create_eventprocessor_client_no_host():
    ep_client = EventprocessorClient()
    assert ep_client.host == 'https://localhost:6443'


def test_create_jobservice_client_with_custom_session():
    custom_session = requests.Session()
    custom_session.verify = True
    custom_session.cert = ('TEST', 'CERT')
    js_client = JobserviceClient(session=custom_session)
    assert js_client.session == custom_session


def test_create_eventprocessor_client_with_custom_session():
    custom_session = requests.Session()
    custom_session.verify = True
    custom_session.cert = ('TEST', 'CERT')
    ep_client = EventprocessorClient(session=custom_session)
    assert ep_client.session == custom_session
