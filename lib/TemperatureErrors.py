class TemperatureError(Exception): pass
class TemperatureRangeError(TemperatureError):
  def __init__(self, temperature):
    self.value = "%s is below absolute 0 and therefore impossible." % temperature
  def __str__(self):
    return repr(self.value)