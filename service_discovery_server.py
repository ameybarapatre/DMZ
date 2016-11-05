import socket
import struct
import sys
import json
from dmz_database_query import dmz_query

multicast_group = '224.3.29.71'
server_address = ('', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
while True:
    print( sys.stderr, '\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    user=json.loads(data.decode('utf-8').replace("'", '"'))

    print( sys.stderr, 'received %s bytes from %s' % (len(data), address))
    print (sys.stderr,user )

    validation="Invalid Credentials"
    validity=dmz_query.view_user(user['username'],user['password'])
    print(validity)
    if validity!=None:
        validation="Logged In"
        print(sys.stderr, 'sending acknowledgement to', address)
        sock.sendto(bytes(validation,'utf-8'), address)
    else:
        print (sys.stderr, 'sending acknowledgement to', address)
        sock.sendto(bytes(validation, 'utf-8'), address)