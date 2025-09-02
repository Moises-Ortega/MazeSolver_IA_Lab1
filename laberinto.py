import numpy as np

class Laberinto:
    
    def __init__(self, archivo):
        print("Creando laberinto...")
        self.cargar(archivo)
        print("Alto del laberinto:" + str(self.alto))
        print("Ancho del laberinto:" + str(self.ancho))
        print("Inicio:" + str(self.inicioX) + "," + str(self.inicioY))
        print("Final:" + str(self.finX) + "," + str(self.finY))

    def cargar(self, archivo):
        try:
            self.mapa = np.loadtxt(archivo, delimiter=",", dtype=str)
            self.alto = self.mapa.shape[0]
            self.ancho = self.mapa.shape[1]
            self.inicioX = int(np.where(self.mapa == 'S')[0][0])
            self.inicioY = int(np.where(self.mapa == 'S')[1][0])
            self.finX = int(np.where(self.mapa == 'M')[0][0])
            self.finY = int(np.where(self.mapa == 'M')[1][0])

        except Exception as e:
            print("Error al cargar el laberinto")

    def mostrar(self):
        print("Mostrando el laberinto")
        for i in range(0, self.alto):
            for j in range(0, self.ancho):
                print(str(self.mapa[i][j]), end=" ")
            print()





