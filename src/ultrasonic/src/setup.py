from urm13 import urm13


CURRENT_ADDRESS = 0x12 #default address is 0x12


if __name__ == "__main__":

    print("Entering setup procedure for 1 urm13 sensor.")
    CURRENT_ADDRESS = input("Enter the current address for the sensor you want to setup (default = 18): ")
    NEW_ADDRESS  = input("Enter the new address for this sensor (in decimal): ")

    sensor = urm13(int(CURRENT_ADDRESS))
    sensor.set_address(int(NEW_ADDRESS))

    print('Now printing all registers: ' + sensor.get_all_registers)

    print('Now printing 1 distance measure: ' + sensor.get_distance)

    print("setup complete.")

