import socket


def get_ip():
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        socket_instance.connect(('10.255.255.255', 1))
        local_ip = socket_instance.getsockname()[0]
    except:
        local_ip = '127.0.0.1'
    finally:
        socket_instance.close()
    return local_ip
