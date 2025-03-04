import logging
from abc import ABC, abstractmethod

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO, handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ])
logger = logging.getLogger(__name__)

class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str) -> None:
        self.make: str = make
        self.model: str = model
        self.region: str = region 

    @abstractmethod
    def start_engine(self) -> None:
        pass

class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Engine started")

class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Motorcycle started")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")

us_factory: VehicleFactory = USVehicleFactory()
eu_factory: VehicleFactory = EUVehicleFactory()

vehicle1: Vehicle = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()  

vehicle2: Vehicle = eu_factory.create_motorcycle("BMW", "R1250")
vehicle2.start_engine()
