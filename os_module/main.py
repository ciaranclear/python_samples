import os
from datetime import datetime

# print(dir(os))
# print(help(os))

# get current working directory
print(os.getcwd())

# list directories in current directory
print(os.listdir())

# this modules path
print(__file__)

# this modules directory
directory = os.path.dirname(__file__)
print(directory)

# this modules base
base = os.path.basename(__file__)
print(base)

# this modules directory and base name
print(os.path.split(__file__))

# make directories
path1 = os.path.join("", "sub_dir_l1", "sub_dir_l2")
os.makedirs(path1)

# make directory
path2 = os.path.join(path1, "sub_dir_l3")
os.mkdir(path2)

# change directory
os.chdir(os.path.join(directory, path2))

# add file
file = open("test.txt", "w")
file.close()

# rename file
os.rename("test.txt", "test1.txt")

# file info
print(os.stat("test1.txt"))
mod_time = os.stat("test1.txt").st_mtime
print(datetime.fromtimestamp(mod_time))

# remove file
os.remove("test1.txt")

# change out of directory
os.chdir(directory)

# os walk
for dirpath, dirnames, filenames in os.walk(directory):
    print("Dirpath ", dirpath)
    print("Dirnames ", dirnames)
    print("Filenames ", filenames)
    print()

# remove directory
os.rmdir(path2)

# remove directories
os.removedirs(path1)

# print environ
print(os.environ)

print(os.environ.get("APPDATA"))

# check path exists
print(os.path.exists(__file__))

# check is file
print(os.path.isfile(__file__))

# check is directory
print(os.path.isdir(directory))

# split path and extension
print(os.path.splitext("/tmp/sub/test.txt"))

if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    print(directory)
    # change out of directory
    os.chdir(directory)
    print(directory)
