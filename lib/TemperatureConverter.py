from TemperatureErrors import TemperatureRangeError

class TemperatureConverter:
  def __init__(self, precision=2):
    self.zero_celsius_in_kelvin = 273.15
    self.abs_zero_celsius = -self.zero_celsius_in_kelvin
    self.abs_zero_fahrenheit = -459.67
    self.precision = precision

  def cToF(self, celsius_value):
    """Convert Celsius to Fahrenheit"""
    self.__checkCelsiusRange(celsius_value)
    return celsius_value * (9.0/5) + 32

  def cToK(self, celsius_value):
    """Convert Celsius to Kelvin"""
    self.__checkCelsiusRange(celsius_value)
    return celsius_value + self.zero_celsius_in_kelvin

  def fToC(self, fahrenheit_value):
    """Convert Fahrenheit to Celsius"""
    self.__checkFahrenheitRange(fahrenheit_value)
    return (fahrenheit_value - 32) * (5.0/9)

  def fToK(self, fahrenheit_value):
    """Convert Fahrenheit to Kelvin"""
    self.__checkFahrenheitRange(fahrenheit_value)
    celsius_value = self.fToC(fahrenheit_value)
    return self.cToK(celsius_value)

  def kToC(self, kelvin_value):
    """Convert Kelvin to Celsius"""
    self.__checkKelvinRange(kelvin_value)
    return kelvin_value - self.zero_celsius_in_kelvin

  def kToF(self, kelvin_value):
    """Convert Kelvin to Fahrenheit"""
    self.__checkKelvinRange(kelvin_value)
    celsius_value = self.kToC(kelvin_value)
    return self.cToF(celsius_value)

  def __checkCelsiusRange(self, celsius_value):
    """Raise TemperatureRangeError if celsius_value is below absolute zero"""
    if (celsius_value < self.abs_zero_celsius): raise TemperatureRangeError(celsius_value)

  def __checkFahrenheitRange(self, fahrenheit_value):
    if (fahrenheit_value < self.abs_zero_fahrenheit): raise TemperatureRangeError(fahrenheit_value)

  def __checkKelvinRange(self, kelvin_value):
    if (kelvin_value < 0): raise TemperatureRangeError(kelvin_value)