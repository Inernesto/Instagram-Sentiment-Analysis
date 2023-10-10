# Replace this function with code to fetch Instagram comments using access_token, instagram_id, and media_id
import requests


def fetch_instagram_comments(access_token, media_id):

    # define the instagram end point to get the comments
    instagram_media_comments = f'https://graph.facebook.com/v14.0/{media_id}/comments?access_token={access_token}'

    # make the call to request the comments
    response = requests.get(instagram_media_comments)

    if not response:
        return None

    # get the json response
    data = response.json()

    # To return all the response object
    # return data

    # To return just the comments
    comments = [item['text'] for item in data["data"]]

    return comments
