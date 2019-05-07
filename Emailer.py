#-- Importing modules --#
import smtplib
import time 

#-- Getting dates and times for emails and logic --#
Day = time.strftime("%a")

#-- This is the weekday message --#
message = """From: YOURNAME <SENDER@SEND.COM>
MIME-Version: 1.0
Content-type: text/html
Subject: 

""" 

#-- This is the message for non weekdays --#
message2 = """From: YOURNAME <SENDER@SEND.COM>
MIME-Version: 1.0
Content-type: text/html
Subject: 

"""

#-- List of adresses to send to --#
li = ["RECIVER1@EXAMPLE.COM", "RECIVER2@EXAMPLE.COM"] # Non-wwekdays
liMon = [] # Monday
liTue = [] # Tuesday
liWed = [] # Wednesday
liThu = [] # Thursday
liFri = [] # Friday

#-- Logic as to which emails to send --#

if Day == "Mon": # Monday
    for i in range(len(liMon)): 
        s = smtplib.SMTP('SMTP SERVER ADDRESS', SMTP SERVER PORT) 
        s.starttls() 
        s.login("SENDER@SEND.COM", "PASSWORD") 
        s.sendmail("sender_email_id", liMon[i], message) 
        s.quit() 
        
else if Day == "Tue": # Tuesday
    for i in range(len(liTue)): 
        s = smtplib.SMTP('SMTP SERVER ADDRESS', SMTP SERVER PORT) 
        s.starttls() 
        s.login("SENDER@SEND.COM", "PASSWORD") 
        s.sendmail("sender_email_id", liMon[i], message) 
        s.quit()  
        
else if Day == "Wed": # Wednesday
    for i in range(len(liWed)): 
        s = smtplib.SMTP('SMTP SERVER ADDRESS', SMTP SERVER PORT) 
        s.starttls() 
        s.login("SENDER@SEND.COM", "PASSWORD") 
        s.sendmail("sender_email_id", liMon[i], message) 
        s.quit()  
        
else if Day == "Thu": # Thursday
    for i in range(len(liThu)): 
        s = smtplib.SMTP('SMTP SERVER ADDRESS', SMTP SERVER PORT) 
        s.starttls() 
        s.login("SENDER@SEND.COM", "PASSWORD") 
        s.sendmail("sender_email_id", liMon[i], message) 
        s.quit()  
        
else if Day == "Fri": # Friday
    for i in range(len(liFri)): 
        s = smtplib.SMTP('SMTP SERVER ADDRESS', SMTP SERVER PORT) 
        s.starttls() 
        s.login("SENDER@SEND.COM", "PASSWORD") 
        s.sendmail("sender_email_id", liMon[i], message) 
        s.quit()  
        
else:
    for i in range(len(li)): # Non-weekdays
        s = smtplib.SMTP('SMTP SERVER ADDRESS', SMTP SERVER PORT) 
        s.starttls() 
        s.login("SENDER@SEND.COM", "PASSWORD") 
        s.sendmail("sender_email_id", liMon[i], message) 
        s.quit()  
