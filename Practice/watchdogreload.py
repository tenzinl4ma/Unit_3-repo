import time
import os
import subprocess
import importlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from kivy.lang import Builder
import main  # Assuming 'main.py' is your Kivy app's main file

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, debounce_time=1.5):
        """Debounce time is the amount of time to wait before reloading after changes are detected."""
        self.debounce_time = debounce_time
        self.last_modified = None

    def reload_kivy(self):
        """Reloads the .kv file without restarting the whole app."""
        print("Reloading .kv file...")
        Builder.unload_file('your_kv_file.kv')  # Unload the old .kv file
        Builder.load_file('your_kv_file.kv')    # Reload the new .kv file

    def reload_python(self):
        """Reloads the main Python module."""
        print("Reloading main Python module...")
        importlib.reload(main)  # Reload the 'main.py' module

    def on_modified(self, event):
        """Triggered when any file changes in the monitored directory."""
        if event.src_path.endswith('.py') or event.src_path.endswith('.kv'):
            if not self.last_modified:
                self.last_modified = time.time()
            else:
                time_since_last = time.time() - self.last_modified
                if time_since_last >= self.debounce_time:
                    if event.src_path.endswith('.kv'):
                        self.reload_kivy()  # Reload the .kv file if changes are detected
                    elif event.src_path.endswith('.py'):
                        self.reload_python()  # Reload the Python file if changes are detected
                    self.last_modified = None  # Reset after reload

    def on_moved(self, event):
        """If files are moved, treat them as modifications as well."""
        self.on_modified(event)

def start_watching():
    """Starts watching the project directory for changes."""
    path = os.getcwd()  # Get the current working directory
    handler = ReloadHandler()
    observer = Observer()
    observer.schedule(handler, path=path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    start_watching()
