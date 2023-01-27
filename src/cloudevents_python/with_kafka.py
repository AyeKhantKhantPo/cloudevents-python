import structlog
from cloudevents.http import CloudEvent
from cloudevents.kafka import KafkaMessage, to_structured
from kafka import KafkaProducer

log = structlog.get_logger()


def send_cloud_event():
    # This data defines a binary cloudevent
    attributes = {
        "datacontenttype": "application/json",
        "type": "cpe.provision.v1",
        "source": "cpems.provision.terminal1",
    }
    data = {"cid": "CK123456", "mac": "AA-BB-CC-DD-EE-FF"}

    event = CloudEvent(attributes, data)
    print(event)

    # send to kafka and print event
    kafka_msg: KafkaMessage = to_structured(event)
    print(kafka_msg)
    msg = kafka_msg.value

    producer = KafkaProducer(retries=5, bootstrap_servers=["localhost:9092"])

    def on_success(record):
        print(record.topic)
        print(record.partition)
        print(record.offset)
        print(record)

    def on_error(excp):
        log.error(excp)
        raise Exception(excp)

    # send the message to mytopic
    producer.send("my-topic", msg).add_callback(on_success).add_errback(on_error)
    # block until all async messages are sent
    producer.flush()

    print(f"Sent {event['id']} from {event['source']} with {event.data}")


def main():
    send_cloud_event()


if __name__ == "__main__":
    main()
