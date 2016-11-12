import socket
import struct
import sys
import json
from dmz_database_query import dmz_query


def runserver():

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

        #print( sys.stderr, 'received %s bytes from %s' % (len(data), address))
        #print (sys.stderr,user )

        validation="Invalid Credentials"
        validity=dmz_query.view_user(user['username'],user['password'])
        print(validity)

        if validity!=None:

            validation="Logged In"
            print('sending acknowledgement to', address)
            sock.sendto(bytearray(validation,'utf-8'), address)
            dmz_query.add_user_ip(user['username'],user['password'],address[0])
        else:
            print ('sending acknowledgement to', address)
            sock.sendto(bytearray(validation, 'utf-8'), address)

if __name__=='__main__':
    runserver()