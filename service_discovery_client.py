import socket
import struct
import sys


def service_discovery(user={"username":"amey","password":"amey"}):
    us = str(user)
    message = bytearray(us, 'utf-8')
    multicast_group = ('224.3.29.71', 10000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    addr=''

    try:

        #print (sys.stderr, 'sending "%s"' % message)
        sent = sock.sendto(message, multicast_group)

        while True:
            print ( 'waiting to receive')
            try:
                data, server = sock.recvfrom(20)
            except socket.timeout:
                print ( 'timed out, no more responses')
                break
            else:
                print ( 'received "%s" from %s' % (data, server))
                if data.decode('utf-8')!="Invalid Credentials":
                    addr=server[0]
                break

    finally:
        print ( 'closing socket')
        sock.close()

    return addr

if __name__=='__main__':
    service_discovery()