import pytest
from cloudevents.conversion import to_binary, to_structured
from cloudevents.http import CloudEvent

from cloudevents_python import __version__
from cloudevents_python.sample_server import app


def test_version():
    assert __version__ == "0.1.0"


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_binary_request(client):
    # This data defines a binary cloudevent
    attributes = {
        "type": "com.example.sampletype1",
        "source": "https://example.com/event-producer",
    }
    data = {"message": "Hello World!"}

    event = CloudEvent(attributes, data)
    headers, body = to_binary(event)

    r = client.post("/", headers=headers, data=body)
    assert r.status_code == 204


def test_structured_request(client):
    # This data defines a binary cloudevent
    attributes = {
        "type": "com.example.sampletype2",
        "source": "https://example.com/event-producer",
    }
    data = {"message": "Hello World!"}

    event = CloudEvent(attributes, data)
    headers, body = to_structured(event)

    r = client.post("/", headers=headers, data=body)
    assert r.status_code == 204
