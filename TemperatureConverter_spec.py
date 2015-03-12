# TemperatureConverter Tests

import unittest
from lib.TemperatureConverter import TemperatureConverter
from lib.TemperatureErrors import TemperatureRangeError

temp_converter = TemperatureConverter()

class KnownValues(unittest.TestCase):
  knownValues = (
    (0, 32),
    (100, 212)
  )

  # test value conversions
  def testCtoF(self):
    """cToF should return the known Fahrenheit value for the
       provided Celsius value."""
    for c_val, f_val in self.knownValues:
      result = temp_converter.cToF(c_val)
      self.assertEqual(result, f_val)

  def testCtoK(self):
    """cToK should return 273.15 Kelvin for 0 Celsius"""
    result = temp_converter.cToK(0)
    self.assertEqual(result, 273.15)

  def testFtoC(self):
    """fToC should return the known Celsius value for the 
       provided Fahrenheit value."""
    for c_val, f_val in self.knownValues:
      result = temp_converter.fToC(f_val)
      self.assertEqual(result, c_val)

  def testFtoK(self):
    """fToK should return 273.15 Kelvin for 32 Fahrenheit"""
    result = temp_converter.fToK(32)
    self.assertEqual(result, 273.15)

  def testKtoC(self):
    """kToC should return 0 Celsius for 273.15 Kelvin"""
    result = temp_converter.kToC(273.15)
    self.assertEqual(result, 0)

  def testKtoF(self):
    """kToF should return 32 Fahrenheit for 273.15 Kelvin"""
    result = temp_converter.kToF(273.15)
    self.assertEqual(result, 32)

  # sanity checks

  # test range exceptions
  def testCtoFRange(self):
    """cToF should raise TemperatureRangeError if Celsius is less than -273.15"""
    self.assertRaises(TemperatureRangeError, temp_converter.cToF, -274)

  def testCtoKRange(self):
    """cToK should raise TemperatureRangeError if Celsius is less than -273.15"""
    self.assertRaises(TemperatureRangeError, temp_converter.cToK, -274)

  def testFtoCRange(self):
    """fToC should raise TemperatureRangeError if Fahrenheit is less than -459.67"""
    self.assertRaises(TemperatureRangeError, temp_converter.fToC, -460)

  def testFtoKRange(self):
    """fToK should raise TemperatureRangeError if Fahrenheit is less than -459.67"""
    self.assertRaises(TemperatureRangeError, temp_converter.fToK, -460)

  def testKtoCRange(self):
    """kToC should raise TemperatureRangeError if Kelvin is less than 0"""
    self.assertRaises(TemperatureRangeError, temp_converter.kToC, -1)

  def testKtoFRange(self):
    """kToF should raise TemperatureRangeError if Kelvin is less than 0"""
    self.assertRaises(TemperatureRangeError, temp_converter.kToF, -1)





unittest.main()