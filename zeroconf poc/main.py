from zeroconf import Zeroconf, ServiceInfo, ServiceBrowser, ServiceStateChange
import socket
import webcolors
import random


SERVICE_TYPE: str = '_http._tcp.local.'
NAMES: list[str] = webcolors.names()
SERVICE_NAME: str = random.choice(NAMES)


def get_local_ip() -> str | None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setblocking(False)
    try:
        # doesn't even have to be reachable
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = None
    finally:
        s.close()
    return ip

print(f'Local ip address: {get_local_ip()}')


# Register the service
desc = {'info': 'Simple mDNS service'}
info = ServiceInfo(
    SERVICE_TYPE,
    SERVICE_NAME + '.' + SERVICE_TYPE,
    addresses=[socket.inet_aton(get_local_ip())],
    port=60080,
    properties=desc)

zeroconf = Zeroconf()
zeroconf.register_service(info)

print('Service registered. Waiting for connections...')


def on_service_state_change(
    zeroconf: Zeroconf, service_type: str, name: str, state_change: ServiceStateChange
) -> None:
    print(f"State changed ({state_change}):")

    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            print(f'  {info.get_name()}')
            print(*[f'  {addr}' for addr in info.parsed_addresses()], sep='\n')
        else:
            print('  no info')

print('Start searhing for services')
browser = ServiceBrowser(zeroconf, SERVICE_TYPE, handlers=[on_service_state_change])


while True:
    pass