import requests
import json
from datetime import *
import time
from workalendar.oceania import Australia


class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self):
        """
        Constructor for the Calculator class
        Nothing is implemented here.
        """
        pass



    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state, final_state, capacity, price, is_peak, is_holiday) -> int:
        """
        This is a method takes in 6 inputs initial_state, final_state, capacity, price, is_peak and is_holiday 
        for the cost calculation of the Joules Up EV Charging Calculator.
        The method will return an integer of the calculation of the cost needed.
        """
        if is_peak:
            disc = 1
        else:
            disc = 0.5

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = (int(final_state) - int(initial_state)) / 100 * int(capacity) * ((price / 100) * disc) * surcharge_factor
        return round(cost, 2) 

    # you may add more parameters if needed, you may also modify the formula.
    #returns int in minutes
    def time_calculation(self, initial_state, final_state, capacity, power) -> int:
        """
        This is a method takes in 4 parameters initial_state, final_state, capacity, power
        for the time calculation of the Joules Up EV Charging Calculator.
        The method will return an integer in minutes of the calculation of the time.
        """
        time = (int(final_state) - int(initial_state)) / 100 * int(capacity) / power
        return round(time, 2)

    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def is_holiday(self, start_date) -> bool:
        """
        This method takes in a parameter start_date and checks if the date/day entered is a holiday, or weekday as the cost incurred will vary if its a normal day 
        or a weekday/public holiday/australia holiday.
        The method returns a boolean of True or False checking whether the start_date entered is a holiday or weekday
        """
        aus = Australia()
        dt = datetime.strptime(start_date, '%d/%m/%Y')
        year = dt.year
        month = dt.month
        day = dt.day
        # WEEKDAYS = HOLIDAYS
        flag = False
        if datetime(year, month, day).isoweekday() >= 6: # checks for weekends
            flag = False
        elif datetime(year, month, day).isoweekday() <= 5:  # checks for weekdays
            return True
        
        if flag == False: 
            for i in aus.holidays(year):
                if start_date == i[0].strftime('%d/%m/%Y'): # this has weekends and public holidays
                    return True
            return False


    def is_peak(self, start_time) -> bool:
        """
        This method takes in a parameter start_time and checks if the time inputted is a peak hour and it will
        return a boolean value of True or False as the cost will change if its a peak hour
        """
        tm = datetime.strptime(start_time, '%H:%M')
        hour = tm.hour
        if hour >= 6 and hour < 18:
            return True
        else:
            return False

    #Method that returns the power from the charger's configuration
    def power_from_configuration(self, charger_configuration) -> int:
        """
        The method takes a parameter charger_configuration and checks if the configuration is an integer of then given range which is
        between 1 and 8, the range given is the number of valid configurations or level of charger configuration and an integer of the power
        outputted by the charger configuration will be outputted. 
        """
        if int(charger_configuration) == 1:
            return 2
        elif int(charger_configuration) == 2:
            return 3.6
        elif int(charger_configuration) == 3:
            return 7.2
        elif int(charger_configuration) == 4:
            return 11
        elif int(charger_configuration) == 5:
            return 22
        elif int(charger_configuration) == 6:
            return 36
        elif int(charger_configuration) == 7:
            return 90
        elif int(charger_configuration) == 8:
            return 350

    #Method that returns the price of each level of configuration from the charger configuration
    def price_from_configuration(self, charger_configuration) -> int:
        """
        The method takes a parameter charger_configuration and checks if the configuration is an integer of then given range which is
        between 1 and 8, the range given is the number of valid configurations or level of charger configuration and an integer of the 
        price of each charger configuration.
        """
        if int(charger_configuration) == 1:
            return 5
        elif int(charger_configuration) == 2:
            return 7.5
        elif int(charger_configuration) == 3:
            return 10
        elif int(charger_configuration) == 4:
            return 12.5
        elif int(charger_configuration) == 5:
            return 15
        elif int(charger_configuration) == 6:
            return 20
        elif int(charger_configuration) == 7:
            return 30
        elif int(charger_configuration) == 8:
            return 50

    #Method to retrieve the solar insolation
    # to be acquired through API
    def get_solar_insolation(self, start_date, post_code):
        """
        The method takes in 2 parameters respectively start_date and post_code to retrieve the solar insolation through API.
        """
        x_date = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        response = requests.get('http://118.138.246.158/api/v1/location?postcode=' + str(post_code)).json()
        response2 = requests.get('http://118.138.246.158/api/v1/weather?location=' + response[0]['id'] + '&date=' + x_date).json()
        return response2['sunHours']

    #Method to retrieve the solar energy duration
    # to be acquired through API
    def get_solar_energy_duration(self, start_date, post_code): 
        """
        This method takes in 2 parameters, start_date and post_code to retrieve the solar energy duration through API
        using the daylight length and the hours between sunset and sunrise 
        """
        if float(self.get_solar_insolation(start_date,post_code)) > float(self.get_day_light_length(start_date,post_code)):
            return self.get_day_light_length(start_date,post_code)
        else:
            return self.get_solar_insolation(start_date,post_code)


    # to be acquired through API
    def get_day_light_length(self, start_date, post_code): 
        """
        This method uses two parameters, start_date and post_code to retrieve the daylight length through the API
        """
        x_date = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        response = requests.get('http://118.138.246.158/api/v1/location?postcode=' + str(post_code)).json()
        response2 = requests.get('http://118.138.246.158/api/v1/weather?location=' + response[0]['id'] + '&date=' + x_date).json()
        day_length = (datetime.strptime(response2['sunset'], ('%H:%M:%S'))) - (datetime.strptime(response2['sunrise'], ('%H:%M:%S')))
        x = str(day_length).split(":")
        int_day_length = int(x[0]) + int(x[1]) / 60  # ignoring seconds
        return str((round(int_day_length,2)))  # this returns amount of hours as a string

    # to be acquired through API
    # 0 <= cc <= 100
    def get_cloud_cover(self, start_date, start_time, post_code, hour):
        """
        This method uses 4 parameters, start_date, start_time, post_code, hour to get the cloud cover from the API
        The method returns a list of integer/float values #check check check
        """
        x_date = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        lst = []
        response = requests.get('http://118.138.246.158/api/v1/location?postcode=' + str(post_code)).json()
        response2 = requests.get('http://118.138.246.158/api/v1/weather?location=' + response[0]['id'] + '&date=' + x_date).json()
        #tm = datetime.strptime(start_time, '%H:%M')
        #end_time = tm + self.time_calculation(initial_state, final_state, capacity, power)
        for i in response2['hourlyWeatherHistory']:
            #if i['hour'] >= start_time and i['hour'] < end_time:
            lst.append(i['cloudCoverPct']) # STILL HAVE TIME TO CONSIDER (add time)

        return lst[int(hour) -1]

    # assuming that the date will be in this form "01/08/2021"
    def get_two_reference_date(self, start_date):
        """
        The purpose of this method is to get two reference dates from the date given, 
        the method will return two reference dates in the form of a list 
        """
        reference_year1 = str(int(start_date.split("/")[2])  -1)
        reference_year2 = str(int(start_date.split("/")[2])  -2)
        
        month = start_date.split("/")[1]
        day = start_date.split("/")[0]

        #if the current date is 29th of February
        if int(month) == 2 and int(day) > 28:
            reference_date1 = str(int(day) -1) + "/" + month + "/" + reference_year1
            reference_date2 = str(int(day) -1) + "/" + month + "/" + reference_year2

        else:
            reference_date1 = day + "/" + month + "/" + reference_year1
            reference_date2 = day + "/" + month + "/" + reference_year2

        return [reference_date1, reference_date2]  #two reference date in a list, Example: ['11/09/2020', '11/09/2019']
    
    def get_end_time(self, initial_state, final_state, capacity, power, start_time):
        """
        This method i uses 5 parameters, initial_state, final_state, capacity, power, start_time to get the 
        end time of the charging duration
        """
        hours = 0
        minutes = float(self.time_calculation(initial_state, final_state, capacity, power))
        seconds = 0

        if type(minutes) is float:  
            seconds = int(round(minutes%1, 2) * 60)
            minutes = int(minutes)

        the_time = start_time.split(":")
        end_hours = int(the_time[0]) + hours
        end_minutes = int(the_time[1]) + minutes
        end_seconds = int(the_time[2]) + seconds

        if end_minutes >= 60:
            end_hours += (end_minutes//60)
            end_minutes = end_minutes%60


        if int(end_hours) == 0:
            end_hours = "00"
        elif int(end_hours) < 10:
            end_hours = "0" + str(end_hours)

        if int(end_minutes) == 0:
            end_minutes = "00"
        elif int(end_minutes) < 10:
            end_minutes = "0" + str(end_minutes)

        if int(end_seconds) == 0:
            end_seconds = "00"
        elif int(end_seconds) < 10:
            end_seconds = "0" + str(end_seconds)
        
        
        end_time = str(end_hours) + ":" + str(end_minutes) + ":" + str(end_seconds)

        return end_time  # Example form "17:10:00"
      

    # Amount of solar energy generated for each whole hour during daylight hours
    def calculate_hourly_solar_energy(self, start_date, start_time, post_code, hour):
        """
        This method is created to calculate the hourly solar energy with the parameters start_date, start_time, post_code, hour.
        The method will perform the calculation of hourly solar energy based on the formula given.
        """
        si = float(self.get_solar_insolation(start_date,post_code))
        dl = float(self.get_day_light_length(start_date,post_code))
        cc = int(self.get_cloud_cover(start_date, start_time, post_code, hour))
       
        return round(si * 1/ dl* (1-cc/100) * 50 * 0.20, 4) #rounding it to 4 decimal places

    # ALG1 2.f.
    def record_solar_energy(self, start_date, start_time,initial_state, final_state, capacity, power, post_code):
        """
        This method records the solar energy with the parameters start_date, start_time, initial_state, final_state, capacity, power, post_code
        """
        lst = []
        initial_start_time = start_time #10:22:00
        end_time = self.get_end_time(initial_state, final_state, capacity, power, start_time) #10:24:30

        #First for loop for the current date
        no_hour = 1 + int(end_time.split(":")[0]) - int(start_time.split(":")[0])
        for _ in range(no_hour):
            hour = int(start_time.split(":")[0])
            se = self.calculate_hourly_solar_energy(start_date, start_time, post_code, hour)
            lst.append((start_date, hour, se)) #[('11/09/2021', 10, 1.3714)]
            start_time = str(int(start_time.split(":")[0]) + 1) + ":" + str(start_time.split(":")[1])
        
        #This is the loop for the reference dates
        reference_lst = self.get_two_reference_date(start_date)
        for i in range(len(reference_lst)):
            start_date = reference_lst[i]
            start_time = initial_start_time
            for _ in range(no_hour):
                hour = int(start_time.split(":")[0])
                se = self.calculate_hourly_solar_energy(start_date, start_time, post_code, hour)
                lst.append((start_date, hour, se))
                start_time = str(int(start_time.split(":")[0]) + 1) + ":" + str(start_time.split(":")[1])

        #Example lst contains [('11/09/2021', 10, 1.3714), ('11/09/2020', 10, 1.4311), ('11/09/2019', 10, 4.0798)]

if __name__ == "__main__":
    calc = Calculator()
    #Manual test cases
    #calc.get_two_reference_date("15/09/2021")
    #calc.get_end_time("10", "100", "90", 36, "10:22:00")
    #calc.get_end_time("0", "100", "100", 350, "00:00:00")
    
    #calc.get_solar_insolation("11/09/2021", "3800")
    #calc.get_cloud_cover("28/09/2021", "10:22:00", "2000", 17)
    #calc.get_day_light_length("11/09/2021", "4008")

    #calc.calculate_hourly_solar_energy("28/09/2021", "10:22:00", "3800", 20)

    #record_solar_energy(self, start_date, start_time, initial_state, final_state, capacity, power, post_code)
    #calc.record_solar_energy("11/09/2021", "10:22:00", "10", "100", "100", 36, "3800")
    #calc.cost_calculation("10", "100", "100", 30, False, False)
    #calc.time_calculation("5","30","100",1)

    