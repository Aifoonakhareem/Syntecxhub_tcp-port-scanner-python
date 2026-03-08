import socket
import threading
import datetime
import time

# User input
target = input("Enter target IP or website: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print("Scanning target:", target)
print("Scanning ports", start_port, "to", end_port)

# Get current scan time
now = datetime.datetime.now()
scan_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Start timer
start_time = time.time()

# Write scan header to log file
with open("results.txt", "a") as file:
    file.write("\n=========================\n")
    file.write(f"Scan Time: {scan_time}\n")
    file.write(f"Target: {target}\n")
    file.write(f"Ports: {start_port} - {end_port}\n")
    file.write("=========================\n")

# Port scanning function
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            output = f"Port {port} is OPEN"
        else:
            output = f"Port {port} is CLOSED"

        print(output)

        # Save result to file
        with open("results.txt", "a") as file:
            file.write(output + "\n")

        s.close()

    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Create threads
threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# End timer
end_time = time.time()
duration = end_time - start_time

print("\nScan completed.")
print("Total scan time:", round(duration, 2), "seconds")

# Log scan duration
with open("results.txt", "a") as file:
    file.write(f"Scan Duration: {round(duration,2)} seconds\n")