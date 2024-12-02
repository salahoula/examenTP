from netmiko import ConnectHandler
router = {
  "device_type": "cisco_ios",
  "host": "sandbox-iosxe-latest-1.cisco.com",
  "username": "admin",
  "password": "C1sco12345",
  "port": 22,
}

with ConnectHandler(**router) as conn:
    print("Affichage de l'heure côté routeur:")
    output_clock = conn.send_command("show clock")
    print(output_clock)

    print("\n Afficher les interfaces du routeur")
    output_interfaces = conn.send_command("show ip int br")
    print(output_interfaces)
    with open("interfaces.txt", "w") as file:
       file.write(output_interfaces)

    print("\nConfiguration du l'interface loopback")
    config_commands = [
        "interface loopback0",
        "ip address 10.8.8.8 255.255.255.240",
    ]
    net_connect.send_config_set(config_commands)
    print("Configuration terminée.")





