from datetime import datetime
from app.calculator_form import *
import unittest

#Unittesting for Calculator_Form class
class TestCalculatorForm(unittest.TestCase):
    def test_validate_BatteryPackCapacity(self):
        self.calculator_form = Calculator_Form()
        if self.calculator_form.BatteryPackCapacity is None:
            raise AssertionError("Field cannot be empty")
        elif int(self.calculator_form.BatteryPackCapacity <= 0) :
            raise ValueError("Input of battrey pack capacity cannot be lower than or equal to 0")
        elif int(self.calculator_form.BatteryPackCapacity > 100) :
            raise ValueError("Input of battrey pack capacity cannot be higher than 100")
        elif self.calculator_form.BatteryPackCapacity == "":
            raise ValueError("Invalid input of battrey pack capacity, input must be integer")
        elif self.calculator_form.BatteryPackCapacity in self.is_char:
            raise ValueError("Invalid input of battrey pack capacity, input must be integer")

    def test_validate_InitialCharge(self):
        self.calculator_form = Calculator_Form()
        if self.calculator_form.InitialCharge is None:
            raise AssertionError("Field cannot be empty")
        elif int(self.calculator_form.InitialCharge <= 0) : 
            raise ValueError("Input of initial charge cannot be lower than or equal to 0")
        elif self.calculator_form.InitialCharge == "":
            raise ValueError("Invalid input of initial charge, input must be integer")
        elif self.calculator_form.InitialCharge in self.is_char:
            raise ValueError("Invalid input of initial charge, input must be integer")

    def test_validate_FinalCharge(self):
        self.calculator_form = Calculator_Form()
        if self.calculator_form.FinalCharge is None:
            raise AssertionError("Field cannot be empty")
        elif int(self.calculator_form.InitialCharge) > int(self.calculator_form.FinalCharge):
            raise ValueError("Input of final charge cannot be lower than initial charge")
        elif int(self.calculator_form.FinalCharge <= 0) : 
            raise ValueError("Input of final charge cannot be lower than or equal to 0")
        elif self.calculator_form.FinalCharge == "":
            raise ValueError("Invalid input of final charge, input must be integer")
        elif self.calculator_form.FinalCharge in self.is_char:
            raise ValueError("Invalid input of final charge, input must be integer")

    def test_validate_StartDate(self):
        self.calculator_form = Calculator_Form()
        if self.calculator_form.StartDate is None:
            raise AssertionError("Field cannot be empty")
        elif self.calculator_form.StartDate < datetime.date(2008,7,1):
            raise ValueError("Invalid input of start date, date cannot be before 1/7/2008")

    def test_validate_StartTime(self):
        self.calculator_form = Calculator_Form()
        if self.calculator_form.StartTime is None:
            raise AssertionError("Field cannot be empty")
        elif self.calculator_form.StartTime != datetime.time():
            raise ValueError("Invalid input of start time")

    def test_validate_ChargerConfiguration(self):
        self.calculator_form = Calculator_Form()
        if self.calculator_form.ChargerConfiguration is None:
            raise AssertionError("Field cannot be empty")
        elif int(self.calculator_form.ChargerConfiguration) <= 0 and int(self.calculator_form.ChargerConfiguration > 8):
            raise ValueError("Invalid charger configuration ")
        elif self.calculator_form.ChargerConfiguration in self.is_char:
            raise ValueError("Invalid input of charger configuration, input of charger configuration must be between 1-8")

    def test_validate_PostCode(self):
        self.calculator_form = Calculator_Form()
        if self.calculator_form.Po is None:
            raise AssertionError("Field cannot be empty")
        elif int(self.calculator_form.PostCode) <= 200 and int(self.calculator_form.PostCode > 8):
            raise ValueError("Invalid post code ")
        elif self.calculator_form.PostCode in self.is_char:
            raise ValueError("Invalid input of charger configuration, input of charger configuration must be between 1-8")
    
    #Method that contains char which stores all the character, alphabets on the keybaord that is not an integer 
    def is_char(self,char):
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz!@#$%^&*()_+{}|:<>?-=[]\;',./"

