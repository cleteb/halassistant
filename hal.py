#! /usr/bin/python2.7
from __future__ import print_function
import datetime
import pyttsx3
import dateutil.parser
import sched
import time
import hal_mail.hal_mail
import hal_calendar.hal_calendar
"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar."""
"""#####################################################"""

#SCHED = sched.scheduler(time.time, time.sleep)

"""#####################################################"""
def speak_the_string(str_say):
    """ Use the string param to send to the py ttsx engine """
    engine = pyttsx3.init()
    engine.say(str_say)
    engine.runAndWait()

def run_service():

    """ Run the main service the create a timer 
  and calls the google api """
    SCHED.enter(20, 1, calendar_loop, (SCHED,))
    SCHED.run()


"""#####################################################"""

"""#####################################################"""
def main():

    """ Define a main() function runs everything """
    #run_service()
    hal_mail.hal_mail.setup_google_gmail()

"""#####################################################"""
"""#####################################################"""

if __name__ == "__main__":
    main()