#!/bin/bash

# Run from the root of the project
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

echo "$parent_path"

echo "Installing clean micropython image"
mpremote bootloader
sleep 5
cp uf2-images/pimoroni-*.uf2 /Volumes/RP2350
