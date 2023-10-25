try:
    file = open("txt.txt")

except FileNotFoundError:
    print("An ERROR has been ocurred: File not found")

else:
    print(file.read())  # if we used f.read(5), only read the first 5 characters
    file.close()

finally:
    print("-----------")
    print("File has been closed")
