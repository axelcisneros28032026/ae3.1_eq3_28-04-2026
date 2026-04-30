import threading
import time


señal = threading.Event()

def trabajador(numero):
    print(f"Trabajador {numero} listo, esperando señal...")
    # aqui se queda parado hasta que alguien haga senal.set()
    señal.wait()
    print(f"Trabajador {numero} procesando datos...")

def coordinador():
    print("Coordinador descargando archivos...")
    time.sleep(3)
    print("Descarga finalizada. Dando luz verde a los trabajadores")
    # esto despierta a TODOS los trabajadores al mismo tiempo
    señal.set()

# lista para guardar los hilos
hilos = []

# crear los 5 trabajadores
for i in range(1, 6):
    t = threading.Thread(target=trabajador, args=(i,))
    hilos.append(t)

# crear el coordinador
coord = threading.Thread(target=coordinador)
hilos.append(coord)

# arrancar todos
for h in hilos:
    h.start()

# esperar que terminen todos
for h in hilos:
    h.join()

print("Todo listo")