'''
    TODO:
    - get either url or text from request
    - run extractive summary util
    - use stategy pattern instead of if / else
'''
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource

from src.nlputils import get_text_from_page, load, summarize

app = Flask(__name__)
CORS(app)

# health check route


@app.route('/', methods=['GET'])
def health():
    return {'version': 'API v1'}, 200


@app.route('/api/v1/getsummary', methods=['POST'])
def get_summary():
    data = request.get_json()

    error = {
        'malformed_req': ({'message': 'Malformed request, must provide either a body of unempty text or valid article url to retrieve text'}, 400),
        'unresolved_source_doc': ({'message': 'Malformed request, the url provided couldn\'t be resolved'}, 400)
    }

    text = data.get('text')
    url = data.get('url')

    if text and len(text) == 0:
        text = None
    if url and len(url) == 0:
        url = None

    if not (text or url):
        return error['malformed_req']

    source_doc = text if text is not None else get_text_from_page(url)

    if source_doc is None:
        return error['unresolved_source_doc']
    else:
        return {'summary': summarize(source_doc)}, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
