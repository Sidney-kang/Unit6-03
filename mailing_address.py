# Created by : Sidney Kang
# Created on : 4 Dec. 2017
# Created for : ICS3UR
# Daily Assignment - Unit 6-03
# This program

class MailingAddress():
      def __init__(self, last_name, first_name, unit_number, civic_number, street_name, street_type, municipality, province, postal_code):
          self.first_name = first_name
          self.last_name = last_name
          self.unit_number = unit_number
          self.civic_number = civic_number
          self.street_name = street_name          
          self.street_type = street_type
          self.municipality = municipality
          self.province = province
          self.postal_code = postal_code
          
last_name = raw_input("What is the addressee's last name? ")  
last_name = last_name.upper()
first_name = raw_input("What is the addressee's first name? ")  
first_name = first_name.upper()
unit_number = raw_input("What is their unit number? ")
unit_number = unit_number.upper()
civic_number = raw_input("What is their civic number? ")
civic_number = civic_number.upper()
street_name = raw_input("What is the name of the street? ")
street_name = street_name.upper()
street_type = raw_input("What is their street type? ")     
street_type = street_type.upper()
municipality = raw_input("Which municipality is the letter being sent to? ")
municipality = municipality.upper()
province = raw_input("Which province is the letter being sent to? ")
province = province.upper()
postal_code = raw_input("What is their postal code? ")
postal_code = postal_code.upper()

mailing_address = MailingAddress(last_name, first_name, unit_number, civic_number, street_name, street_type, municipality, province, postal_code)

print(mailing_address.first_name + ' ' + mailing_address.last_name)
print(mailing_address.unit_number + '-' + mailing_address.civic_number + ' ' + mailing_address.street_name + ' ' + mailing_address.street_type)
print(mailing_address.municipality + ' ' + mailing_address.province + ' ' + mailing_address.postal_code)          
