from Device import Device

class ESP_32(Device):
    def __init__(self, deviceName, IP, port, sensors):
        super().__init__(deviceName, IP, port, sensors)
        pass #Put specific ESP32 attributes here