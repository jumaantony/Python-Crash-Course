data = open("data.txt", "r+")  # i am opening the data.txt file for reading and writing
full_data = data.read()  # reading all byte into the file from the last cusor
file_data = data.read(18)  # reading 18 bytes
print(full_data, "\n")
print(file_data)
data.close()
