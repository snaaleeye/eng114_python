# try:
#     file = open("orders.txt")
#
# except FileNotFoundError as errmsg:
#     print("There has been an error! PANIC!!!")
#     print(errmsg)
#     raise

# def open_and_print_file(file):
#     try:
#         opened_file = open(file, "r")
#         file_line_list = opened_file.readlines()
#
#         for line in file_line_list:
#             print(line.rstrip('\n'))
#
#         opened_file.close()
#
#     except FileNotFoundError:
#         print("File cannot be found or directory is incorrect, please check the details provided")
#         raise
#
# open_and_print_file("order.txt")

def open_and_print_file(file):
    try:
        with open(file, "r") as files:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except:
        print("file cannot be found or directory is incorrect, please check details")
        raise
    finally:
        print("\nExecution complete")

def write_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check details")
        raise

write_to_file("order.txt", "Lasagna")
open_and_print_file("order.txt")
