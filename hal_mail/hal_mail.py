#! /usr/bin/python3

"""#####################################################"""
def setup_google_gmail():
   
    # Setup the Gmail API
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http())) 
    call_google_gmail(service)

def call_google_gmail(svr_mail):
    # Call the Gmail API
    results_mail = svr_mail.users().labels().list(userId='cleteb@gmail.com').execute()
    labels_mail = results_mail.get('labels', [])
    if not labels_mail:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels_mail:
            print(label['name'])

"""#####################################################"""