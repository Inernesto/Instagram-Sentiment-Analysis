from flask import Flask, request, jsonify
from analyze_comments import analyze_sentiments
from fetch_comments import fetch_instagram_comments
from data_model import store_data
from data_model import get_all_data
from data_model import get_latest_data
from data_model import get_data_range

app = Flask(__name__)


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():

    access_token = ''  # access_token variable defined
    media_id = ''  # media_id variable defined

    if request.method == 'GET':
        access_token = request.args.get('access_token')
        media_id = request.args.get('media_id')
    elif request.method == 'POST':
        data = request.json
        access_token = data.get('access_token')
        media_id = data.get('media_id')

    comments = fetch_instagram_comments(access_token, media_id)

    # return jsonify(comments)

    if not comments:
        return jsonify({"error": "Unable to fetch comments"})

    # call the analyze_sentiments function with the comments as parameters
    analyzed_obj = analyze_sentiments(comments)

    # call the store_data function to store the analyzed data in the database
    return jsonify(store_data(media_id, analyzed_obj))


@app.route('/retrieve-all', methods=['GET', 'POST'])
def retrieve_all():

    media_id = ''  # media_id variable defined

    if request.method == 'GET':
        media_id = request.args.get('media_id')
    elif request.method == 'POST':
        data = request.json
        media_id = data.get('media_id')

    return jsonify(get_all_data(media_id))


@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve():

    media_id = ''  # media_id variable defined

    if request.method == 'GET':
        media_id = request.args.get('media_id')
    elif request.method == 'POST':
        data = request.json
        media_id = data.get('media_id')

    return jsonify(get_latest_data(media_id))


@app.route('/retrieve-range', methods=['GET', 'POST'])
def retrieve_range():

    media_id = ''  # media_id variable defined
    start = ''  # beginning of the date period
    end = ''  # end of the date period

    if request.method == 'GET':
        media_id = request.args.get('media_id')
        start = request.args.get('start')
        end = request.args.get('end')
    elif request.method == 'POST':
        data = request.json
        media_id = data.get('media_id')
        start = data.get('start')
        end = data.get('end')

    return jsonify(get_data_range(media_id, start, end))


if __name__ == '__main__':
    app.run(debug=True)
