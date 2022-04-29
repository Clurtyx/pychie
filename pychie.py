import os
import time
print("Hello! Welcome to the 'Pychie' installer!\n Let's get you set up and ready to go!")
time.sleep(3)
intro = input("Press 'Enter' to Begin!")
if intro == "":
     print("Let's go!")
else:
    print("Close enough! ")
print("First, let's get your partitions in order.")
time.sleep(1)
os.system("lsblk && fdisk -l")
disk = input("Which disk would you like to install Arch to?: ")
os.system("cfdisk " disk)