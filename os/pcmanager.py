import os

print("1.shutdown")
print("2.reboot")
print("3.quit")
option = input("enter option")

if option == "1":
    os.system("shutdown /s /t 1")
elif option == "2":
    os.system("reboot now")
else:
    quit()

