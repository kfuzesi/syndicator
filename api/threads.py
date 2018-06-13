
import threading
from integration import *

def syndicate(new_event):
    eventbrite_url = "test"
    api_post(eventbrite_url, )

# interval in seconds
def check_db(interval):
    base_url = "http://127.0.0.1:5000/recentEvents"
    data = api_get(base_url, None)
    for new_event in data.json():
        syndicate(new_event)
        put_url = base_url + "/" + str(new_event['id'])
        api_put(put_url, None)
    threading.Timer(interval, check_db, [10]).start()