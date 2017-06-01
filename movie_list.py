import stat
import os
import time

path = '/media/vinay/Elements/Movies/English Movies'

try:
    os.chdir(path)
    # print(os.getcwd())
    count = 0
    list_2017 = []
    list_2016 = []
    list_2015 = []

    for root, dirs, files in os.walk(path):
        # print(root)
        # os.chdir(root)
        # print(files)
        for i in files:
            if i.endswith(".mkv") or i.endswith(".mp4") or i.endswith(".avi"):
                os.chdir(root)
                if os.stat(i).st_size > 100000000 :
                    # print(time.ctime(os.stat(i).st_mtime))
                    L = time.ctime(os.stat(i).st_mtime).split()
                    # print(i)
                    # print(os.stat(i).st_size)
                    # print(L[4])
                    # print(i)
                    if L[4] == "2017":
                        list_2017.append(i)
                    elif L[4] == "2016":
                        list_2016.append(i)
                    elif L[4] == "2015":
                        list_2015.append(i)
                    count += 1

    # print("The movies added in 2017 are: ")
    # for i in list_2017 :
    #     print(i)
    # print("\n\n\n")
    #
    # print("The movies added in 2016 are: ")
    # for i in list_2016 :
    #     print(i)
    # print("\n\n\n")
    #
    # print("The movies added in 2015 are: ")
    # for i in list_2015 :
    #     print(i)
    # print("\n\n\n")
    # print("The Total no of video files are: " + str(count))

    os.chdir(path)
    with open("movies added in 2017.txt", "w") as m:
        count = 1
        for i in list_2017 :
            m.write(str(count) + "." + i + "\n")
            count += 1

    with open("movies added in 2016.txt", "w") as m:
        count = 1
        for i in list_2016 :
            m.write(str(count) + "." + i + "\n")
            count += 1

    with open("movies added in 2015.txt", "w") as m:
        count = 1
        for i in list_2015 :
            m.write(str(count) + "." + i + "\n")
            count += 1
except IOError:
    print("could not open " + path)
