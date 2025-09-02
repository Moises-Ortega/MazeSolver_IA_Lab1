from collections import deque

class Agente:

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.dir = str("nte")
        self.actual = str('S')
        print("El agente apareció en la posición:" + str(self.posX) + "," + str(self.posY))

class SimpleReflexAgent(Agente):
    def avanzar(self, mapa):
        pasos = int(0)
        while(self.actual != 'M' and pasos <= 10000):
            match self.dir:
                case "nte":
                    if(mapa[self.posY][self.posX+1] != '1'):
                        self.posX += 1
                        self.dir = "est"
                    elif(mapa[self.posY-1][self.posX] != '1'):
                        self.posY -= 1
                    elif(mapa[self.posY][self.posX-1] != '1'):
                        self.posX -= 1
                        self.dir = "oes"
                    else:
                        self.dir = "oes"
                        #pasos -=1
                case "sur":
                    if(mapa[self.posY][self.posX-1] != '1'):
                        self.posX -= 1
                        self.dir = "oes"
                    elif(mapa[self.posY+1][self.posX] != '1'):
                        self.posY += 1
                    elif(mapa[self.posY][self.posX+1] != '1'):
                        self.posX += 1
                        self.dir = "est"
                    else:
                        self.dir = "est"
                        #pasos -=1
                case "est":
                    if(mapa[self.posY+1][self.posX] != '1'):
                        self.posY += 1
                        self.dir = "sur"
                    elif(mapa[self.posY][self.posX+1] != '1'):
                        self.posX += 1
                    elif(mapa[self.posY-1][self.posX] != '1'):
                        self.posY -= 1
                        self.dir = "nte"
                    else:
                        self.dir = "nte"
                        #pasos -=1
                case "oes":
                    if(mapa[self.posY-1][self.posX] != '1'):
                        self.posY -=1
                        self.dir ="nte"
                    elif(mapa[self.posY][self.posX-1] != '1'):
                        self.posX -= 1
                    elif(mapa[self.posY+1][self.posX] != '1'):
                        self.posY += 1
                        self.dir = "sur"
                    else:
                        self.dir = "sur"
                        #pasos -=1
            pasos += 1
            self.actual = str(mapa[self.posY][self.posX])
            print("Posición actual: (" + str(self.posX) + "," + str(self.posY) + ") " + "Sentido: " + self.dir)
        if pasos <= 10000:
            print("Laberinto completado en " + str(pasos) + " pasos :)")
        else:
            print("Se han sobrepasado los 10,000 pasos y no se ha podido completar el laberinto")


class GoalBasedAgent(Agente):

    visitados = set()
    porVisitar = deque()
    padres = {}

    def avanzarBFS(self, mapa):
        inicio = (self.posY, self.posX)
        self.porVisitar.append(inicio)
        self.padres[inicio] = None

        while self.porVisitar:
            y, x = self.porVisitar.popleft()

            if (y, x) in self.visitados:
                continue
            self.visitados.add((y, x))

            if mapa[y][x] == "M":
                return self.reconstruir_camino((y, x))

            movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dy, dx in movimientos:
                ny, nx = int(y + dy), int(x + dx)
                if (0 <= ny < len(mapa) and 0 <= nx < len(mapa[0]) 
                    and mapa[ny][nx] != 1   # no es muro
                    and (ny, nx) not in self.visitados
                    and (ny, nx) not in self.padres):

                    self.porVisitar.append((ny, nx))
                    self.padres[(ny, nx)] = (y, x)

        return None

    def reconstruir_camino(self, objetivo):
        camino = []
        actual = objetivo
        while actual is not None:
            camino.append((int(actual[0]), int(actual[1])))
            actual = self.padres[actual]
        camino.reverse()
        return camino
        


