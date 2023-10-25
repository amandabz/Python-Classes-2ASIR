try:
    file = open("txt.txt")

except FileNotFoundError:
    print("ERROR: File not found")

else:
    print(file.read())  # if we used f.read(5), only read the first 5 characters

finally:
    file.close()
    print("-----------")
    print("File has been closed")
