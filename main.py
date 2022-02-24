from flask import Flask, request, jsonify, make_response
from logger import logger

app = Flask(__name__)


@app.route('/test', methods=["POST", "GET"])
def runn():
    if request.method == "POST":
        body = request.json
        logger.debug(body)
        return make_response(jsonify(body))
    body = request.json
    logger.debug(body)
    return make_response(jsonify(body))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2000)