```python
import time
import hashlib
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

MONITORED_DIRECTORY = "monitored_folder"
LOG_FILE = "logs/file_activity.log"

logging.basicConfig(
 filename=LOG_FILE,
 level=logging.INFO,
 format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculate_file_hash(file_path):
 """Calculate SHA-256 hash of a file."""
 sha256_hash = hashlib.sha256()
 try:
     with open(file_path, "rb") as file:
         for block in iter(lambda: file.read(4096), b""):
             sha256_hash.update(block)
     return sha256_hash.hexdigest()
 except Exception:
     return "HASH_ERROR"

class FileActivityHandler(FileSystemEventHandler):
 def on_created(self, event):
     if not event.is_directory:
         file_hash = calculate_file_hash(event.src_path)
         logging.info(f"File Created: {event.src_path} | Hash: {file_hash}")

 def on_modified(self, event):
     if not event.is_directory:
         file_hash = calculate_file_hash(event.src_path)
         logging.info(f"File Modified: {event.src_path} | Hash: {file_hash}")

 def on_deleted(self, event):
     if not event.is_directory:
         logging.warning(f"File Deleted: {event.src_path}")

def start_monitoring():
 event_handler = FileActivityHandler()
 observer = Observer()
 observer.schedule(event_handler, MONITORED_DIRECTORY, recursive=True)
 observer.start()

 print("[+] Secure File Transfer Monitoring Started")
 print(f"[+] Monitoring directory: {MONITORED_DIRECTORY}")

 try:
     while True:
         time.sleep(2)
 except KeyboardInterrupt:
     observer.stop()
     print("[!] Monitoring stopped")

 observer.join()

if __name__ == "__main__":
 start_monitoring()
