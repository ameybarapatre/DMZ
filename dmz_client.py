import sys, getopt
import threading
import service_discovery_client
from dmz_database_query import dmz_query
import redis_client

def main(argv):
   au = False
   ase = False
   username=""
   password=""
   ag =False
   grp=0
   sn=''
   spt=''
   sp=''
   ru=False
   rse=False
   rg=False
   flush = False
   try:
      opts, args = getopt.getopt(argv,"h:u:p",['name=','pwd='])
   except getopt.GetoptError:
      print("invalid inputs")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('dmz_server.py help menu')
         sys.exit()
      elif opt in ("-u", "--name"):
          username=arg
      elif opt in ("-p", "--pwd"):
          password = arg

   return username ,password

if __name__ == "__main__":
    user = {}
    user['username'], user['password'] = main(sys.argv[1:])
    address=service_discovery_client.service_discovery(user)
    if address!='':
        t1 = threading.Thread(target=redis_client.rules_daemon(address))
        t1.start()