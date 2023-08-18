import time
import schedule
import requests
from winotify import Notification

def fetch_request():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    quote = data[0]['q'] + " - " + data[0]['a']
    return quote

def sends(title, message):
    toast = Notification(app_id="For you.",
                         title=title,
                         msg=message,
                         duration="long",
                         icon=r"c:\somewhere\image.jpg" # Add image with the alert
                         )
    toast.show()

def schedule_notification():
    title = "For you."
    quote = fetch_request()
    schedule.every(2600).seconds.do(sends, title, quote)

if __name__ == "__main__":
    schedule_notification()
    while True:
        schedule.run_pending()
        time.sleep(1)
