#!/bin/python3.11

#Import Libraries.
import os
import oracledb
import pandas as pd
import paramiko
from sqlalchemy import create_engine, types
from datetime import datetime
from dateutil.relativedelta import relativedelta
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

#Set Oracle environment variables.
os.putenv("ORACLE_HOME", "/oracle/app/oracle/product/19c")
os.putenv("ORACLE_SID", "VGER")
os.putenv("ORACLE_PATH", "$ORACLE_HOME/bin:$ORACLE_PATH")

#Define commonly used variables.
now = datetime.now()
today = datetime.today().strftime("%Y%m%d")
currentMonth = format(datetime.now(), "%B")
filename = f'[PUT FILE NAME HERE]_{today}.csv'
filepath = f'[PUT FILE PATH HERE]/{filename}'
remote_filename = f'[PUT FILE NAME HERE]_{today}.csv'
reote_filepath = f'[PUT FILE PATH HERE]/{remote_filename}'

#Connect to oracle database.
oracledb.init_oracle_client()

connection = oracledb.connect (
	user="",
	password="",
	dsn="")
engine = create_engine('oracle+oracledb://', creator=lambda: connection)


#Define Queries.
query = """[PUT ORACLE SQL STATEMENT HERE]"""

#Additional query if needed.
# query2 = """[PUT ORACLE SQL STATEMENT HERE]"""


#Run the query to extract data for all new barcodes identified in the compare query and export to pipe delimited csv file.
df = pd.read_sql(query, engine)
df.to_csv(localFilepath, sep='\t', quotechar='"', index=False)

connection.close()

# Uncomment this block of code and enter missing information to connect to SFTP server and send the file created.
# HOST_NAME = ''
# USER_NAME = ''
# PASSWORD = ''
# PORT = 22
#
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname=HOST_NAME, port=PORT, username=USER_NAME, password=PASSWORD)
#
# sftp_client= client.open_sftp()
# sftp_client.put(localFilepath,remoteFilepath)
# sftp_client.close()


#Uncomment this block of code and enter missing information to send email with file created attached as Excel spreadsheet.
# msg = MIMEMultipart()
# sender=''
# recipients = ['']
# server=smtplib.SMTP('localhost')
# body = ''
#
# msg['Subject'] = ''
# msg['From']=sender
# msg['To'] = ', '.join(recipients)
# body_part = MIMEText(body)
# msg.attach(body_part)
#
# filename = f'{filepath}{filename}'
# attachment = open(filename, 'rb')
# xlsx = MIMEBase('application','vnd.openxmlformats-officedocument.spreadsheetml.sheet')
# xlsx.set_payload(attachment.read())
#
# encoders.encode_base64(xlsx)
# xlsx.add_header('Content-Disposition', 'attachment', filename=filename)
# msg.attach(xlsx)
#
# server.sendmail(sender, recipients, msg.as_string())
# server.quit()
# attachment.close()
