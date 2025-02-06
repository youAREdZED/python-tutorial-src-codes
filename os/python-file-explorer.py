import os
option = 0
while option != 5:
    print("1.goto ")
    print("2.open file")
    print("3.delete file")
    print("4.copy file")
    print("5.exit")
    option = int(input("enter your option : "))

    if option == 1:
        path = input("enter path : ")
        try:
            os.chdir(path)
            print("now you are on : ", path)
        except:
            print("something went wrong")
    elif option == 2:
        file_name = input("name : ")
        file_path = input("path : ")
        file_type = input("type : ")
        try:
            path = r"{x}{y}.{z}".format(x = file_path, y = file_name, z = file_type)
            os.system("start " + path)
        except:
            print("someting went wrong !")
    elif option == 3:
        file_name = input("name : ")
        file_path = input("path : ")
        file_type = input("type : ")
        try:
            path = r"{x}{y}.{z}".format(x = file_path, y = file_name, z = file_type)
            os.remove(path)
            print("file deleted !")
        except:
            print("something went wrong !")
    elif option == 4:
        file_name = input("name : ")
        file_path = input("path : ")
        file_type = input("type : ")
        file_dist = input("dist : ")
        try:
            src = r"{x}{y}.{z}".format(x = file_path, y = file_name, z = file_type)
            cmd = f'"copy "{src}" "{file_dist}"'
            os.system(cmd)
        except:
            print("something went wrong !")
    else:
        option = 5
        break