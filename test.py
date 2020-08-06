import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
from whatsapp import WhatsApp
from apscheduler.schedulers.blocking import BlockingScheduler

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'My Project-36a14dee9910.json'

DIALOGFLOW_PROJECT_ID = 'vigilant-host-192906'
DIALOGFLOW_LANGUAGE_CODE = 'id'
SESSION_ID = 'me'
WHATSAPP_CONTACT = 'bayou'
LAST_DIALOG = ''

def read_job():
    print ("Mulai read data")
    messages = whatsapp.get_last_message_for(WHATSAPP_CONTACT)
    print(messages)
    if LAST_DIALOG != messages :
         sendToDialogflow(messages[len(messages)-1])
    


def sendToDialogflow(texts):
    text_input = dialogflow.types.TextInput(text=texts, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    print(whatsapp.send_message(WHATSAPP_CONTACT,response.query_result.fulfillment_text))   



whatsapp = WhatsApp(100, session="juaracoding_session2")

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

scheduler = BlockingScheduler()
scheduler.add_job(read_job, 'interval', seconds=30)
scheduler.start()