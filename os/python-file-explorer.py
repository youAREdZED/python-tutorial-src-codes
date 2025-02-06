import os

option = 0

while option != 5:

    print("1.goto ")
    print("2.open file")
    print("3.delete file")
    print("4.copy file")
    print("5.quit")
    option = int(input("enter option : "))
    if option == 1:
        path = input("enter your path : ")
        try:
            os.chdir(path)
            print("now you are on : ", path)
        except:
            print("something went wrong!")
    elif option == 2:
        file_path = input("enter your file path : ")
        file_name = input("enter your file name : ")
        file_type = input("enter your file type : ")
        try:
            path = r"{x}{y}.{z}".format(x=file_path, y=file_name, z=file_type)
            os.system("start " + path)
            print("file now is open")
        except:
            print("something went wrong!")
    elif option == 3:
        file_path = input("enter your file path : ")
        file_name = input("enter your file name : ")
        file_type = input("enter your file type : ")
        try:
            path = r"{x}{y}.{z}".format(x=file_path, y=file_name, z=file_type)
            os.remove(path)
            print("your file removed successfully")
        except:
            print("something went wrong!")
    elif option == 4:
        file_path = input("enter your file path : ")
        file_name = input("enter your file name : ")
        file_type = input("enter your file type : ")
        file_dist = input("enter your file dist : ")
        path = r'{x}{y}.{z}'.format(x=file_path, y=file_name, z=file_type)
        try:
            cmd = f'copy "{path}" "{file_dist}"'
            os.system(cmd)
        except:
            print("something went wrong !")
    else:
        option = 5
        break
