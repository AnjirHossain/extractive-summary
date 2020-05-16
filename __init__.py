from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from src.nlputils import summarize, load, get_text_from_page

app = Flask(__name__)
CORS(app)

# health check route
@app.route('/', methods=['GET'])
def health():
    return {'version': 'API v1'}, 200


@app.route('/api/v1/getsummary', methods=['POST'])
def get_summary():
    data = request.get_json()

    summary = None
    no_text = 'text' not in data
    no_url = 'url' not in data

    if data is None \
            or no_text \
            and no_url:
        return {'message': 'Malformed request, must provide either text or url to retrieve text'}, 400

    if not no_text and len(data['text']) == 0:
        return {'message': 'Malformed request, the source text is empty'}, 400

    if not no_url in data and len(data['url']) == 0:
        return {'message': 'Malformed request, the url of the source text is empty'}, 400

    if no_text:
        source_doc = get_text_from_page(data['url'])

        if source_doc is None:
            return {'message': 'Malformed request, the url provided couldn\'t be resolved'}, 400

        summary = summarize(source_doc)
    else:
        summary = summarize(data['text'])

    return {'summary': summary}, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
