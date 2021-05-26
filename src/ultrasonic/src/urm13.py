from smbus2 import SMBus
import time
import numpy as np

class urm13:
    def __init__(self, cur_address):
        self.bus = SMBus(1)
        self.address = cur_address
        self.set_address(self.address)
        self.set_default()
    
    def set_register(self, offset, value):
        self.bus.write_i2c_block_data(self.address, offset, [value])
    
    def get_register(self,start,end):
        block = self.bus.read_i2c_block_data(self.address,start,end-start+1)
        return block

    def get_all_registers(self):
        return self.bus.read_i2c_block_data(self.address,0,13)

    def set_mult_registers(self, offsets, values):
        for i in range(len(offsets)):
            self.set_register(offsets[i],values[i])
    
    def set_default(self):
        """set all values other than i2c communication address to default as provided on wiki"""
        values = [self.address,0x02,0x10,0xFF,0xFF,0xFF,0xFF,0x00,0x00, 0x04,0x00,0x00,0x00] #defaults as provided on datasheet: https://wiki.dfrobot.com/URM13_Ultrasonic_Sensor_SKU_SEN0352 
        offsets = range(0,13)
        self.set_mult_registers(offsets,values)

    def set_address(self,address):
        """set i2c commmunication address"""
        self.set_register(0,address)
        self.address = address

    def get_address(self):
        return self.address

    def get_PID_register(self):
        """Product check (detect sensor type)"""
        PID = self.get_register(1,1)
        return PID

    def get_VID_register(self):
        """Firmware Version: 0x10 for V1.0"""
        VID = self.get_register(2,2)
        return VID
    
    def get_distance(self):
        """get distance in cm"""
        distance = "0x"
        distance_bytes = self.get_register(3,4)
        for dist in distance_bytes:
            distance += hex(dist)[2:]
        distance = int(distance, 16)
        return distance

    def get_board_temp(self):
        """get the internal temperature of the board in Celcius"""
        temp = "0x"
        temp_bytes = self.get_register(5,6)
        for temp in temp_bytes:
            temp += hex(temp)[2:]
        temp = int(temp, 16) * 0.1
        return temp

    def set_external_temp_compensation(self, temp):
        """write ambient temeperature data to this register for external temperature compensation in celcius"""
        value = temp / 0.1
        #if exceeds max then set to max
        if(value > 65535):
            value = 65535

        self.temp_compensation = value
        hex_temp_comp = ("000" + hex(value)[2:])[-4:] #pad the hexidecimal out to always be four chars
        values_2_write = [int("0x" + hex_temp_comp[:2],16), int("0x" + hex_temp_comp[3:],16)]
        self.set_mult_registers([7,8],values_2_write)
 
    def get_external_temp_comp(self):
        """get the external temp comensationg set by user in celcius"""
        temp = "0x"
        temp_bytes = self.get_register(7,8)
        for temp in temp_bytes:
            temp += hex(temp)[2:]
        temp = int(temp, 16) * 0.1
        return temp

    def set_full_config(self, configs=[0,0,0,0,0,1,0,0]): 
        """default config = 0x04 = 00000100"""
        config_string = "".join(configs)
        config_dec = int(config_string,base=2)
        self.set_register(9,config_dec)

    def get_full_config(self):
        return self.get_register(9,9)

    def set_single_config(self,offset,mode):
        curr_config = self.get_full_config()[0]
        curr_config_bin = list(("0000000" + bin(curr_config)[2:])[-8:]) #pad the binary out to always be 8 chars
        curr_config_bin[-offset - 1] = str(mode)
        curr_config_bin = int("".join(list(curr_config_bin)),2)
        self.set_register(9,curr_config_bin)

    def config_range_mode(self,mode):
        """Set Ranging Mode: 0 for long range mode, 1 for short range mode"""
        self.set_single_config(4,mode)

    def config_detect_mode(self,mode):
        """Set Detection Mode: 0 for auto detection, 1 for trigger detection"""
        self.set_single_config(2,mode)

    def config_temp_comp(self,mode):
        """Enable or Disable Temp Compensation: 0 for disable, 1 for enable"""
        self.set_single_config(1,mode)

    def config_internal_external_comp(self,mode):
        """Use internal or external temp compensation: 0 for internal, 1 for external"""
        self.set_single_config(1,mode)

    def trigger_measurement(self):
        """Trigger one measurement, the value will be stored in the distance register. Note: only works when detection mode is set to trigger mode"""
        self.set_register(10,0x01)

    def get_electrical_noise_degree(self):
        """	0x00-0x0A corresponds to noise degree 0 to 10. This parameter can reflect the influence of power supply and environment on the sensor. The smaller the noise level, the more accurate the distance value detected by the sensor."""
        return self.get_register(11,11)

    def set_sensitivity(self,value):
        """0x00-0x0A corresponds to sensitivity level 0 to 10. Set the ranging sensitivity in large measuring range(40-900cm). The smaller the value, the higher the sensitivity."""
        self.set_register(12,value)
    
    def get_sensitivity(self):
        """0x00-0x0A corresponds to sensitivity level 0 to 10. Set the ranging sensitivity in large measuring range(40-900cm). The smaller the value, the higher the sensitivity."""
        return self.get_register(12,12)
if __name__ == "__main__":
    addresses = [0x11,0x12,0x13]
    sensors = []
    for address in addresses:
        sensors.append(urm13(address))

    for sensor in sensors:
        sensor.config_range_mode(0)
        sensor.config_detect_mode(1)
        print(sensor.get_full_config())



    time.sleep(5)
    # for sensor in sensors:
    #     sensor.config_detect_mode(0)
    old_distance = 0
    start = time.time()
    while(1):
        start = time.time()
        for sensor in sensors:
            sensor.trigger_measurement()
        time.sleep(.07)
        for i, sensor in sensors:
            distance = sensor.get_distance()
            print("[Sensor {}]: Distance: {}".format(i,distance),end=" ")
        end = time.time()
        print("Time Elapsed: {}".format(end - start))
 






