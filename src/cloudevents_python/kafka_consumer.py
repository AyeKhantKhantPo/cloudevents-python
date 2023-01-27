import json

from kafka import KafkaConsumer


def main():
    # To consume from fintechexplained-topic
    consumer = KafkaConsumer(
        "my-topic",
        group_id="my-group",
        enable_auto_commit=False,
        bootstrap_servers=["localhost:9092"],
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )
    for message in consumer:
        print(message.topic)
        print(message.partition)
        print(message.offset)
        print(message.key)
        print(message.value)


if __name__ == "__main__":
    main()
