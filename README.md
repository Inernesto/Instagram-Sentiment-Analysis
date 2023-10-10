# Instagram-Sentiment-Analysis
Analyze Instagram Media/Posts to find the sentiment score on the comments. It is a service that can be deployed on a server or in the cloud. It makes use of Python's Flask Framework for handling HTTP requests, PyMongo for saving the scores of the analysis of each media for further analysis, and Google's NLP for the comment sentiments.   
# To Use It
The application integrating this service will need to call the "/analyze" endpoint and pass along the access token for the Instagram account as well as the specific media ID for the media that needs analysis. NB: The Instagram account must be either a business account or a creator account. It cannot be a personal account.   
The endpoints are as follows:   
GET /analyze?access_token={}&media_id={} or POST /analyze -d {access_token:"", media_id:""} NB: To fetch and analyze the media comments, and then store the analysis in a NoSQL i.e Mongo DB before returning the analysis back as a response.   
GET /retrieve-all?media_id={} or POST /analyze -d {media_id:""} NB: Fetches all the analysis done for a specific media.   
GET /retrieve?media_id={} or POST /analyze -d {media_id:""} NB: Fetches the most recent analysis done for a specific media.   
GET /retrieve-range?media_id={}&start={}&end={} or POST /analyze -d {media_id:"", start:"", end:""} NB: Fetches a range of analysis done for a specific media where start & end are dates in this format: %Y%m%d    
