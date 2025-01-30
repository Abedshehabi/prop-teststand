class Device:
    def __init__(self, deviceName, IP, port, sensors):
        self._deviceName = deviceName
        self._IP = IP
        self._port = port
        self._sensors = sensors

    