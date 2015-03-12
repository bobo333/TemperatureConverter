from TemperatureErrors import TemperatureRangeError

class TemperatureConverter:
  def __init__(self, precision=2):
    self.zero_celsius_in_kelvin = 273.15
    self.abs_zero_celsius = -self.zero_celsius_in_kelvin
    self.abs_zero_fahrenheit = -459.67
    self.precision = precision

  def cToF(self, celsius_value):
    """Convert Celsius to Fahrenheit"""
    if (celsius_value < self.abs_zero_celsius): raise TemperatureRangeError('oops')
    return celsius_value * (9.0/5) + 32

  def cToK(self, celsius_value):
    """Convert Celsius to Kelvin"""
    if (celsius_value < self.abs_zero_celsius): raise TemperatureRangeError('oops')
    return celsius_value + self.zero_celsius_in_kelvin

  def fToC(self, fahrenheit_value):
    """Convert Fahrenheit to Celsius"""
    if (fahrenheit_value < self.abs_zero_fahrenheit): raise TemperatureRangeError('oops')
    return (fahrenheit_value - 32) * (5.0/9)

  def fToK(self, fahrenheit_value):
    """Convert Fahrenheit to Kelvin"""
    if (fahrenheit_value < self.abs_zero_fahrenheit): raise TemperatureRangeError('oops')
    celsius_value = self.fToC(fahrenheit_value)
    return self.cToK(celsius_value)

  def kToC(self, kelvin_value):
    """Convert Kelvin to Celsius"""
    if (kelvin_value < 0): raise TemperatureRangeError(kelvin_value)
    return kelvin_value - self.zero_celsius_in_kelvin

  def kToF(self, kelvin_value):
    """Convert Kelvin to Fahrenheit"""
    if (kelvin_value < 0): raise TemperatureRangeError(kelvin_value)
    celsius_value = self.kToC(kelvin_value)
    return self.cToF(celsius_value)