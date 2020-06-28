# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import UserUtteranceReverted
import requests,re
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset,Restarted
import os
import smtplib
import imghdr
from email.message import EmailMessage

class email:
    email_id = ""
    password = ""
    sender_email_id = ""
    person_name = ""
    type_loan = ""
    phone_number = ""


    def __init__(self,email_id,password,sender_email_id,person_name,type_loan,phone_number):
        self.email_id = email_id
        self.password = password
        self.sender_email_id = sender_email_id
        self.type_loan = type_loan
        self.phone_number = phone_number
        self.person_name = person_name

    def sendmail(self):
        EMAIL_ADDRESS = self.email_id 
        EMAIL_PASSWORD = self.password

        #contacts = ['YourAddress@gmail.com']

        msg = EmailMessage()
        msg['Subject'] = 'Your deatils'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = self.sender_email_id

        msg.set_content('')

        htmlfile =""" \
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="stylesheet" type="text/css" href="/home/harshith/Desktop/mail/style.css">
        </head>
        <body>
        <p>This is the mail reagrding lates enquirey with the our company BIgdatamatica</p>
        <h2>Coustmer Detials</h2>
        <table>
        <tr>
            <th>Person Name</th>
            <th>Email id</th>
            <th>Type Loan</th>
            <th>Phone Number</th>
        </tr>
        <tr>
            <td>{person_name:}</td>
            <td>{email_id:}</td>
            <td>{type_loan:}</td>
            <td>{phone_number:}</td>
        </tr>
        </table>
        </body>
        </html>
                """

        msg.add_alternative("/home/harshith/Desktop/mail/style.css",subtype ="css")

        htmlfile = htmlfile.format(person_name=self.person_name,email_id =self.sender_email_id,type_loan= self.type_loan,phone_number=self.phone_number )
        msg.add_alternative(htmlfile, subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("message  has been send succesfully")



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Congrats you've restarted me! 😉")

        return [AllSlotsReset()]



class loanForm(FormAction):

    def name(self):
        return "loan_form"

    @staticmethod
    def required_slots(tracker):
        return [
        "person_name",
        "email_id",
        "type_loan",
        "phone_number",
        ]

    def validate_phone_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> Dict[Text, Any]:

        #print(value)

        li = []
        if type(value)==str:
            li.append(value)
        else:
            li = value
        p2 = pattern()
        for value in li:
            if p2.search_phone_number(strign=value):
                return {"phone_number":value}
            else:
                dispatcher.utter_message(text="Thats an incorrect format please enter a valid format")
                return{"phone_number":None}


    def validate_person_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> Dict[Text, Any]:
        li = []
        if type(value)==str:
            li.append(value)
        else:
            li = value
        p3 = pattern()
        for value in li:
            if(p3.search_phone_number('^\\d+$',value)):
                return {"person_name":None}
            else:
                print("value has been sucesfully accepted")
                return {"person_name":value}

    def validate_email_id(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> Dict[Text, Any]:

        li = []
        if type(value)==str:
            li.append(value)
        else:
            if "email" in value:
                value.remove("email")
                li = value
            else:
                li=value
        print(li)
        p = pattern()
        for value in li: 
            print(value)   
            if p.email_id_search(slot_value=value):
                return {"email_id":value}
            else:
                dispatcher.utter_message(text="please enter a valid email id format xyz@xyz.com")
                return{"email_id":None}
    
    def slot_mappings(self):
        return {"person_name":[self.from_entity(entity="person_name", intent="inform"),
                               self.from_entity(entity="PERSON", intent=["inform","affirm"]),
                               self.from_entity(entity="ORG", intent="inform"),
                               self.from_entity(entity="ORG", intent="deny"),
                               self.from_text(intent="inform"),
                               self.from_text(intent="greet"),],
                "email_id":[self.from_entity(entity="email_id",intent="inform"),
                            self.from_entity(entity="email",intent="inform")]}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any], ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit")
        send = email("harshit675@gmail.com","harshitH9@!",tracker.get_slot("email_id"),tracker.get_slot("person_name"),tracker.get_slot("type_loan"),tracker.get_slot("phone_number"))
        send.sendmail()
        return []


class ActionCustom(Action):
   def name(self):
      return "action_custom"

   def run(self, dispatcher, tracker, domain):
      # send utter default response to user
      dispatcher.utter_message(template="utter_default")
      # ... other code
      return []


class loanForm2(FormAction):

    def name(self):
        return "loan_form2"

    @staticmethod
    def required_slots(tracker):
        return [
       "housing_status",
       "other_loans",
       "monthly_salary",
        ]


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any], ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit2")
        return []



class ActionRestarted(Action):
    def name(self):
        return "action_chat_restart"
    def run(self,dispatcher,tracker,domain):
        return[Restarted()]



class ActionGreetUser(Action):
    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        print("greet_block_excuted")
        return [UserUtteranceReverted()]


class pattern:
    def search_phone_number(self,pattern='^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$',strign=None):
        search1 = re.compile(pattern).search(strign)
        if not search1:
            print(False)
            return False
        else:
            print(True)
            return True 

    def email_id_search(self,pattern="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",slot_value=None):
        search1 = re.compile(pattern).search(slot_value)
        if not search1:
            print(slot_value)
            print(False)
            return False
        else:
            print(True)
            return True 