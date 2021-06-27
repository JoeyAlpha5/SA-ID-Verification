import time as time
from datetime import date

"""
South Africa ID Format
+-------------------------+
|9|8|0|1|0|9|0|5|1|3|0|8|5|
+-------------------------+
|Y|Y|M|M|D|D|S|S|S|S|C|A|Z|
+-------------------------+
"""

# Initialize constants variables to determine users' gender
CONST_FEMALE_LOWER_BOUND = 0000
CONST_FEMALE_UPPER_BOUND = 4999
CONST_MALE_LOWER_BOUND = 5000
CONST_MALE_UPPER_BOUND = 9999

# initializeconstants to classify citizenship
CONST_SA_CITIZEN = 0
CONST_PERM_RESIDENT = 1

class SouthAfricanID(object):
    """
    This is a blueprint for the South African identity verification.
    """

    def __init__(self,input_id):
        self.input_id = input_id
        # extract years, month and date from the valid id
        self.year = self.input_id[:len(self.input_id) - 11]
        self.month = self.input_id[len(self.input_id) - 11:len(self.input_id) - 9]
        self.day = self.input_id[len(self.input_id) - 9:len(self.input_id) - 7]

    def validate_id(self):
        """
        This function gets an id number from the user and store it in an array.
        :returns: a list containing an ID number
        """

        # get the last value of an id number
        Z = self.input_id[-1]

        # get the valid value of an id
        valid_checksum_Z = self.get_checksum()
    
        if int(Z) == valid_checksum_Z:
            return True
        else:
            return False


    def get_date_of_birth(self):
        """
        This function extracts date of birth from the id number in this format YYYY, MM and DD
        :returns: the date of birth in YYYY/MM/YY format.
        """
        # check if the user was born before 2000 
        if self.year.startswith("0"):
            self.year = "20{}".format(self.year)
        else:
            self.year = "19{}".format(self.year)

        # set the date of birth in YYYY/MM/DD format
        dob = "{}-{}-{}".format(self.year, self.month, self.day)

        return dob

    def get_age(self):
        """
        This function gets the user age
        :returns: age
        """
        # borrowed from https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/
        todays_date = date.today()

        #get the current month
        month = todays_date.month

        # get the day 
        day = todays_date.day
       

        if month >= int(self.month) and day >= int(self.day):
           return todays_date.year - int(self.year)  
        else:
           return (todays_date.year - int(self.year)) - 1

    def get_gender(self):
        """
        This function gets applicants gender: Male or Female
        :returns: gender -> female or male
        """
       
        # extracts the SSSS digits from the id to determine if the user is female or male
        SSSS = int(self.input_id[len(self.input_id) - 7:len(self.input_id) - 3])

        if SSSS >= CONST_FEMALE_LOWER_BOUND and SSSS <= CONST_FEMALE_UPPER_BOUND:
            return "Female"
        elif SSSS >= CONST_MALE_LOWER_BOUND and CONST_MALE_UPPER_BOUND:
            return "Male"

    def get_citizenship(self):
        """
        This function gets applicants citizenship: South African :0 or Permanant Resident : 1
        """

        C = int(self.input_id[len(self.input_id)-3])
        if  C == CONST_SA_CITIZEN:
            return "SA Citizen"
        elif C == CONST_PERM_RESIDENT:
            return "Permanent Resident"

    # following Luhn Algorithm pseudocode from https://en.wikipedia.org/wiki/Luhn_algorithm
    def get_checksum(self):
        """
        This funcion validates the RSA id number
        The objective is to vaidate the last digit number from the id number
        """
        try:
            # get the length of the number of digits from an input RSA id number.
            nDigits = int(len(self.input_id))
            if nDigits != 13:
                raise ValueError
            else:
               
                # set a variable
                sum = 0
                parity = nDigits % 2
                # iterate through the id number to compute the sum   
                for index in range(0,nDigits - 1):
                    
                    # get all digits along with their indexes except the last digit
                    digit = int(self.input_id[index])

                    # double every second second digit
                    if index % 2 == parity:
                        digit = digit * 2
                    
                    # substract a 9 to all values greater than 10
                    if digit > 9:
                        digit = digit - 9
                        
                    # compute the sum of all digits
                    sum += digit
                
                # multiply the sum by 9
                acc_sum = sum * 9

                # compute the checksum digit()
                Z = acc_sum % 10

                return Z
            
        except ValueError:
            print("ID Number is NOT valid.")


# get the South African ID verification script
id_number =  SouthAfricanID("0123456789012")

# validates the users input ID
if id_number.validate_id():
    date_of_birth = id_number.get_date_of_birth()
    age = id_number.get_age()
    gender = id_number.get_gender()
    citizenship = id_number.get_citizenship()
    print("Born: ",date_of_birth)
    print("Age: ",age)
    print("Gender: ",gender)
    print("Citizenship: ",citizenship)
else:
    print("ID Number is NOT valid.")
