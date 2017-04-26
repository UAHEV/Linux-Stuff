#!/usr/bin/python

# transmitI2C.py
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

# transmitI2C - Utility for transmitting data over I2C.
#
# Input are the bus number (1 or 0 on raspi), address to send to (in hex, ex: 0x04),
# and the data to transmit (base-10).
#
# Output is the data given, in hexadecimal form, sent over I2C to the address given,
# on the bus specified. An Atmega on the other end of the bus can use missingI2C's
# "long readI2CHex(int howMany)" to recieve the value

import argparse
import subprocess
from smbus2 import SMBusWrapper


### Set up the command line stuff
parser = argparse.ArgumentParser(description='Transmit integer to address')
parser.add_argument('bus', metavar='b', help='bus to transmit on (Will be 0 or 1)')
parser.add_argument('address', metavar='a', type=str, help='address to transmit to (in hex, ex: 0x04)')
parser.add_argument('data', metavar='d', type=str, help='data to transmit')

### parse arguments
args = parser.parse_args()

### send data
with SMBusWrapper(args.bus) as bus:	
	bus.write_i2c_block_data(int(args.address, 16), 0, bytearray(hex(int(args.data))))

#
# FIX THIS
#
# This is "Proof of concept" stuff for a telemetry stream. Eventually, this
# should be ommited entirely and moved to a script somewhere that can fetch
# speed from the motor controller using I2C
#
datastream = open("~/data.txt", "w")

datastream.write(args.data)
