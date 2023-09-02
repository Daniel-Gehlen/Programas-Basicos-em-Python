``` mermaid
graph TD
  classVehicle[class Vehicle]
  classCar[class Car]
  classMotorcycle[class Motorcycle]

  classVehicle -- Inheritance --> classCar
  classVehicle -- Inheritance --> classMotorcycle

  classVehicle --> initVehicle[__init__brand, model]
  classVehicle --> startEngine[start_engine]
  classVehicle --> stopEngine[stop_engine]

  classCar --> initCar[__init__brand, model, num_doors]
  classCar --> openDoors[open_doors]
  classCar --> closeDoors[close_doors]

  classMotorcycle --> initMotorcycle[__init__brand, model]
  classMotorcycle --> performWheelie[wheelie]

  myCar[my_car = Car Toyota, Camry, 4]
  myMotorcycle[my_motorcycle = Motorcycle Harley-Davidson, Sportster]

  myCar -->|Method Call| startCarEngine[my_car.start_engine]
  myCar -->|Method Call| openCarDoors[my_car.open_doors]

  myMotorcycle -->|Method Call| startMotorcycleEngine[my_motorcycle.start_engine]
  myMotorcycle -->|Method Call| performMotorcycleWheelie[my_motorcycle.wheelie]

```