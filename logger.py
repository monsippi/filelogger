import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileSystemEventHandler

class Watcher:
    # Set the directory on watch
    watchDirectory = "."

    def __init__(self):
        self.observer = Observer()
        self.handler = Handler()

    def logs(self):
        return self.handler.logs

    def run(self):
        self.observer.schedule(self.handler, self.watchDirectory, recursive = True)
        self.observer.start()


class Handler(FileSystemEventHandler):
    def __init__(self):
        self.logs = []

    def on_created(self, event):
        self.logs.append((event.event_type, event.src_path, "File was created"))

    def on_deleted(self, event):
        self.logs.append((event.event_type, event.src_path, "File was deleted"))

    def on_modified(self, event):
        self.logs.append((event.event_type, event.src_path, "File was modified"))

    def on_moved(self, event):
        self.logs.append((event.event_type, event.src_path, "File was moved to {}".format(event.dest_path)))
