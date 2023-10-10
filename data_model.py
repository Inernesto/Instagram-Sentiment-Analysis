from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # mongo connection url & port
db = client['sentiment_analysis']  # database name

sentiment_data = db['sentiment_data']  # collection name


def store_data(media_id, analyzed_obj):  # store the data of the analysis

    # check if the media id exists
    media = sentiment_data.find_one({"_id": media_id})

    if media:

        # preparing update query
        update_query = {
            '$push': {'data': analyzed_obj}
        }

        # updating the media id with the new analysis
        sentiment_data.update_one({'_id': media_id}, update_query)

    else:

        # preparing new sentiment data
        data = {
            '_id': media_id,
            'data': [analyzed_obj]
        }

        # inserting new sentiment data
        sentiment_data.insert_one(data)

    return analyzed_obj


def get_all_data(media_id=""):  # get all the analyzed data for the media id

    # fetch the data for the media id
    media = sentiment_data.find_one({"_id": media_id})

    # check if media exists
    if not media:
        return {"error": "Unable to retrieve data"}

    # pull the data field from the fetched result
    data = media.get('data', [])

    return data


def get_latest_data(media_id=""):  # get the last analyzed data for the media id

    # fetch the data for the media id
    media = sentiment_data.find_one({"_id": media_id})

    # check if media exists
    if not media:
        return {"error": "Unable to retrieve data"}

    # pull the data field from the fetched result
    data = media.get('data', [])

    # check to see if the fetched array has data and return the latest/last analysis
    if len(data) > 0:
        return data[-1]

    return data


def get_data_range(media_id="", start="", end=""):

    # convert the start string to int
    start = int(start)

    # convert the end string to int
    end = int(end)

    # Define the query to find documents by media_id
    query = {
        '_id': media_id
    }

    # Find the document based on the media_id
    media = sentiment_data.find_one(query)

    # check if media exists
    if not media:
        return {"error": "Unable to retrieve data"}

    # Initialize an empty list to store selected data objects
    selected_data = []

    if media:
        # Get the 'data' array from the document
        data_array = media.get('data', [])

        # Loop through the 'data' array and select objects with dates in the specified range
        for data_item in data_array:
            date_str = data_item.get('date')
            if date_str:
                date = int(date_str)
                if start <= date <= end:
                    selected_data.append(data_item)

    return selected_data






