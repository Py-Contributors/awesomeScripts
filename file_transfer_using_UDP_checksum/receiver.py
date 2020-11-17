import sys
import socket


# Function that checks and returns argument values
def check_arg():
    # When the array size is 3, it returns the input ip address and port.
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    # If the size of the array is not 3, use sys.exit().
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


def separate_header(data):
    # Cut the header from data.
    header = data[:36]
    # Truncate checksum from data.
    send_checksum = data[36:40]
    # txt file information is cut from data.
    result_data = data[40:]
    # Returns the 3 variables above.
    return header, result_data, send_checksum


if __name__ == '__main__':
    # Get the ip address and port number.
    ip_addr, port = check_arg()
    print("It was successfully entered. Let's move on!")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set it to non-blocking.
    client_socket.setblocking(False)
    # Set timeout to 15.
    client_socket.settimeout(15.0)
    print("receiver socket created.")

    # Receiving data is repeated through an infinite loop.
    while True:
        command = input("enter a command: \n1. receive \n2. exit\n")
        # Divide commands.
        command_list = command.split()
        # If the command is exit, close the socket and
        # Use the sys.exit function.
        if command_list[0] == 'exit':
            print("socket close")
            socket.close()
            print("sys exit")
            sys.exit()
        # If the command is receive, it prepares to receive data.
        if command_list[0] == 'receive':
            # Send command to sender.
            client_socket.sendto(command.encode(), (ip_addr, int(port)))
            # Receives and prints a response to whether the command is valid
            is_valid, addr = client_socket.recvfrom(2000)
            print(is_valid.decode())
            # It receives and prints an answer as to whether the file exists.
            is_exist, addr = client_socket.recvfrom(2000)
            print(is_exist.decode())
            # Receive and print the size of the file.
            file_size, addr = client_socket.recvfrom(2000)
            print(file_size.decode())
            num, addr = client_socket.recvfrom(2000)
            # To print from 1 when printing the packet number
            # Change the variables accordingly.
            num = int(num.decode()) + 1
            check = num
            # The open function write mode is used through the file name.
            write_file = open(command_list[1], 'wb')
            # The file is received as much as the file size through a loop.
            while check != 1:
                # It receives packet from sender.
                chunk_file, addr = client_socket.recvfrom(1024)
                # Through the separate_header function
                # that defines the received packet
                # Separate header and txt file information
                # and checksum.
                header, result_data, send_checksum \
                    = separate_header(chunk_file.decode())
                # To calculate a new checksum from header
                # and txt file information
                # Create data. ('0000' is the place of checksum.)
                new_data = header + '0000' + result_data
                # Print the sender's checksum for explicit viewing.
                print('sender checksum:', send_checksum)
                # Calculate a new checksum
                # using the defined calc_checksum function.
                receive_checksum = calc_checksum(new_data)
                # Print the receiver's checksum
                # so that it can be viewed explicitly.
                print('receiver checksum:', receive_checksum)

                # If the checksum doesn't match, close the socket
                # After printing the output statement, use sys.exit().
                if send_checksum != receive_checksum:
                    socket.close()
                    print('checksum error!')
                    sys.exit()

                # write txt file.
                data = chunk_file[40:]
                write_file.write(data)
                # It prints out the number of packet.
                packet_msg = "packet number " + str(num - check + 1)
                print(packet_msg)
                check -= 1
            write_file.close()
            print("receive complete")

        # If the command is neither exit nor receive
        # Exit socket and use sys.exit().
        else:
            print("Command is not correct.")
            print("socket close")
            socket.close()
            print("sys exit")
            sys.exit()
