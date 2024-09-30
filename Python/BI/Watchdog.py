import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

Update = r"X:\\BI\\Atualizador\\update.py"
os.system('cls' if os.name == 'nt' else 'clear')
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        os.system(f"python {Update}")

def observar_pasta(pasta):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, pasta, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    pasta_para_observar = 'X:\\BI\\DADOS'  # Insira o caminho da pasta que deseja observar
    observar_pasta(pasta_para_observar)