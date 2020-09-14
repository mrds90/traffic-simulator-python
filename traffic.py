from vehicle import Vehicle
from street import Street
import methods
from land import Land
import random



land1=Land(1000,1500,8)
for x in range(8):
    print(land1.streetList[x].begining)

a=land1.streetList[x].maxSpeedLimit
print(a)

carTest=Vehicle(random.randint(0,len(land1.streetList)),land1)
