from flask import Flask, request
from redis import Redis
import os
import socket

app = Flask(__name__)
host = socket.gethostname()
user = "unknown"
card_num = ""

@app.route('/')
def hello():
    try:
        # Parse out the user from the request.
        user = request.args.get("user")
    except:
        return "Failed to parse arguments\n"

    try:
        # Look up that user's payment information, if it exists.
        redis = Redis(host='redis.user-data.svc.cluster.local', port=6379, socket_connect_timeout=1)
        card_num = redis.get(user)
    except Exception as e:
        return "%s: failed to connect to user payment database\n" % host

    if card_num:
        return '%s: found payment method "%s" for user/%s\n' % (host, card_num, user)
    else:
        return '%s: no payment information for user/%s"\n' %(host, user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
