from cloudevents.http import from_http
from flask import Flask, request

app = Flask(__name__)


# create an endpoint at http://localhost:/3000/
@app.route("/", methods=["POST"])
def home():
    # create a CloudEvent
    event = from_http(request.headers, request.get_data())

    # you can access cloudevent fields as seen below
    print(
        f"Found {event['id']} from {event['source']} with type "
        f"{event['type']} and specversion {event['specversion']}"
    )
    print(f"DATA : {event.data}")

    return "", 204


def main():
    app.run(port=3000)


if __name__ == "__main__":
    main()
