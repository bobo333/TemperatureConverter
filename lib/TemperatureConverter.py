from TemperatureErrors import TemperatureRangeError

class TemperatureConverter:
  def __init__(self, precision=2):
    self.abs_zero_celsius = 273.15
    self.precision = precision

  def cToF(self, celsius_value):
    """Convert Celsius to Fahrenheit"""
    return celsius_value * (9.0/5) + 32

  def cToK(self, celsius_value):
    """Convert Celsius to Kelvin"""
    return celsius_value + self.abs_zero_celsius

  def fToC(self, fahrenheit_value):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit_value - 32) * (5.0/9)

  def fToK(self, fahrenheit_value):
    """Convert Fahrenheit to Kelvin"""
    celsius_value = self.fToC(fahrenheit_value)
    return self.cToK(celsius_value)

  def kToC(self, kelvin_value):
    """Convert Kelvin to Celsius"""
    if (kelvin_value < 0): raise TemperatureRangeError(kelvin_value)
    return kelvin_value - self.abs_zero_celsius

  def kToF(self, kelvin_value):
    """Convert Kelvin to Fahrenheit"""
    celsius_value = self.kToC(kelvin_value)
    return self.cToF(celsius_value)