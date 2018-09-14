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

    # 2da parte
    @total_time.setter
    def total_time(self, total_time):
        if self.__total_time == 0 and self.__total_time == total_time:
            raise Exception

    def speed_record(self):
        # si velocidad = 0 retur 0 y speed es = 0
        # si velocidad es > 0 return velocidad y actauliza speed, que es resultado de distacia / tiempo
        if self.__total_time == 0:
            self.__speed = 0
            return self.__speed
        else:
            self.__speed = (self.__total_distance / self.__total_time)
            return round(self.__speed, 2)


    @total_distance.setter
    def total_distance(self, total_distance):
        if self.__total_distance == 0 and self.__total_distance == total_distance:
            raise Exception

    def new_workout(self, total_distance, total_time):
        #incrementa total_distance
        self.__total_distance += total_distance
        self.__total_time += total_time

# Runner class
class Runner(Athlete): # Hereda de Athlete Class

    def __init__(self, distance=0, time=0, speed=0):
        super().__init__(distance, time) # Hereda solo variable instancia

    def run(self):                           #llamar variable de instancia
        return "I'm a Runner and Ran " + str(self.total_distance) + " meters, time: " + str(self.total_time) + " seconds, speed: " + str(self.speed_record()) + " m/s"

# Swimmer class
class Swimmer(Athlete):

    def __init__(self, distance=0, time=0, speed=0):
        super().__init__(distance, time) # Hereda solo variable instancia

    def swim(self):                           #llamar variable de instancia
        return "I'm a Swimmer and Swim " + str(self.total_distance) + " meters, time: " + str(self.total_time) + " seconds, speed: " + str(self.speed_record()) + " m/s"
                #"Swam"  meters, time: 10 seconds, speed: 5.0 m/s"

#Cyclist class
class Cyclist(Athlete):

    def __init__(self, distance=0, time=0, speed=0):
        super().__init__(distance, time)

    def roll_a_bicla(self):                           #llamar variable de instancia
        return "I'm a Cyclist and Roll " + str(self.total_distance) + " meters, time: " + str(self.total_time) + " seconds, speed: " + str(self.speed_record()) + " m/s"


# Pruebas a mano de Cyclist lass
cyclist_1 = Cyclist(75, 5)
print(cyclist_1.roll_a_bicla() == "I'm a Cyclist and Roll 75 meters, time: 5 seconds, speed: 15.0 m/s")
cyclist_2 = Cyclist(85, 7)
print(cyclist_2.roll_a_bicla() == "I'm a Cyclist and Roll 85 meters, time: 7 seconds, speed: 12.14 m/s")

# Pruebas a mano de Swimmer class
# swimmer_1 = Swimmer(50, 5)
# print(swimmer_1.swim() == "I'm a Swimmer and Swim 50 meters, time: 5 seconds, speed: 10.0 m/s")
# swimmer_2 = Swimmer(70, 12)
# print(swimmer_2.swim() == "I'm a Swimmer and Swim 70 meters, time: 12 seconds, speed: 5.83 m/s")
# """Ejemplo de entrada y salida"""

# runner_1 = Runner(0, 0)
# print(runner_1.run())
# runner_2 = Runner()
# print(runner_2.run())
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
