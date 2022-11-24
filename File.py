import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

source = "C:/Users/Dell/Downloads"


# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1
  def on_created(self, event):
    print(f"Hey, (event.src_path) has been created!")

  def on_deleted(self, event):
    print(f"Oops! Someone has deleted (event.src_path)!")

  def on_modified(self, event):
    print(f"Hey There!, (event.src_path) has been modified")

  def on_moved(self, event):
    print(f"Someone moved (event.src_path) to (event.dest_path")
    

   


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
try:



  while True:
    time.sleep(2)
    print("running...")

except KeyboardInterrupt:
    print("stopped!")
    observer.stop()