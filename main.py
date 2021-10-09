import os
import pyudev
import time
from aion.logger import lprint
from aion.kanban import KanbanConnection
from aion.microservice import main_decorator, Options


SERVICE_NAME = "check-usb-dongle-connection"
PATH = "/dev/"
DEVICE = "ttyUSB2"
INTERVAL = 1

class CheckUsbDongle():
    def check_connection_loop(self):
        print("[CHECK_USB_DONGLE] start to check loop")
        while True:
            res = self.check_connection()
            if res:
                print("[CHECK_USB_DONGLE] USB Dongle is detected (path: {})".format(res[0]))
                # vendor = self.check_vendor(res[0])
                vendor = self.check_vendor(os.path.join('/dev/', res[0]))
                # print("[CHECK_USB_DONGLE] Dongle Vendor: {}".format(vendor))
            else:
                print("[CHECK_USB_DONGLE] No Dongle is detected")
            time.sleep(INTERVAL)
            
    def check_connection(self):
        files = os.listdir(PATH)
        return [f for f in files if DEVICE in f]
        
    def check_vendor(self, path: str):
        context = pyudev.Context()
        print(path)
        dev = pyudev.Devices.from_device_file(context, path)
        return dev.get('ID_MODEL')

@main_decorator(SERVICE_NAME)
def main(opt: Options):
    cud = CheckUsbDongle()
    cud.check_connection_loop()

if __name__ == "__main__":
    main()
