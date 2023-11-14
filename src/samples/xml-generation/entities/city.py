# Location
import xml.etree.ElementTree as ET


class City:

    def __init__(self, name):
        City.counter += 1
        self._id = City.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("City")
        el.set("id", str(self._id))
        el.set("name", self._name)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"


City.counter = 0

# <CarData>
#   <Cars>
#     <Car id="0">
#       <CarCompany id="1">
#         <CompanyName>Toyota</CompanyName>
#       </CarCompany>
#       <CarModel id="2">
#         <ModelName>Vitz</ModelName>
#       </CarModel>
#     </Car>
#   </Cars>

#   <Location>
#     <CarLocation id="3">
#       <!-- Location Information -->
#       <City>Islamabad</City>
#       <!-- ... (Other location details) -->
#     </CarLocation>
#   </Location>

#   <CarState>
#     <CarStateInfo id="4">
#       <!-- Car State Information -->
#       <Price>2385000</Price>
#       <Mileage>9869</Mileage>
#       <RegistrationStatus>Un-Registered</RegistrationStatus>
#       <ModelYear>2017</ModelYear>
#       <!-- ... (Other car state details) -->
#     </CarStateInfo>
#   </CarState>

#   <EngineInfo>
#     <CarEngineInfo id="5">
#       <!-- Engine Information -->
#       <EngineType>Petrol</EngineType>
#       <EngineCapacity>1000</EngineCapacity>
#       <!-- ... (Other engine details) -->
#     </CarEngineInfo>
#   </EngineInfo>

#   <AppearanceInfo>
#     <CarAppearanceInfo id="6">
#       <!-- Appearance Information -->
#       <Color>Silver</Color>
#       <BodyType>Hatchback</BodyType>
#       <TransmissionType>Automatic</TransmissionType>
#       <!-- ... (Other appearance details) -->
#     </CarAppearanceInfo>
#   </AppearanceInfo>
# </CarData>