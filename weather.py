import requests
import json
import pynotify
'''
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
    return weather #["hourly"]["data"][0]['precipType']

print parse_weather()
'''
def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
