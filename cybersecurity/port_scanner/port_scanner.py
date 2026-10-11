import socket

target = input("Enter IP address: ")
port = input("Enter port: ")
number = int(port)
port_scanner = socket.socket()
port_scanner.settimeout(3)

try:
    port_scanner.connect((target, number))
    print("Open")

except OSError:
    print("Error, connection unsuccessful")

finally:
    port_scanner.close()
    print("Scan finished")
