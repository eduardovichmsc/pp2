import os

path = "C:/Users/eduar/Desktop/github/pp2/lab_6/dir-and-files/"

# Task 1
listDir = os.listdir(path)
pp2_list = [item for item in listDir]
# print(pp2_list)

# Task 2
is_w_access_ok = os.access(path, os.W_OK)
is_r_access_ok = os.access(path, os.R_OK)
is_e_access_ok = os.access(path, os.EX_OK)
# print(is_r_access_ok, is_w_access_ok, is_e_access_ok, sep="\n")

# Task 3
dir_exists = os.path.exists("dfk")
dir_exists = os.path.exists(path)
# print(dir_exists)

# Task 4
line_counter = 0
file = open("demofile.txt", "r")
for line in file:
  line_counter += 1
# print(line_counter)

# Task 5
new_file = open("list_to_file.txt", "w")
new_file.write(str(listDir))

# Task 6
for i in range(65, 90 + 1):
  create_alph_file = open("./alphabetical/" + chr(i) + ".txt", "w")
  create_alph_file.write("its " + chr(i) + " file")

# Task 7
textFrom = open("demofile.txt", "r").readlines()
text = ""
for i in textFrom:
  text += i + "\n"
copyTo = open("copiedFromDemofile.txt", "w")
copyTo.write(text)

# Task 8
filename = "delete_me.txt"
create_file_to_delete = open(path + "/" + filename, "w")
is_path_exist = os.path.exists(path + "/" + filename)
# print(is_path_exist)

is_d_accesed = os.access(filename, os.X_OK)
# print(is_d_accesed)

# if is_path_exist:
#   os.remove(path + "/" + filename)
# else:
#   print("Couldn't remove the file!")