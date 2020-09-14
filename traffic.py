from vehicle import Vehicle
from street import Street
import methods

carTest=Vehicle(60,1,4)
streetTest= Street(1,(1,3),(5,8),4)

print(streetTest.lanes)
print(carTest.lane)

print(carTest.streetPercent)


print(carTest.initial_direction(streetTest.yDir))
print(carTest.initial_position((1,3),(5,8)))






