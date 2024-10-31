#!/usr/bin/env python3

import os, sys, subprocess, tempfile, hashlib, binascii

# get a list of connected devices
process = subprocess.run(["mpremote", "connect", "list"], stdout=subprocess.PIPE, universal_newlines=True)
default_device = None
for line in process.stdout.split("\n"):
  if "MicroPython" in line:
    default_device = line.split(" ")[0]

# either use the first detected micropython device (default) or the one specified as the second command line parameter
device = sys.argv[2] if len(sys.argv) > 2 else default_device

# delete all the files on the device

# this script runs on the remote device to return a list of all files and their hashes on the internal storage
tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"""import hashlib, binascii, os
def hash_directory(d):
  for entry in os.ilistdir(d):
    if entry[1] == 0x4000:
      print(d + "/" + entry[0])
      hash_directory(d + "/" + entry[0])
    if entry[1] == 0x8000:
      with open(d + "/" + entry[0], "rb") as f:
        print(d + "/" + entry[0], binascii.hexlify(hashlib.sha1(f.read()).digest()).decode("ascii"))
hash_directory(".")""")
print("> fetch existing file hashes from", device)
tmp.close()
result = subprocess.run(["mpremote", "connect", device, "run", tmp.name], capture_output=True, text=True)
if result.returncode != 0:
  print("  ! failed to get hashes from remote device, error returned was:")
  print()
  print("    ", result.stdout)
  sys.exit(1)

