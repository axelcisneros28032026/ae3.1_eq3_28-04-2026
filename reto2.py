import threading
import time

# Máximo 4 conexiones simultáneas
semaforo_bd = threading.Semaphore(4)

def consulta_bd(id_hilo):
    semaforo_bd.acquire()
    try:
        print(f"Hilo {id_hilo} conectando a la BD...")
        time.sleep(2)
        print(f"Hilo {id_hilo} terminó su consulta y libera la conexión")
    finally:
        semaforo_bd.release()

hilos = []

# Crear 20 hilos casi simultáneamente
for i in range(20):
    t = threading.Thread(target=consulta_bd, args=(i+1,))
    hilos.append(t)
    t.start()

# Esperar a que todos terminen
for t in hilos:
    t.join()

print("Todas las consultas han finalizado.")
