# i2cUtilities.py
#
# Written by Will Boyd
#
# Copyright 2017 UAHEV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from smbus2 import SMBusWrapper

######################################################################################
# transmitI2C - Utility for transmitting data over I2C.                              #
#                                                                                    #
# Input are the bus number (1 or 0 on raspi), address to send to (in hex, ex: 0x04), #
# and the data to transmit (base-10).                                                #
#                                                                                    #
# Output is the data given, in hexadecimal form, sent over I2C to the address given, #
# on the bus specified. An Atmega on the other end of the bus can use missingI2C's   #
# "long readI2CHex(int howMany)" to recieve the value                                #
######################################################################################
def transmitI2C(bus, address, data):
    with SMBusWrapper(args.bus) as bus:
    	bus.write_i2c_block_data(int(address, 16), 0, bytearray(hex(int(data))))

### End transmitI2C()

######################################################################################
# requestI2C - Utility for requesting data over I2C.                                 #
#                                                                                    #
# Input are the bus number (1 or 0 on raspi) and address to send to (in decimal),    #
#                                                                                    #
# The function returns the recieved response, in decimal form                        #
######################################################################################
def requestI2C(bus, address):

	### send the data
	with SMBusWrapper(bus) as bus:
		### read the data from the address given
		data = bus.read_byte_data(address, 0)
        return data

### End requestI2C()
