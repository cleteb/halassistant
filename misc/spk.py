#! /usr/bin/python3
"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar."""

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import pyttsx3
import dateutil.parser
import sched
import time

SCHED = sched.scheduler(time.time, time.sleep)


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
  
  run_service()
  #setup_google_gmail()
  #call_google_gmail()

"""#####################################################"""

if __name__ == "__main__":
  main()
