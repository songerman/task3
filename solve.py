import argparse
import socket
from threading import *
import sys


class UDPListener:

    def __init__(self, ip):
        self.ip = ip

    def try_to_connect(self, _port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.ip, _port))
            print(_port)
            sock.close()
        except TypeError:
            pass
        except OSError:
            pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Программа ищет открытые TCP порты.'
                    'Use -p *port* to get open ports')
    parser.add_argument('-i', '--ip',
                        type=str,
                        help='Type ip address here',
                        dest='ip')

    ip = parser.parse_args().ip
    udp_listener = UDPListener(ip)

    with open("ports.txt") as f:
        _range = f.read().split('\n')

    print("Пожалуйста, подождите, это займет некоторое время...")
    print("Открытые порты:")
    for port in range(int(_range[0]), int(_range[1])):
        thread = Thread(udp_listener.try_to_connect(port))
        thread.start()
        thread.join()
    sys.exit(1)
