import socket
import struct
import sys

def service_discovery(user={"username":"amey","password":"amy"}):
    message = bytes(str(user), 'utf-8')
    multicast_group = ('224.3.29.71', 10000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


    try:

        print (sys.stderr, 'sending "%s"' % message)
        sent = sock.sendto(message, multicast_group)

        while True:
            print (sys.stderr, 'waiting to receive')
            try:
                data, server = sock.recvfrom(20)
            except socket.timeout:
                print (sys.stderr, 'timed out, no more responses')
                break
            else:
                print (sys.stderr, 'received "%s" from %s' % (data, server))
                break

    finally:
        print (sys.stderr, 'closing socket')
        sock.close()

if __name__=='__main__':
    service_discovery()