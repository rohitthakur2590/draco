from netmiko import ConnectHandler

# Connect to device
# Execute 'show version'
# Display output

# device = ConnectHandler(device_type='juniper_junos', ip='192.168.122.196', username='vagrant', password='Vagrant')
#
# output  = device.send_command('show version')
# print(output)
# device.disconnect()


device = ConnectHandler(device_type='juniper_junos', ip='192.168.122.196', username='vagrant', password='Vagrant')

interface = device.send_command('show interfaces fxp0 descriptions')

print("Before Merged Operation: ", interface)

configcmds = ["set interfaces fxp0 description Script", "commit"]
device.send_config_set(configcmds)

print("After Merged operation")
output = device.send_command("show interfaces fxp0 descriptions")

print(output)
device.disconnect()



