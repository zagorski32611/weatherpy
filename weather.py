import requests
import json
import appindicator
import pynotify
import gtk
import signal

# Create new app indicator with name and icon:
app = appindicator.Indicator("weatherpy", '/home/joe/weatherpy/icons/sun.png', appindicator.CATEGORY_APPLICATION_STATUS)
app.set_status(appindicator.STATUS_ACTIVE)

# Create app menu:
menu = gtk.Menu()
gw = gtk.MenuItem("Get Weather")
qi = gtk.MenuItem("Quit")

# append gw and qi to Menu
menu.append(gw)
menu.append(qi)

# set menu to application:
app.set_menu(menu)
gw.show()
qi.show()


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

def parse_weather():
    weather = get_weather()
    #return weather["hourly"]["data"][0]['precipType']
    global current_temp
    global summary
    current_temp = weather["currently"]["temperature"]
    summary = weather["currently"]["summary"]
    icon = weather["currently"]["icon"]

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
