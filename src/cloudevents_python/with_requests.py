import sys

import requests
from cloudevents.conversion import to_binary, to_structured
from cloudevents.http import CloudEvent


def send_binary_cloud_event(url):
    # This data defines a binary cloudevent
    attributes = {
        "type": "com.example.sampletype1",
        "source": "https://example.com/event-producer",
    }
    data = {"message": "Hello World!"}

    event = CloudEvent(attributes, data)
    headers, body = to_binary(event)

    # send and print event
    requests.post(url, headers=headers, data=body)
    print(f"Sent {event['id']} from {event['source']} with {event.data}")


def send_structured_cloud_event(url):
    # This data defines a binary cloudevent
    attributes = {
        "type": "com.example.sampletype2",
        "source": "https://example.com/event-producer",
    }
    data = {"message": "Hello World!"}

    event = CloudEvent(attributes, data)
    headers, body = to_structured(event)

    # send and print event
    requests.post(url, headers=headers, data=body)
    print(f"Sent {event['id']} from {event['source']} with {event.data}")


def main():
    # expects a url from command line.
    # e.g. python3 client.py http://localhost:3000/
    if len(sys.argv) < 2:
        sys.exit("Usage: python with_requests.py <CloudEvents controller URL>")

    url = sys.argv[1]
    send_binary_cloud_event(url)
    send_structured_cloud_event(url)


if __name__ == "__main__":
    main()
