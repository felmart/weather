#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script to send the weather forecasts to email
import smtplib
import json
import sys


# read email from file
def email_reader(email_file):
    '''Function to read te email data from txt file'''
    with open('email.txt', 'r') as mail:
        pass
    pass


# read password from file
def password_reader(key_file):
    '''Function to read the password for an email account'''
    with open('password.txt', 'r') as pwd:
        pass
    pass


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('email@domain.com', 'PASSWORD')
smtpObj.sendmail('recipient@domain.com', 'Subject: Today\'s Weather Forecast\n')
smtpObj.quit()
