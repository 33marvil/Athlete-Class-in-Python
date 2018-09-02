"""code goes here"""
class Athlete:

    def __init__(self, distance=0, time=0): #speed=0):
        self.__total_distance = distance
        self.__total_time = time
        self.__speed = 0

    @property
    def total_distance(self):
        return self.__total_distance

    @property
    def total_time(self):
        return self.__total_time

    def validate_time(self):
        if self.__total_distance == 0 and self.__total_time > 0:
            raise Exception

    #@property # getter
    # Metodo speed
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed


class Runner(Athlete): # Hereda de Athlete Class

    def __init__(self, distance=0, time=0):
        super().__init__(distance, time) # Hereda solo variable instancia
        #self.__speed = speed


    #
    # def total_time(self, total_time):
    #     self.__total_time =














"""Ejemplo de entrada y salida"""

# #instancia de atleta con distancia en metros y tiempo en segundos
# swimmer = Swimmer(50, 10)
#
# #test para swimmer con distancia = 50 y tiempo = 5 segundos
# print(swimmer.swim())
# #>> "Swam 50 meters, time: 10 seconds, speed: 5.0 m/s"
#
# #test para runner al hacer ejercicio, incrementa distancia = 10 metros y tiempo = 5 segundos
# swimmer.new_workout(10, 5)
#
# #test para runner con distancia = 60 metros y tiempo = 15 segundos
# print(swimmer.swim())
#>> "Swam 60 meters, time: 15 seconds, speed: 4.0 m/s"
