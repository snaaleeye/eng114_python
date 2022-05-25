# try:
#     file = open("orders.txt")
#
# except FileNotFoundError as errmsg:
#     print("There has been an error! PANIC!!!")
#     print(errmsg)
#     raise

def open_and_print_file(file):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))

        opened_file.close()

    except FileNotFoundError:
        print("File cannot be found or directory is incorrect, please check the details provided")
        raise

open_and_print_file("order.txt")