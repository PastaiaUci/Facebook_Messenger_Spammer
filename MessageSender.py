from fbchat import Client
from fbchat.models import *
from password import pw
client = Client('lucadavidstefan21@yahoo.com', pw)


Soce_ID = "100007278813840"
Bogdan_ID = "100004488721512"
Horatiu_ID = "100006267215357"
Andrei_ID = "100009989251335"

thread_type = ThreadType.USER
thread_id = "100006267215357"

i = 1
while i < 12:
    message_id = client.send(Message(text="Noapte Buna"),
                             thread_id=Andrei_ID, thread_type=thread_type)
    i = i+1


Client.logout()
