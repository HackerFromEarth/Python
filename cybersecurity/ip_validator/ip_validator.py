ip = input("Enter an IP address: ")
ip_parts = ip.split(".")
is_valid = True
if len(ip_parts) != 4:
    is_valid = False
else:
    for part in ip_parts:
        try:
            number = int(part)
        except:
            is_valid = False
            continue
        if number > 255 or number < 0:
            is_valid = False
if not is_valid:
    print("Invalid IP")
else:
    print("Valid IP")
