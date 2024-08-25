""" 
The Observer design pattern is a behavioral pattern that defines a 
one-to-many dependency between objects. When one object (the subject) changes state,
all its dependents (observers) are notified and updated automatically.
"""

from abc import ABC, abstractmethod
#Subject: A WeatherStation class (the subject) that maintains weather data and notifies observers when data changes.
class WeatherStation:
    def __init__(self):
        self.temperature =0
        self.humidity =0
        self.pressure =0
        self.observers = []
        
    def registerObserver(self, observer):
        self.observers.append(observer)
    
    def removeObserver(self,observer):
        self.observers.remove(observer)
        
    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        self.notifyObservers()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

#Observer:The Observer abstract base class that defines the interface for objects that should be 
# notified of changes in the WeatherStation.
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

#Concrete Observer: Implement observer interface
class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Current conditions: {temperature}F degrees and {humidity}% humidity")
    
#Concrete Observer: Implement observer interface    
class StatisticsDisplay(Observer):
    def __init__(self):
        self.temp_sum =0
        self.num_readings = 0
        
    def update(self, temperature, humidity, pressure):
        self.temp_sum += temperature
        self.num_readings +=1
        avg_temp = self.temp_sum / self.num_readings
        print(f"Avg. temperature: {avg_temp:.1f}F")
 
#Concrete Observer: Implement observer interface       
class ForecastDisplay(Observer):
    def __init__(self):
        self.last_pressure =0
        self.current_pressure =0
    def update(self, temperature, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        
        if self.current_pressure > self.last_pressure:
            print("Forecast: Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("Forecast: More of the same")
        else:
            print("Forecast: Watch out for cooler, rainy weather")
            


if __name__ == "__main__":
    weather_station = WeatherStation()

    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()

    weather_station.registerObserver(current_display)
    weather_station.registerObserver(stats_display)
    weather_station.registerObserver(forecast_display)

    print("First weather update:")
    weather_station.setMeasurements(80, 65, 30.4)
    
    print("\nSecond weather update:")
    weather_station.setMeasurements(82, 70, 29.2)
    
    print("\nThird weather update:")
    weather_station.setMeasurements(78, 90, 29.2)
    
    
""" 
Main benefits:

Loose coupling between subject and observers
Support for broadcast communication
Easy addition of new observers without modifying the subject

"""