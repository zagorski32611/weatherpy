import requests
import json
import pynotify

r = requests.get("https://api.darksky.net/forecast/2b41959f8298b697485d46bea2477504/41.443234,-81.774603?exclude=minutely,hourly")

def get_weather():
    if r.status_code != 200:
        print "Shit's broke!!"
    else:
        weather = r.json()
        return weather
#print get_weather()

def parse_weather():
    weather = get_weather()
    #return weather["hourly"]["data"][0]['precipType']
    global current_temp
    global summary
    current_temp = weather["currently"]["temperature"]
    summary = weather["currently"]["summary"]

print parse_weather()

w_message = "It is currently %s degress" % current_temp + " with " + summary

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    title = "Current Weather"
    message = parse_weather()
    return
sendmessage("Current Weather", w_message)
