import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def read_Template(filename):
    with open(filename,'r',encoding='utf-8') as template_file:
        template_file_content=template_file.read()
        return Template(template_file_content)

def main():
    message_template=read_Template('template.txt')
    MY_ADDRESS=rankercode447@gmail.com
    PASSWORD=jhakrushna@079

    s=smtplib.SMTP(host="smtp.gmail.com",port=587)
    s.starttls()
    s.login(MY_ADDRESS,PASSWORD)

    with open("detail.csv","r")as csv_file:
        csv_reader=csv.reader