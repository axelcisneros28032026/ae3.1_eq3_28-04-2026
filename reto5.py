import threading
import time
import random

barrera_lobby = threading.Barrier(4)

def jugador(numero_jugador):
    tiempo_de_carga = random.randint(1, 4)
    time.sleep(tiempo_de_carga)

    print(f"Jugador {numero_jugador} ha cargado y está esperando en el lobby...")

    barrera_lobby.wait()

    print(f"Jugador {numero_jugador} entrando a la partida!")

# Se crean los 4 hilos jugadores
lista_jugadores = []

for i in range(1, 5):
    hilo_jugador = threading.Thread(target=jugador, args=(i,))
    lista_jugadores.append(hilo_jugador)
    hilo_jugador.start()

for hilo in lista_jugadores:
    hilo.join()

print("La partida ha comenzado!")