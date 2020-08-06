import os
import pandas as pd
from whatsapp import WhatsApp
from apscheduler.schedulers.blocking import BlockingScheduler

def read_job():
    global x
    x =x+1
    pesan =  "Hai "+df.loc[x].values[0]+" Untuk mengikuti webminar WhatsApp Hack with A.I Chatbot anda dapat bergabung di group wa kami dengan link https://chat.whatsapp.com/Ij2wBMpaDMjBO9ZlB13jeb, untuk access zoom dan materi seminar akan diberikan pada group wa"
    print(pesan)
    print(whatsapp.send_message(df.loc[x].values[0],pesan))   
    

whatsapp = WhatsApp(100, session="juaracoding_session")
data = pd.read_excel ('data_peserta_wahack.xlsx')
df = pd.DataFrame(data,columns=['Nama Lengkap'])
rows = len(df)
x =-1;


scheduler = BlockingScheduler()
scheduler.add_job(read_job, 'interval', seconds=5)
scheduler.start()
