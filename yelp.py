import config # importing env variables from dotenv
import requests # open a web url 
import json # json used to transmit web data


# get events for the city name a user types in. 
def get_businesses( city ):

    # use the dotenv file to find the correct variable for Yelp
    # need to use Yelp key name
    headers = { "Authorization": f"Bearer {config.YELP_AUTH_TOKEN}" }
    params = {"location": city, "limit": 10, "term": "seafood"}

    # the Request() method calls an external URL from our Python server
    request = requests.get(
        "https://api.yelp.com/v3/businesses/search",
        params=params,  # parameters are passed via the URL
        headers=headers, # headers are variables passed DIRECTLY to the server
    )

    # get a JSON response from Yelp. 
    # They keep the info we need in the response_body.events.
    # returns a JSON array of events in a city
    return json.loads(request.text)["businesses"]
