import requests
import json
import appindicator
import notify2
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

# Parse the JSON payload
def parse_weather():
    weather = get_weather()
    #return weather["hourly"]["data"][0]['precipType']
    global current_temp
    global summary
    global icon_json
    current_temp = weather["currently"]["temperature"]
    summary = weather["currently"]["summary"]
    icon_json = weather["currently"]["icon"]

print parse_weather()


# Logic for notification icon based on icon from payload:

def get_icon(input):
    if input == "clear-day":
        return "/home/joe/weatherpy/icons/sun.png"
    elif input == "clear-night":
        return "/home/joe/weatherpy/icons/moon.png"
    elif input == "rain" or input == "sleet":
        return "/home/joe/weatherpy/icons/drizzle.png"
    elif input == "snow":
        return "/home/joe/weatherpy/icons/snow.png"
    elif input == "wind":
        return "/home/joe/weatherpy/icons/wind.png"
    elif input == "fog":
        return "/home/joe/weatherpy/icons/fog.png"
    elif input == "cloudy":
        return "/home/joe/weatherpy/icons/cloudy.png"
    elif input == "partly-cloudy-day":
        return "/home/joe/weatherpy/icons/partlycloudy_day.png"
    elif input == "partly-cloudy-night":
        return "/home/joe/weatherpy/icons/partlycloudy_night.png"
    else:
        return "/home/joe/weatherpy/icons/sun.png"

# Message for notification bubble
w_message = "It is currently %s degress" % current_temp + " with " + summary
image = get_icon(icon_json)

# Create the notificaiton bubble:

def sendweather(title, message, image):
    notify2.init("Test")
    notice = notify2.Notification(title, message, image)
    notice.show()
    title = "Current Weather"
    #message = parse_weather()
    return
sendweather("Current Weather", w_message, image)
