import os

file_path = input("path : ")
file_name = input("name : ")
file_type = input("type : ")

path = r"{x}{y}.{z}".format(x=file_path, y=file_name, z=file_type)

try:
    os.open(path, os.O_CREAT)
    print("file created successfully")
except:
    print("something went wrong !")
