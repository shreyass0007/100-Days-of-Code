#Exception Handling
# try:
#     file=open("a_file.txt")
#     a_dictionary={"key":"value"}
#     print(a_dictionary["sdfsdf"])
# except FileNotFoundError:
#     file=open("a_file.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exit")
# else:
#     content=file.read()
#     print()
# finally:
#     file.close()
#     print("File was closed")


height=float(input("Height:"))
weight=int(input("Weight:"))
BMI=weight/(height*height)
if height>3:
    raise ValueError("Human Height should not be over 3 meter.")
print(BMI)