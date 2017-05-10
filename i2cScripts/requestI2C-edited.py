#!/usr/bin/python

import argparse
import subprocess
from smbus2 import SMBusWrapper
### Set up the command line stuff
parser = argparse.ArgumentParser(description='Request integer from address')
parser.add_argument('bus', metavar='b', help='bus to request from (0 or 1)')
parser.add_argument('address', metavar='a', help='address to request from (decimal)')
#parser.add_argument('number', metavar='n', type=str, help='number of bytes to request')

def requestI2C(busNumber, address):

	### send the data
	with SMBusWrapper(args.bus) as bus:
		### read the data from the address given
		data = bus.read_byte_data(9, 0)
		return data

### Parse the arguments
args = parser.parse_args() 

print requestI2C(args.bus, args.address)
