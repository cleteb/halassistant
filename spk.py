#! /usr/bin/python3
"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar."""

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import pyttsx
import dateutil.parser
import sched
import time

SCHED = sched.scheduler(time.time, time.sleep)

def setup_google_calendar():
  """ Setup the Calendar API """
  scopes = 'https://www.googleapis.com/auth/calendar.readonly'
  store = file.Storage('credentials.json')
  creds = store.get()
  if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', scopes)
    creds = tools.run_flow(flow, store)
  service = build('calendar', 'v3', http=creds.authorize(Http()))
  return service

def call_google_calendar(svr):
  """ Call the Calendar API """
  now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
  print('Getting the upcoming 1 event')
  events_result = svr.events().list(calendarId='primary', timeMin=now,
                                    maxResults=2, singleEvents=True,
                                    orderBy='startTime').execute()
  return events_result

def speak_the_string(str_say):
  """ Use the string param to send to the py ttsx engine """
  engine = pyttsx.init()
  engine.say(str_say)
  engine.runAndWait()

def run_service():
  """ Run the main service the create a timer 
  and calls the google api """
  SCHED.enter(120, 1, calendar_loop, (SCHED,))
  SCHED.run()


def calendar_loop(sc):

  # Setup the Calendar API and get the service object
  svr = setup_google_calendar()

  # Call the Calendar API and get the event results list
  evts_rslt = call_google_calendar(svr)

  events = evts_rslt.get('items', [])

  if not events:
    print('No upcoming events found.')
  for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    #print(dateutil.parser.parse('2008-09-03T20:56:35.450686Z'))
    #print(dateutil.parser.parse(start).date().strftime("%A"))
    #print(start)
    str_say = "You have an appointment on"
    str_say = str_say + " " + dateutil.parser.parse(start).strftime("%A") +","
    str_say = str_say + " " + dateutil.parser.parse(start).strftime("%B")
    str_say = str_say + " " + dateutil.parser.parse(start).strftime("%d")
    str_say = str_say + ", at " + event['summary']
    #print("You have an appointment on")
    #print(dateutil.parser.parse(start).strftime("%A"))
    #print(dateutil.parser.parse(start).strftime("%B"))
    #print(dateutil.parser.parse(start).strftime("%d"))
    #print("@ " + event['summary'])
    print(str_say)
    speak_the_string(str_say)

  SCHED.enter(120, 1, calendar_loop, (sc,))
  
"""#####################################################"""
def setup_google_gmail():
  # Setup the Gmail API
  SCOPESMAIL = 'https://www.googleapis.com/auth/gmail.readonly'
  #SCOPESMAIL = 'https://mail.google.com/'
  store_mail = file.Storage('credentials.json')
  creds_mail = store_mail.get()
  if not creds_mail or creds_mail.invalid:
    flow_mail = client.flow_from_clientsecrets('client_secret_mail.json', SCOPESMAIL)
    creds_mail = tools.run_flow(flow_mail, store_mail)
  service_mail = build('gmail', 'v1', http=creds_mail.authorize(Http()))
  call_google_gmail(service_mail)

def call_google_gmail(svr_mail):
  # Call the Gmail API
  results_mail = svr_mail.users().labels().list(userId='cleteb').execute()
  labels_mail = results_mail.get('labels', [])
  if not labels_mail:
    print('No labels found.')
  else:
    print('Labels:')
    for label in labels_mail:
      print(label['name'])
    
"""#####################################################"""
    

def main():
  """ Define a main() function runs everything """
  
  run_service()
  #setup_google_gmail()
  #call_google_gmail()

if __name__ == "__main__":
  main()
