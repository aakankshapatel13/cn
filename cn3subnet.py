def to_binary(num):
    return f"{num:08b}"

def get_ip():
    ip = input("Enter IP (192.B.C.D format): ").split('.')
    return [int(x) for x in ip]

def get_cidr():
    while True:
        try:
            cidr = int(input("Enter CIDR (24-31): "))
            if 24 <= cidr <= 31:
                return cidr
            print("CIDR must be between 24 and 31.")
        except ValueError:
            print("Please enter a valid integer.")

def calculate_mask(cidr):
    subnet_mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
    mask_octets = [(subnet_mask >> (8 * i)) & 0xFF for i in range(3, -1, -1)]
    return mask_octets

def calculate_addresses(ip, mask):
    network = [ip[i] & mask[i] for i in range(4)]
    broadcast = [network[i] | (255 - mask[i]) for i in range(4)]
    return network, broadcast

def display_info(ip, mask, network, broadcast):
    print("Subnet mask in numeric format:", '.'.join(map(str, mask)))
    print("Subnet mask in binary format :", ''.join(to_binary(x) for x in mask))
    
    print("Network address in numeric format:", '.'.join(map(str, network)))
    print("Network address in binary format :", ''.join(to_binary(x) for x in network))
    
    print("Broadcast address in numeric format:", '.'.join(map(str, broadcast)))
    print("Broadcast address in binary format:", ''.join(to_binary(x) for x in broadcast))
    
    first_addr = network[:3] + [network[3] + 1]
    last_addr = broadcast[:3] + [broadcast[3] - 1]
    print("First address in numeric format:", '.'.join(map(str, first_addr)))
    print("Last address in numeric format:", '.'.join(map(str, last_addr)))
    print("First address in binary format :", ''.join(to_binary(x) for x in first_addr))
    print("Last address in binary format  :", ''.join(to_binary(x) for x in last_addr))

def main():
    ip = get_ip()
    cidr = get_cidr()
    mask = calculate_mask(cidr)
    network, broadcast = calculate_addresses(ip, mask)
    display_info(ip, mask, network, broadcast)

if __name__ == "__main__":
    main()
