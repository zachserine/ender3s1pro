#!/usr/bin/env python3

import os
import sys

klipper_folder = "/home/biqu/klipper"
klipper_out = "/home/biqu/klipper/out"
dest = "/home/biqu/klipper_config/bins"

os.chdir(klipper_folder)
bin_file = "klipper.bin"

if not os.path.exists(dest):
    os.makedirs(dest)

make_command = "make"
os.system(make_command)
os.chdir(klipper_out)

os.rename(klipper_out + "/" + bin_file, dest + "/" + bin_file)
