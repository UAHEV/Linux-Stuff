#!/usr/bin/python


import argparse
import subprocess
from smbus2 import SMBusWrapper


### Set up the command line stuff
parser = argparse.ArgumentParser(description='Request integer from address')
parser.add_argument('bus', metavar='b', help='bus to request from (0 or 1)')
parser.add_argument('address', metavar='a', type=str, help='address to request from (in hex, ex: 0x04)')
#parser.add_argument('number', metavar='n', type=str, help='number of bytes to request')

### parse arguments
args = parser.parse_args()

### send the data
with SMBusWrapper(args.bus) as bus:	
	### Read a block of 16 bytes from address 80, offset 0
    	block = bus.read_i2c_block_data(0x08, 0, 6)
    	### Set the string for output
	returnData = ""
	### Returned value is a list of 16 byte
	for value in block:
		if (value < 128):
			returnData += str(chr(value))
	### And print
	print(returnData)
	
#	try:
#    	bus.write_i2c_block_data(args.address, 0, bytearray(args.data))
#	except IOError:
#   		subprocess.call(['i2cdetect', '-y', '1'])
#  		flag = 1
