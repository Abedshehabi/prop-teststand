from Device import Device

class Camera(Device):
    def __init__(self, deviceName, IP, port, sensors):
        super().__init__(deviceName, IP, port, sensors)
        pass #Put unique attributes of camera here