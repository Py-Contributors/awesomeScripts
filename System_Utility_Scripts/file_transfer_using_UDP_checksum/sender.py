import sys
import os
import socket


# Function that checks and returns argument values
def check_arg():
    # When the size of the array is 2, the received port is returned.
    if len(sys.argv) == 2:
        return sys.argv[1]
    # If the size of the array is not 2, use sys.exit().
    else:
        print("sys exit")
        sys.exit()


# It takes data as an argument and calculates a checksum.
def calc_checksum(data):
    # Initialize the variables s and e to divide by 2 bytes with 0 and 2.
    s = 0
    e = 2
    # It creates an empty list to store the information divided by 2 bytes.
    data_array = []
    # Repeat the length of data divided by 2.
    # Cut data using s and e and add it to data_array.
    for i in range(int(len(data) / 2)):
        data_array.append(data[s:e])
        s += 2
        e += 2
    # Initialize checksum to zero.
    checksum = 0x0
    # Repeat the length of the data array.
    # This is an iterative statement for iteratively calculating checksum.
    for i in range(len(data_array)):
        # print((hex(ord(data_array[i][0]))), (hex(ord(data_array[i][1]))))
        # After converting to ASCII code using the ord function
        # and hexadecimal using the hex function,
        # Since the two data are str type,
        # they are connected and saved. (4 bytes)
        sliced_data = (hex(ord(data_array[i][0])))
        sliced_data = sliced_data + (hex(ord(data_array[i][1])))[2:]
        # print('(a) result :', sliced_data)
        # After converting the data passed through (a)
        # to the existing checksum into int type, it is added.
        checksum += int(sliced_data, 0)
        # print('(b) result :', hex(checksum))
        # The process of (c) can be derived using% operation.
        checksum %= 0xFFFF
        # print('(c) result :', hex(checksum))
    # print('before (e) : ', bin(checksum))
    # This is an operation that inverts the bits of the checksum.
    # It is inverted using XOR operation.
    checksum ^= 0xFFFF
    # print('after (e) : ', bin(checksum))
    # After converting to hexadecimal,
    # truncates the preceding '0x' and returns.
    return (hex(checksum)[2:]).rjust(4, '0')


# This is a function that creates a header.
def make_header(Data, size):
    # 172.30.1.22
    Src_Address = 'ac1e0116'
    # 192.168.56.1
    Dst_Address = 'c0a83801'
    # 00
    Zeros = '00'
    # UDP protocol
    Protocol = '17'
    # Saves the size of the read data received
    # as a factor plus 8 headers.
    length = str(hex((size + 8)))[2:]
    # The rjust() function is used to
    # make 4 bytes by padding the front with zeros.
    UDP_Length = length.rjust(4, '0')
    # Port 8000 is used.
    Src_Port = '1f40'
    # Port 8000 is used.
    Dst_Port = '1f40'
    # Same as UDP Length.
    Length = UDP_Length
    # Set the initial checksum to 0000.
    # Concatenate data into str form.
    init_checksum = '0000'

    data = Src_Address + Dst_Address + Zeros + Protocol + UDP_Length
    data = data + Src_Port + Dst_Port + Length + init_checksum + Data
    # The checksum is calculated using a function
    # defined based on the generated data.
    checksum = calc_checksum(data)
    # Print the calculated checksum.
    print('checksum:', checksum)
    # Fill in the empty checksum with the calculated checksum.
    data = Src_Address + Dst_Address + Zeros + Protocol + UDP_Length
    data = data + Src_Port + Dst_Port + Length + checksum + Data
    # Returns the created data.
    return data


# This is a function that sends a file.
def sender_send(f_name, addr):
    # Sends a message indicating that the receive
    # command has been successfully received.
    server_socket.sendto("received receive command".encode(), addr)
    # If the file exists, it transmits.
    if os.path.isfile(f_name):
        # Create and send a message stating that the file exists.
        is_exist_msg = f_name + " file exists!"
        print(is_exist_msg)
        server_socket.sendto(is_exist_msg.encode(), addr)
        # Calculate and print the file size.
        file_size = os.stat(f_name).st_size
        num = int(file_size / (1024 - 40)) + 1
        file_size_msg = "file_size : " + str(file_size)
        print(file_size_msg)
        # The calculated file size is sent to the receiver.
        server_socket.sendto(file_size_msg.encode(), addr)
        server_socket.sendto(str(num).encode(), addr)
        # The file is read through the open function.
        read_file = open(f_name, 'rb')
        check = num
        # It transmits as much as the file size calculated through the loop.
        while check != 0:
            # The length of header 40 is subtracted from 1024
            # and the file is read.
            chunk_file = read_file.read(1024 - 40)
            # After decoding the read chunk_file to utf-8
            # Create a header using the make_header function.
            data = make_header(chunk_file.decode('utf-8'), len(chunk_file))
            # The created data is transmitted using a socket.
            # At this time, it is encoded with utf-8 and transmitted.
            server_socket.sendto(data.encode('utf-8'), addr)
            # It prints out the number of packet.
            packet_msg = "packet number " + str(num - check + 1)
            print(packet_msg)
            check -= 1
        read_file.close()
        print("send complete")

    # If the file does not exist, a message is created and printed.
    else:
        is_empty_message = f_name + " can't find!"
        print(is_empty_message)


if __name__ == '__main__':
    # Get the port number.
    port = check_arg()

    # Create a socket and prepare to receive data through socket & bind
    print("It was successfully entered. Let's move on!")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Server socket created.")
    server_socket.bind(('', int(port)))
    print("Successful binding. waiting for client now.")

    # It repeats data transmission through an infinite loop.
    while True:
        # It receives the command and file name
        # received from the receiver and saves it.
        msg, addr = server_socket.recvfrom(2000)
        msg = msg.decode().split()
        # If the command is receive, the file is sent through sender_send.
        if msg[0] == 'receive':
            file_name = msg[1]
            sender_send(file_name, addr)
        # If the command is not receive, close the socket and
        # Use the sys.exit() function.
        else:
            print("Command is not correct.")
            print("socket close")
            socket.close()
            print("sys exit")
            sys.exit()
