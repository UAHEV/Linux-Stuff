#!/usr/bin/python

# requstI2C_wrapper.py
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

# A simple wrapper for the requestI2C() function in i2cUtilities.

import argparse
from i2cUtilities import requestI2C

### Set up the command line stuff
parser = argparse.ArgumentParser(description='Request data from I2C device')
parser.add_argument('bus', metavar='b', help='bus to request from (0 or 1)')
parser.add_argument('address', metavar='a', help='address to request from (decimal)')

### Parse the command line arguments
args = parser.parse_args()

### and make the request
print requestI2C(args.bus, args.address)
