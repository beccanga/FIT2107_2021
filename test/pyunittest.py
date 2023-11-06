from app.calculator import *
import unittest

#Unittesting for Calculator class
class TestCalculator(unittest.TestCase):

    #Unit testing for cost calulcation
    # initial, final, capacity, price, is_peak, is_holiday
    def test_cost(self): 
        """
        The purpose of this tester method is to check for the validity of the cost_calculation(0) method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method. The tester also checks for the validity of the inputs of
        the parameters from the file's method. If the test cases are unable to pass, an error message will be printed
        """
        self.calculator = Calculator()
        self.assertEqual(self.calculator.cost_calculation("10", "50", "100", 5, True, False),2.0, msg = "Incorrect calculation of cost") 
        self.assertEqual(self.calculator.cost_calculation("10", "10", "100", 20, True, True),0.0, msg = "Incorrect calculation of cost") 
        self.assertEqual(self.calculator.cost_calculation("10", "100", "100", 20, True, True),19.8, msg = "Incorrect calculation of cost") 
        self.assertEqual(self.calculator.cost_calculation("10", "100", "100", 30, False, False),13.5, msg = "Incorrect calculation of cost") 

    #Unit testing for time calculation 
    #initial, final, capacity, power
    def test_time_calculation(self): #TODO
        """
        The purpose of this tester method is to check for the validity of the time_calculation() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method. The tester also checks for the validity of the inputs of
        the parameters from the file's method. If the test cases are unable to pass, an error message will be printed
        """
        self.calculator = Calculator()
        
        self.assertEqual(self.calculator.time_calculation("10","100","100",3),30.0,msg= "Incorrect calculation for time") 
        self.assertEqual(self.calculator.time_calculation("0","100","100",8),12.5,msg= "Incorrect calculation for time") 
        self.assertEqual(self.calculator.time_calculation("5","30","100",1),25.0,msg= "Incorrect calculation for time") 
        

    #Unit testing for holiday
    def test_is_holiday(self):
        """
        The purpose of this tester method is to check for the validity of the is_holiday() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method. Which is to check if the parameter passed in is infact a holiday or
        a week day as this parameter affects the cost calculation. If the test cases are unable to pass, an error message will be printed
        """
        self.calculator = Calculator()

        #Checking for holidays
        self.assertEqual(self.calculator.is_holiday("30/12/2021"),True, msg = "This date is not a holiday") #New Years eve
        self.assertEqual(self.calculator.is_holiday("1/1/2021"), True, msg = "This date is not a holiday") #New Years
        self.assertEqual(self.calculator.is_holiday("2/4/2021"),True, msg = "This date is not a holiday") #Good Friday 
        self.assertEqual(self.calculator.is_holiday("24/12/2021"),True,msg= "This date is not a holiday") #Christmas eve day (Regional Holiday)
        self.assertEqual(self.calculator.is_holiday("25/12/2021"),True, msg = "This date is not a holiday") #Christmas day
        self.assertEqual(self.calculator.is_holiday("26/12/2021"),True, msg = "This date is not a holiday") #Boxing day
        self.assertEqual(self.calculator.is_holiday("27/12/2021"),True, msg = "This date is not a holiday") #Christmas day (Public Holiday)
        self.assertEqual(self.calculator.is_holiday("25/1/2021"),True,msg = "This date is not a holiday") #the day before Australia Independence day
        self.assertEqual(self.calculator.is_holiday("26/1/2021"),True, msg = "This date is not a holiday") #Australia Independence day
        
        #Random weekdays for testing
        self.assertEqual(self.calculator.is_holiday("29/9/2021"), True, msg = "This date is not a holiday") #Wednesday in September
        self.assertEqual(self.calculator.is_holiday("16/7/2021"), True, msg = "This date is not a holiday") #Friday in July
        self.assertEqual(self.calculator.is_holiday("18/9/2021"), False, msg = "This date is not a holiday") #Saturday in September
        self.assertEqual(self.calculator.is_holiday("19/9/2021"), False, msg = "This date is not a holiday") #Sunday in September


    #Unit testing for is_peak method
    #peak period is 6am - 6pm according to the requirements
    def test_is_peak(self):
        """
        The purpose of this tester method is to check for the validity of the is_peak() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method. Which is to check if the parameter passed in is infact a peak hour
        or not a peak hour which is 6am - 6pm according to the requirements, as this parameter affects the cost calculation. 
        If the test cases are unable to pass, an error message will be printed.
        """
        self.calculator = Calculator()
        self.assertEqual(self.calculator.is_peak("6:00"),True, msg = "Not peak period")
        self.assertEqual(self.calculator.is_peak("15:00"), True, msg = "Not peak period") 
        self.assertEqual(self.calculator.is_peak("3:00"), False, msg = "Not peak period") #3 am - False
        self.assertEqual(self.calculator.is_peak("19:00"), False, msg = "Not peak period") # 7 pm - False
        self.assertEqual(self.calculator.is_peak("5:59"), False, msg = "Not peak period") #5:59 am - False
        self.assertEqual(self.calculator.is_peak("18:01"), False, msg = "Not peak period") # 6:01 pm - False

    
    #Unit testing for power from configuration method
    def test_power_from_configuration(self):
        """
        The purpose of this tester method is to check for the validity of the power_from_configuration() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method. Which is to check if the input parameter of charger_configuration
        is accurate and the power returned after validating the level of charger configuration as the power affects the time calculation. 
        If the test cases are unable to pass, an error message will be printed.
        """
        self.calculator = Calculator()
        #Checking for false inputs
        self.assertEqual(self.calculator.power_from_configuration(int(0)),None,msg= "Invalid charger configuration")
        self.assertEqual(self.calculator.power_from_configuration(int(9)),None,msg= "Invalid charger configuration")
        
        #True values
        self.assertEqual(self.calculator.power_from_configuration(int(1)),2,msg= "Invalid power from configuration")
        self.assertEqual(self.calculator.power_from_configuration(int(2)),3.6,msg= "Invalid power from configuration")
        self.assertEqual(self.calculator.power_from_configuration(int(3)),7.2,msg= "Invalid charger configuration")
        self.assertEqual(self.calculator.power_from_configuration(int(4)),11,msg= "Invalid power from configuration")
        self.assertEqual(self.calculator.power_from_configuration(int(5)),22,msg= "Invalid power from configuration")
        self.assertEqual(self.calculator.power_from_configuration(int(6)),36,msg= "Invalid power from configuration")
        self.assertEqual(self.calculator.power_from_configuration(int(7)),90,msg= "Invalid power from configuration")
        self.assertEqual(self.calculator.power_from_configuration(int(8)),350,msg= "Invalid charger configuration")
  
    
    #Unit testing for price_from_configuration() method
    def test_price_from_configuration(self):
        """
        The purpose of this tester method is to check for the validity of the price_from_configuration() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method. Which is to check if the input parameter of charger_configuration
        is accurately within the boundary and the price returned after validating the level of charger configuration is accurate and an integer or float
        as the price affects the time calculation. 
        If the test cases are unable to pass, an error message will be printed.
        """
        self.calculator = Calculator()
        #Checking for false inputs
        self.assertEqual(self.calculator.price_from_configuration(int(0)),None,msg= "Invalid charger configuration")
        self.assertEqual(self.calculator.price_from_configuration(int(9)),None,msg= "Invalid charger configuration")
        
        #True values
        #Checking for correct configuration values
        self.assertEqual(self.calculator.price_from_configuration(int(1)),5,msg= "Invalid price from configuration")
        self.assertEqual(self.calculator.price_from_configuration(int(2)),7.5,msg= "Invalid charger configuration")
        self.assertEqual(self.calculator.price_from_configuration(int(3)),10,msg= "Invalid price from configuration")
        self.assertEqual(self.calculator.price_from_configuration(int(4)),12.5,msg= "Invalid price from configuration")
        self.assertEqual(self.calculator.price_from_configuration(int(5)),15,msg= "Invalid charger configuration")
        self.assertEqual(self.calculator.price_from_configuration(int(6)),20,msg= "Invalid charger configuration")
        self.assertEqual(self.calculator.price_from_configuration(int(7)),30,msg= "Invalid charger configuration")
        self.assertEqual(self.calculator.price_from_configuration(int(8)),50,msg= "Invalid price from configuration")
    
    #Unit testing for get_solar_insolation() method
    def test_get_solar_insolation(self): 
        """
        The purpose of this tester method is to check for the validity of the get_solar_insolation() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method which is to get the solar insolation hrough the API provided.
        The tester method will validate the input of the parameter, start_date, and post_code of the get_solar_insolation() method and validates the input to check if the test cases provided to prove the 
        method get_solar_insolation() is able to run and return the sun hours (solar insolation). If the test cases are unable to pass, an error message will be printed.
        """
        self.calculator = Calculator()

        #Invalid solar insolation 
        #Different post_codes for each (different)date 
        self.assertEqual(self.calculator.get_solar_insolation("11/09/2021", "3800"),1.6,msg = "Solar insolation is not valid")
        self.assertEqual(self.calculator.get_solar_insolation("11/09/2021", "2000"),5.3,msg = "Solar insolation is not valid")
        self.assertEqual(self.calculator.get_solar_insolation("11/09/2021", "4008"),5.9,msg = "Solar insolation is not valid")

        self.assertEqual(self.calculator.get_solar_insolation("13/09/2021", "3800"),4.9,msg = "Solar insolation is not valid")
        self.assertEqual(self.calculator.get_solar_insolation("13/09/2021", "2000"),3.1,msg = "Solar insolation is not valid")
        self.assertEqual(self.calculator.get_solar_insolation("13/09/2021", "4008"),5.2,msg = "Solar insolation is not valid")

        self.assertEqual(self.calculator.get_solar_insolation("28/09/2021", "3800"),5.2,msg = "Solar insolation is not valid")
        self.assertEqual(self.calculator.get_solar_insolation("28/09/2021", "2000"),5.5,msg = "Solar insolation is not valid")
        self.assertEqual(self.calculator.get_solar_insolation("28/09/2021", "4008"),4.3,msg = "Solar insolation is not valid")

        self.assertEqual(self.calculator.get_solar_insolation("8/9/2021", "3800"),4.8,msg = "Solar insolation is not valid")
        self.assertEqual(self.calculator.get_solar_insolation("8/9/2021", "2000"),5.2,msg = "Solar insolation is not valid")
        self.assertEqual(self.calculator.get_solar_insolation("8/9/2021", "4008"),5.8,msg = "Solar insolation is not valid")
        

    def test_get_solar_energy_duration(self): 
        """
        The purpose of this tester method is to check for the validity of the get_solar_energy_duration() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method which is to get the solar energy duration through the API provided.
        The tester method will validate the input of the parameter's of the get_solar_energy_duration() method which is the start_date and the post_code 
        and validate if the test cases provided to prove the method get_solar_energy_duration() is able to run. 
        If the test cases are unable to pass, an error message will be printed.
        """
        self.calculator = Calculator()
        self.assertEqual(self.calculator.get_solar_energy_duration("11/09/2021","3800"),1.6,msg = "Solar energy duration is not valid")
        self.assertEqual(self.calculator.get_solar_energy_duration("08/09/2021", "3800"),4.8,msg = "Solar energy duration is not valid")
        self.assertEqual(self.calculator.get_solar_energy_duration("03/08/2021", "5000"),3.5,msg = "Solar energy duration is not valid")
        self.assertEqual(self.calculator.get_solar_energy_duration("06/06/2021", "3000"),1.6,msg = "Solar energy duration is not valid")

    def test_get_day_light_length(self): 
        """
        The purpose of this tester method is to check for the validity of the get_day_light_length() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method which is to get the daylight length through the API provided.
        The tester method will validate the input of the parameter's of the get_day_light_length() method which is the start_date and the post_code and validate if the test cases provided to prove the 
        method get_day_light_length() is able to run. If the test cases are unable to pass, an error message will be printed.
        """
        self.calculator = Calculator()
        #True values
        self.assertEqual(self.calculator.get_day_light_length("11/09/2021", "3800"),"11.67",msg = "Incorrect day light length")
        self.assertEqual(self.calculator.get_day_light_length("13/09/2021", "3800"),"11.75",msg = "Incorrect day light length")
        self.assertEqual(self.calculator.get_day_light_length("28/09/2021", "3800"),"12.35",msg = "Incorrect day light length")

        self.assertEqual(self.calculator.get_day_light_length("11/09/2021", "2000"),"11.73",msg = "Incorrect day light length")
        self.assertEqual(self.calculator.get_day_light_length("13/09/2021", "2000"),"11.8",msg = "Incorrect day light length")
        self.assertEqual(self.calculator.get_day_light_length("28/09/2021", "2000"),"12.32",msg = "Incorrect day light length")

        self.assertEqual(self.calculator.get_day_light_length("11/09/2021", "4008"),"11.82",msg = "Incorrect day light length")
        self.assertEqual(self.calculator.get_day_light_length("13/09/2021", "4008"),"11.87",msg = "Incorrect day light length")
        self.assertEqual(self.calculator.get_day_light_length("28/09/2021", "4008"),"12.27",msg = "Incorrect day light length")


    def test_get_cloud_cover(self): 
        """
        The purpose of this tester method is to check for the validity of the get_cloud_cover() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method which is to get the cloud cover pct through the API provided through the start date and the start time.
        The tester method will validate the input of the parameter's of the get_cloud_cover() method which is the start_date and the start_time and validate if the test cases provided to prove the 
        method get_cloud_cover() is able to run. If the test cases are unable to pass, an error message will be printed.
        """
        self.calculator = Calculator()
        #Changes in start date, while other parameters stay the same
        self.assertEqual(self.calculator.get_cloud_cover("11/09/2021","10:22","3800",17),90,msg = "Incorrect cloud cover pct ") 
        # self.assertEqual(self.calculator.get_cloud_cover("13/09/2021","10:22","3800",17),52,msg = "Incorrect cloud cover pct ")
        self.assertEqual(self.calculator.get_cloud_cover("28/09/2021","10:22","3800",17),16,msg = "Incorrect cloud cover pct ")

        #Changes in hour, with the same start dates as previous tests, while other parameters stay the same
        self.assertEqual(self.calculator.get_cloud_cover("11/09/2021","10:22","3800",20),78,msg = "Incorrect cloud cover pct ") 
        self.assertEqual(self.calculator.get_cloud_cover("28/09/2021","10:22","3800",20),20,msg = "Incorrect cloud cover pct ")

        #Changes in start time, with the same dates as previous tests, while other parameters stay the same
        self.assertEqual(self.calculator.get_cloud_cover("11/09/2021","6:22","3800",20),78,msg = "Incorrect cloud cover pct ") 
        self.assertEqual(self.calculator.get_cloud_cover("28/09/2021","6:22","3800",20),20,msg = "Incorrect cloud cover pct ")

        #Changes in post code, with the same start dates , start time, hour as previous tests, while other parameters stay the same 
        self.assertEqual(self.calculator.get_cloud_cover("13/09/2021","10:22","2000",20),67,msg = "Incorrect cloud cover pct ")
        self.assertEqual(self.calculator.get_cloud_cover("28/09/2021","10:22","2000",20),46,msg = "Incorrect cloud cover pct ")
   

    def test_get_two_reference_date(self): 
        """
        The purpose of this tester method is to check for the validity of the get_two_reference_date() method. To test if the method is able to identify reference
        date in the most immediate past which means checking the validity of the exact date in the past. If the reference dates for the start_date are incorrect, an
        error message will be printed.
        """
        self.calculator = Calculator()
        self.assertEqual(self.calculator.get_two_reference_date("11/09/2021"), ['11/09/2020', '11/09/2019'], msg = "Incorrect reference dates")
        self.assertEqual(self.calculator.get_two_reference_date("15/09/2021"), ['15/09/2020', '15/09/2019'], msg = "Incorrect reference dates")
        self.assertEqual(self.calculator.get_two_reference_date("29/02/2020"), ['28/02/2019', '28/02/2018'], msg = "Incorrect reference dates")

    def test_get_end_time(self):
        """
        The purpose of this tester method is to check for the validity of the get_end_time() method. The tester test if the format of the output end time are valid
        or not and if it obtains the expected end time. If the end time retrieved is incorrect, an error message will be printed.
        """
        self.calculator = Calculator()
        self.assertEqual(self.calculator.get_end_time("10", "100", "90", 36, "10:22:00"),"10:24:15",msg = "Incorrect end time retrieved")
        self.assertEqual(self.calculator.get_end_time("0", "100", "99", 2, "08:11:00"),"09:00:30",msg = "Incorrect end time retrieved")
        self.assertEqual(self.calculator.get_end_time("0", "100", "100", 2, "00:00:00"),"00:50:00",msg = "Incorrect end time retrieved")
        self.assertEqual(self.calculator.get_end_time("0", "100", "100", 350, "00:00:17"),"00:00:34",msg = "Incorrect end time retrieved")
    
    def test_calculate_hourly_solar_energy(self): 
        """
        The purpose of this tester method is to check for the validity of the get_calculate_hourly_solar_energy() method in the calculator.py's Calculator method
        is able to meet its purpose and fulfill the requirements of the method which is to calculate the solar energy through the formula provided.
        The tester method will validate the input of the parameter's of the calculate_hourly_solar_energy() method which is the start_date and the start_time and 
        validate if the test cases provided to prove the method calculate_hourly_solar_energy() is able to run. 
        If the test cases are unable to pass, an error message will be printed.
        """
        self.calculator = Calculator()
        #Change in start_date
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("11/09/2021", "10:22:00", "3800", 17),0.1371, msg = "Incorrect hourly solar energy calculation")
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("13/09/2021", "10:22:00", "3800", 17),2.0017, msg = "Incorrect hourly solar energy calculation")
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("28/09/2021", "10:22:00", "3800", 17),3.5368, msg = "Incorrect hourly solar energy calculation")

        #Change in start_time
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("11/09/2021", "15:22:00", "3800", 17),0.1371, msg = "Incorrect hourly solar energy calculation")
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("28/09/2021", "15:22:00", "3800", 17),3.5368, msg = "Incorrect hourly solar energy calculation")

        #Change in post_code  
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("11/09/2021", "10:22:00", "2000", 17),4.5183, msg = "Incorrect hourly solar energy calculation")
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("13/09/2021", "10:22:00", "2000", 17),1.6551, msg = "Incorrect hourly solar energy calculation")
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("28/09/2021", "10:22:00", "2000", 17),2.5, msg = "Incorrect hourly solar energy calculation")

        #Change in hour
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("11/09/2021", "10:22:00", "3800", 20),0.3016, msg = "Incorrect hourly solar energy calculation")
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("13/09/2021", "10:22:00", "3800", 20),4.0451, msg = "Incorrect hourly solar energy calculation")
        self.assertEqual(self.calculator.calculate_hourly_solar_energy("28/09/2021", "10:22:00", "3800", 20),3.3684, msg = "Incorrect hourly solar energy calculation")


    
    def test_record_solar_energy(self): #TODO
        """
        The purpose of this tester method is to check for the validity of the record_solar_energy() method. The tester will test if the method is able to run successfully
        with the correct inputs. An error message will be printed, if the method doesn't run successfully.
        """
        self.calculator = Calculator()
        self.assertEqual(self.calculator.record_solar_energy("03/08/2021", "00:22:00", "0", "100", "100", 2, "3800"), None,
        msg = "Incorrect record of solar energy")

