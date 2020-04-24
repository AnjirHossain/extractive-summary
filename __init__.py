from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from src.nlputils import summarize

app = Flask(__name__)


@app.route('/api/v1/getsummary', methods=['POST'])
def get_summary():
    data = request.get_json()

    if data is None \
            or data['text'] is None \
            or len(data['text']) == 0:
        return jsonify({'error': 'No data provided'})

    return jsonify({'text': summarize(doc=data['text'], rank_lower_bound=3)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
