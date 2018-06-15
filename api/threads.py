
import threading
from datetime import datetime
import requests

def syndicate(new_event):
    print("SYNDICATING...")

    eventbrite_url = "https://www.eventbriteapi.com/v3/events/?token=PJUFOO7Y6T6H6U64C7ZZ"

    # Format start and end time
    start_time = datetime.strptime(new_event['start_time'], '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = datetime.strptime(new_event['end_time'], '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%dT%H:%M:%SZ')

    json = {
        "event":
            {
                "name":{"html":new_event['name']},
                "description":{"html":new_event['description']},
                "start":{"utc":start_time,"timezone":new_event['start_timezone']},
                "end":{"utc":end_time,"timezone":new_event['end_timezone']},
                "currency":new_event['currency']
             }
    }

    res = requests.post(eventbrite_url, json=json)

    # Debugging
    print(res.status_code)
    print(res.text)

    return res.status_code

# interval in seconds
def check_db(interval):
    base_url = "http://127.0.0.1:5000/recentEvents"
    data = requests.get(base_url)
    for new_event in data.json():
        if syndicate(new_event) == 200:
            put_url = base_url + "/" + str(new_event['id'])
            requests.put(put_url)
    threading.Timer(interval, check_db, [interval]).start()