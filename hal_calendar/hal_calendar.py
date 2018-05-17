#! /usr/bin/python2.7

from oauth2client import file, client, tools
from apiclient.discovery import build
from httplib2 import Http

"""#####################################################"""
def get_google_calendar():
    """ Setup the Calendar API """
    scopes = 'https://www.googleapis.com/auth/calendar.readonly'
    try:
        store = file.Storage("/home/clete/Code/HalAssistantOnGitHub/halassistant/hal_calendar/credentials.json")
        creds = store.get()
    finally:
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

def calendar_loop(sc, halassistant ):

    # Setup the Calendar API and get the service object
    svr = get_google_calendar()

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

    SCHED.enter(20, 1, calendar_loop, (sc,))

"""#####################################################"""

def main():

    """ Define a main() function runs everything """
    setup_google_calendar()
    
if __name__ == "__main__":
    main()