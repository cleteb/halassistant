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
Main application that calls email and calendar events and 
speaks them out loud."""
"""#####################################################"""

#SCHED = sched.scheduler(time.time, time.sleep)
class Hal():
    
    def __init__(self):
        SCHED = sched.scheduler(time.time, time.sleep)
        
    """#####################################################"""
    def speak_the_string(str_say):
        """ Use the string param to send to the py ttsx engine """
        engine = pyttsx3.init()
        engine.say(str_say)
        engine.runAndWait()

    def run_calendar():
        """ Run the main service the create a timer 
        and calls the google api """
        SCHED.enter(20, 1, hal_calendar.hal_calendar.calendar_loop, (SCHED,))
        SCHED.run()


"""#####################################################"""

"""#####################################################"""
def main():

    """ Define a main() function runs everything """
    my_hal = Hal()
    #run_calendar()
    #hal_mail.hal_mail.get_google_calendar()
    my_hal_mail = hal_mail.hal_mail.Hal_Mail()
    my_hal_mail.get_google_gmail()    

"""#####################################################"""
"""#####################################################"""

if __name__ == "__main__":
    main()