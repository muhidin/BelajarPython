class Vehicle:
    note = "class to represent a car"

    def __init__(self, name = "common vehicle", number_of_wheels = 4):
        self.name = name
        self.number_of_wheels = number_of_wheels

from typing import Final

ENGINE_ELECTRIC: Final = "electric engine"
ENGINE_GASOLINE: Final = "gasoline engine"
ENGINE_DIESEL: Final = "diesel engine"
ENGINE_HYBRID: Final = "hybrid engine"

class Engine:
    note = "class to represent an engine"

    def __init__(self, engine_name):
        self.engine_name = engine_name

    def drive_sound(self):
        if self.engine_name == ENGINE_ELECTRIC:
            return "whirr"
        elif self.engine_name == ENGINE_GASOLINE:
            return "vroom"
        elif self.engine_name == ENGINE_DIESEL:
            return "chug"
        elif self.engine_name == ENGINE_HYBRID:
            return "hiss"
        else:
            return "unknown engine sound"

class ElectricCar(Vehicle, Engine):
    note = "class to represent an electric car"

    def __init__(self, name = "electric car", number_of_wheels = 4, engine_name = ENGINE_ELECTRIC):
        Vehicle.__init__(self, name, number_of_wheels)
        Engine.__init__(self, engine_name)

    def drive_sound(self):
        return f"{self.name} goes {Engine.drive_sound(self)}"


v1 = Vehicle()
print(v1.name, "has", v1.number_of_wheels)

v4 = ElectricCar()
print(v4.name, "has", v4.number_of_wheels, "wheels. engine sound:", v4.drive_sound())