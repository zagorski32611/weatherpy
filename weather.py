import requests
import json
import appindicator
import notify2
import gtk
import signal

# Get info from Dark Sky, only daily forcasts by exclude minutely and hourly forecasts:
r = requests.get("https://api.darksky.net/forecast/2b41959f8298b697485d46bea2477504/41.443234,-81.774603?exclude=minutely,hourly")

# Get response and convert to json
def get_weather():
    if r.status_code != 200:
        print "Shit's broke!!"
    else:
        weather = r.json()
        return weather
#print get_weather()

# Parse the JSON payload
def parse_weather():
    weather = get_weather()
    #return weather["hourly"]["data"][0]['precipType']
    global current_temp
    global summary
    current_temp = weather["currently"]["temperature"]
    summary = weather["currently"]["summary"]
    icon = weather["currently"]["icon"]

print parse_weather()

# Message for notification bubble
w_message = "It is currently %s degress" % current_temp + " with " + summary
image ='/home/joe/weatherpy/icons/sun.png'
# Create the notificaiton bubble:

def sendweather(title, message, image):
    notify2.init("Test")
    notice = notify2.Notification(title, message, image)
    notice.show()
    title = "Current Weather"
    #message = parse_weather()
    return
sendweather("Current Weather", w_message, image)
