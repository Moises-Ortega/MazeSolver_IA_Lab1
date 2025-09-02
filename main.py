from laberinto import *
from agente import *

def main():
    laberinto = Laberinto("laberinto100x100.csv")
    sragente = SimpleReflexAgent(laberinto.inicioX, laberinto.inicioY)
    gbagente = GoalBasedAgent(laberinto.inicioX, laberinto.inicioY)    
    laberinto.mostrar()
    sragente.avanzar(laberinto.mapa)
    camino = gbagente.avanzarBFS(laberinto.mapa)
    print("Camino encontrado: ", camino, "con ", len(camino), "pasos")


main()
