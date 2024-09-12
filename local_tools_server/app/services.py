from zeroconf import Zeroconf, ServiceInfo, ServiceBrowser, ServiceStateChange
import socket
import webcolors
import random
from .utils import get_local_ip


class Service():
    def __init__(self):
        self.SERVICE_TYPE: str = '_http._tcp.local.'
        self.service_names: list[str] = webcolors.names()
        self.service_name: str = random.choice(self.service_names) + ' ' + str(random    .randint(0, 99))
        self.discovered_services: list[ServiceInfo] = []
        self.zeroconf_discovery: Zeroconf | None = Zeroconf()
        self.zeroconf_service: Zeroconf = Zeroconf()
        self.browser: ServiceBrowser | None = None
        self.register_service()
        self.scan()

    def register_service(self):
        desc = {'info': 'Simple mDNS service'}
        info = ServiceInfo(
            self.SERVICE_TYPE,
            self.service_name + '.' + self.SERVICE_TYPE,
            addresses=[socket.inet_aton(get_local_ip())],
            port=60080,
            properties=desc)
        self.zeroconf_service.register_service(info)


    def scan(self):
        if self.zeroconf_discovery:
            self.zeroconf_discovery.close()
            self.zeroconf_discovery = Zeroconf()

        def on_service_state_change(
            zeroconf: Zeroconf, service_type: str, name: str, state_change: ServiceStateChange
        ) -> None:
            print(f"State changed ({state_change}):")

            if True:
                service_info = zeroconf.get_service_info(service_type, name)
                if service_info:
                    print(f'  {service_info.get_name()}')
                    print(*[f'  {addr}' for addr in service_info.parsed_addresses()], sep='\n')
                else:
                    print('  no info')
            
            if service_info and state_change == ServiceStateChange.Added:
                self.discovered_services.append(service_info)

        self.discovered_services.clear()
        print('Start searhing for services')
        ServiceBrowser(self.zeroconf_discovery, self.SERVICE_TYPE, handlers=[on_service_state_change])
        
    def print_service_info(self, service_name: str):
        service_info = self.zeroconf_discovery.get_service_info(self.SERVICE_TYPE, service_name)
        print(service_info)

    def get_discovered_services(self) -> list[str]:
        return [service.get_name() for service in self.discovered_services]
        

service = Service()
