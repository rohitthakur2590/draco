from netmiko import ConnectHandler

username = "vagrant"
password = "Vagrant"
device_type = 'juniper_junos'
host = '192.168.122.196'

device = ConnectHandler(device_type=device_type, ip=host, username=username, password=password)

output = device.send_command("show version | display xml")

print(output)

