#! /usr/bin/python2.7

from oauth2client import file, client, tools
from apiclient.discovery import build
from httplib2 import Http

class Hal_Mail():
    
    def __init__(self):
        print "Hal Mail"
        
    """#####################################################"""
    def get_google_gmail(self):
       
        # Setup the Gmail API
        SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
        #store = file.Storage("credentials.json")
        store = file.Storage("/home/clete/Code/HalAssistantOnGitHub/halassistant/hal_mail/credentials.json")
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('gmail', 'v1', http=creds.authorize(Http())) 
        self.call_google_gmail(service)
    
    def call_google_gmail(self, svr_mail):
        # Call the Gmail API
        #results_mail = svr_mail.users().labels().list(userId='cleteb@gmail.com').execute()
        results_mail = svr_mail.users().messages().list(userId='cleteb@gmail.com', maxResults=3, q='from:millerk9@michigan.gov').execute()
        
        #labels_mail = results_mail.get('labels', [])
        #if not labels_mail:
        #    print('No labels found.')
        #else:
        #    print('Labels:')
        #    for label in labels_mail:
        #        print(label['name'])
        
        emails_mail = results_mail.get('messages', [])
        if not emails_mail:
            print('No emails found.')
        else:
            print('emails')
            for email in emails_mail:
                print(email['id'])
                message = svr_mail.users().messages().get(userId='cleteb@gmail.com', id=email['id']).execute()
                
                print 'Message snippet: %s' % message['snippet']
                
                

"""#####################################################"""
def main():

    """ Define a main() function runs everything """
    my_hal_mail = Hal_Mail()
    my_hal_mail.get_google_gmail()
    
if __name__ == "__main__":
    main()