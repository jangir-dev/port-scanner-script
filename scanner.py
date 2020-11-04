import os, socket 
from datetime import datetime 

os.system("cls")

host = input("Hostname: ")
host_ip = socket.gethostbyname(host)

print("-" * 45)
print(f'Scanning {host_ip}')
print("-" * 45)

time_started = datetime.now()

try:
	port_list = [] # список портов

	for port in port_list:

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((host_ip, port))

		if result == 0:
			print(f"Port {port} open")

		sock.close()

except KeyboardInterrupt:
	print("Exiting...")
	quit()

except socket.gaierror:
	print("Hostname could not be resolved")
	quit()

except socket.error:
	print("Could not connect to server")
	quit()


time_finished = datetime.now()
time_delta = time_finished - time_started

print(f"Used time {time_delta}")

quit()