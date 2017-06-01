import stat
import os
import time

path = '/media/vinay/Elements/Movies/English Movies'
os.chdir(path)
# print(os.getcwd())
count = 0
list_2017 = []
list_2016 = []
list_2015 = []
for dirs in os.listdir(path):
    for files in os.listdir(dirs):
        if files.endswith(".mkv") or files.endswith(".mp4") or files.endswith(".avi"):
            # print(os.getcwd())
            path += "/" + dirs
            # print(path)
            os.chdir(path)
            # print(files)
            # print(" " + time.ctime(os.stat(files).st_mtime))
            L = time.ctime(os.stat(files).st_mtime).split()
            # print(L[len(L) - 1])
            # print(files)
            if L[4] == "2017":
                list_2017.append(files)
            elif L[4] == "2016":
                list_2016.append(files)
            elif L[4] == "2015":
                list_2015.append(files)
            count += 1
        path = '/media/vinay/Elements/Movies/English Movies'
        os.chdir(path)


print("The movies added in 2017 are: ")
for i in list_2017 :
    print(i)
print("\n\n\n")

print("The movies added in 2016 are: ")
for i in list_2016 :
    print(i)
print("\n\n\n")

print("The movies added in 2015 are: ")
for i in list_2015 :
    print(i)
print("\n\n\n")

print(count)
