file = open('C:\\Users\\ASUS\\Desktop\\network.log.txt')

lines = file.readlines()

total_packet = len(lines)
total_traffic = 0

protocol_statistics = {}
top_ips = {}
port_statistics = {}
traffic_by_ip = {}

for line in lines:
    word = line.split()

    ip = word[0]
    port = word[1]
    protocol = word[2]
    bytes_ = int(word[3])

    # Total Traffic
    total_traffic += bytes_

    # Protocol Statistics
    if protocol not in protocol_statistics:
        protocol_statistics[protocol] = 1
    else:
        protocol_statistics[protocol] += 1

    # Packets by IP
    if ip not in top_ips:
        top_ips[ip] = 1
    else:
        top_ips[ip] += 1

    # Packets by Port
    if port not in port_statistics:
        port_statistics[port] = 1
    else:
        port_statistics[port] += 1

    # Traffic by IP
    if ip not in traffic_by_ip:
        traffic_by_ip[ip] = bytes_
    else:
        traffic_by_ip[ip] += bytes_


# Sort IPs by packet count
top = sorted(
    top_ips.items(),
    key=lambda item: item[1],
    reverse=True
)

# Sort ports by packet count
ports = sorted(
    port_statistics.items(),
    key=lambda item: item[1],
    reverse=True
)


print("=" * 15, "Network Traffic Analyzer", "=" * 15)

print(f"\nTotal Packets: {total_packet}")
print(f"Total Traffic: {total_traffic} bytes")

print("\nProtocol Statistics:")
for protocol, count in protocol_statistics.items():
    print(f"{protocol} -> {count}")

print("\nTop IPs:")
for ip, count in top:
    print(f"{ip} -> {count} packets")

print("\nPort Statistics:")
for port, count in ports:
    print(f"{port} -> {count} packets")

print("\nTraffic by IP:")
for ip, traffic in traffic_by_ip.items():
    print(f"{ip} -> {traffic} bytes")

print("=" * 50)




