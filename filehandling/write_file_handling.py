try:
    f = open("txt.txt", "a+")  # open the file in "append and read" mode

except FileNotFoundError:  # It won't occur, becasuse with 'a+', if the file doesn't exist, it is created
    print("An ERROR has been ocurred: File not found")

else:
    f.write("\nEnd of the file")

    f.seek(0)  # move the file pointer to the beginning of the file
    print(f.read())

    f.close()

finally:
    print("-----------")
    print("File has been closed")
