import threading
import time

asientos_disponibles = 50

# Lock para proteger la sección crítica
lock = threading.Lock()

def terminal(id_terminal):
    global asientos_disponibles

    for _ in range(15):
        lock.acquire()
        try:
            if asientos_disponibles > 0:
                time.sleep(0.1)
                asientos_disponibles -= 1
                print(f"Terminal {id_terminal} vendió un boleto. Asientos restantes: {asientos_disponibles}")
        finally:
            lock.release()

hilos = []
for i in range(5):
    hilo = threading.Thread(target=terminal, args=(i + 1,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Total de asientos restantes: {asientos_disponibles}")