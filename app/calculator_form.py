from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError, Optional
import datetime

# validation for form inputs
class Calculator_Form(FlaskForm):
    # this variable name needs to match with the input attribute name in the html file
    # you are NOT ALLOWED to change the field type, however, you can add more built-in validators and custom messages
    BatteryPackCapacity = StringField("Battery Pack Capacity", [DataRequired()])
    InitialCharge = StringField("Initial Charge", [DataRequired()])
    FinalCharge = StringField("Final Charge", [DataRequired()])
    StartDate = DateField("Start Date", [DataRequired("Data is missing or format is incorrect")], format='%d/%m/%Y')
    StartTime = TimeField("Start Time", [DataRequired("Data is missing or format is incorrect")], format='%H:%M')
    ChargerConfiguration = StringField("Charger Configuration", [DataRequired()])
    PostCode = StringField("Post Code", [DataRequired()])

    # use validate_ + field_name to activate the flask-wtforms built-in validator
    # this is an example for you
    def validate_BatteryPackCapacity(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("Cannot fetch data")
        elif field.data.lstrip('-').isdigit() == False:
            raise ValueError("Input cannot be string")
        elif int(field.data) < 0:
            raise ValueError("BatteryPackCapacity cannot be less than 0")

    # validate initial charge here
    def validate_InitialCharge(self, field):
        # another example of how to compare initial charge with final charge
        # you may modify this part of the code
        if int(field.data) > int(self.FinalCharge.data):
            raise ValueError("Initial charge data error")
        elif field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("Cannot fetch data")
        elif field.data.lstrip('-').isdigit() == False:
            raise ValueError("Input cannot be string")
        elif int(field.data) < 0:
            raise ValueError("Initial charge should not be less than 0")
        

    # validate final charge here
    def validate_FinalCharge(self, field):
        if int(field.data) < int(self.InitialCharge.data):
            raise ValueError("Final charge data error")
        elif field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("Cannot fetch data")
        elif field.data.lstrip('-').isdigit() == False:
            raise ValueError("Input cannot be string")
        elif int(field.data) < 0:
            raise ValueError("Final charge should not be less than 0")

    # validate start date here
    def validate_StartDate(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("Cannot fetch data")
        # start from 1st July 2008
        elif field.data < datetime.date(2008, 7, 1):
            raise ValueError("Date must be after 1/7/2008")

    # validate start time here
    def validate_StartTime(self, field):
        if field.date is None:
            raise ValidationError('Field data is None')

    # validate charger configuration here
    def validate_ChargerConfiguration(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("Cannot fetch data")
        elif int(field.data) < 1 or int(field.data) > 8:
            raise ValueError("Charger configuration must be between 1 to 8")

    # validate postcode here
    def validate_PostCode(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")
        elif field.data.lstrip('-').isdigit() == False:
            raise ValueError("cannot fetch data (input cannot be string)")
        elif int(field.data) < 200 and int(field.data) > 9999:
            raise ValueError("cannot fetch data (must be between 0200 - 9999)")
