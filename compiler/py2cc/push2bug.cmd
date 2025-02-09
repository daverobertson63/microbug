@echo off
:: This will do a simple upload to he bug from the compiler dir
loader\dfu-programmer.exe atmega32u4 flash microbug\compiler\microbug\build\arduino.avr.leonardo\microbug.ino.hex