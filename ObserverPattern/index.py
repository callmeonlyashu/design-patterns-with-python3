from CWeatherMobileSubscriber import WeatherMobileSubscriber as mobile_subscriber
from CWeatherMonitorSubscriber import WeatherMonitorSubscriber as monitor_subscriber
from CWeatherPublisher import Weather

weatherinfo = Weather()
mobile = mobile_subscriber(weatherinfo)
monitor = monitor_subscriber(weatherinfo)

weatherinfo.setMeasurements(80, 65, 34.5)

weatherinfo.setMeasurements(12, 15, 32.5)