import socket

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
