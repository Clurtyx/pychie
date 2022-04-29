import os
import time
print("Hello! Welcome to the 'Pychie' installer!\n Let's get you set up and ready to go!")
time.sleep(3)
intro = input("Press 'Enter' to Begin!")
if intro == "mqn":
    print("You have found the easter egg! Mqn nutove moment")
if intro == "":
     print("Let's go!")

print("First, let's get your partitions in order.")
time.sleep(1)
def intro():
    os.system("lsblk && fdisk -l")
    disk = input("Which disk would you like to install Arch to?: ")
    installDrive = input("Is this your drive? (Y,n): ", disk)
    if installDrive == "n":
        return False
while intro():
    pass