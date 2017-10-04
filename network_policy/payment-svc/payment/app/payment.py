from flask import Flask, request
from redis import Redis
import os
import socket

app = Flask(__name__)
host = socket.gethostname()
user = "unknown"
card_num = "1234-5667-2468-1357"

@app.route('/')
def hello():
    try:
        # Parse out the user from the request.
        user = request.args.get("user")
    except:
        return "Failed to parse arguments"

    try:
        # Store the user's payment information (just credit card number)
        # in the user database.
        redis = Redis(host='redis.user-data.svc.cluster.local', port=6379, socket_connect_timeout=1)
        redis.set(user, card_num)
    except Exception as e:
        return "%s: failed to connect to user payment database" % host

    # Success.
    return '%s: stored payment information (card=%s) for user/%s\n' % (host, card_num, user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
