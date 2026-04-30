import threading
import time

def monitor_sistema():
    while True:
        print("Monitoreando sistema...")
        time.sleep(1)

# Crear hilo monitor como daemon
monitor = threading.Thread(target=monitor_sistema)
monitor.daemon = True  # se termina automáticamente cuando termina el main thread
monitor.start()

# Hilo principal
print("Programa principal procesando video...")
time.sleep(5)
print("Programa principal terminado. Cerrando sistema.")
