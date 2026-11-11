import ipaddress
from pathlib import Path
dispositivos=[
    {
        "nombre": "Router01",
        "interfaz": "G0/0",
        "ip": "192.168.1.1",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "Router02",
        "interfaz": "G0/0",
        "ip": "192.168.2.1",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "SwitchCore",
        "interfaz": "VLAN10",
        "ip": "192.168.10.2",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "FirewallEdge",
        "interfaz": "G0/1",
        "ip": "10.0.0.256",
        "mascara": "255.0.0.0"
    },
    {
        "nombre": "ServidorDNS",
        "interfaz": "Eth0",
        "ip": "192.168.2.1",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "AccessPoint01",
        "interfaz": "BVI1",
        "ip": "172.16.5.10",
        "mascara": "255.255.0.0"
    },
    {
        "nombre": "RouterBranch",
        "interfaz": "S0/0/0",
        "ip": "192.168.100.999",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "ServidorSQL",
        "interfaz": "Eth1",
        "ip": "192.168.20.15",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "SwitchAccess",
        "interfaz": "VLAN1",
        "ip": "192.168.1.254",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "GatewayVoz",
        "interfaz": "G0/2",
        "ip": "172.16.1.1",
        "mascara": "255.255.255.128"
    }
]
ips_registradas=[]
ip_validas=0
ips_novalidas=0
ips_duplis=0

for dispositivo in dispositivos:
    ip=dispositivo["ip"]
    nombre=dispositivo["nombre"]
#EXCEPCIONES
    try:
        ipaddress.ip_address(ip)

        if ip in ips_registradas:
            print(nombre, "-", ip, "Dirección IP duplicada")
            ips_duplis+=1
        else:
            print(nombre, "-", ip, "Dirección IP válida")
            ips_registradas.append(ip)
            ip_validas+=1
    except ValueError:
        print(nombre, "-", ip, "Dirección IP no válida")
        ips_novalidas+=1

print("validas:", ip_validas)
print("no validas:", ips_novalidas)
print("duplicadas:", ips_duplis)

carpeta=Path("configuraciones")
carpeta.mkdir(exist_ok=True)

#GENERAR LAS CONFIGURACIONES IP VALIDAS Y NO DUPLICADAS

if ip_validas > 0:

   for ip_valida in ips_registradas:
        for dispositivo in dispositivos:
            if dispositivo["ip"] == ip_valida:
                configuracion=f'''
hostname {dispositivo["nombre"]}
interface {dispositivo["interfaz"]}
ip address {dispositivo["ip"]} {dispositivo["mascara"]}

                end
                '''

                archivo=carpeta/ f'{dispositivo["nombre"]}.txt'
                archivo.write_text(configuracion,encoding="utf-8")
                break

#HAY MARTINEZ JUAN PABLO
#LITIID43
#11/11/26