import sys, getopt
import threading
from service_discovery_server import runserver
from dmz_database_query import dmz_query


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
   rsg=False
   flush = False
   try:
      opts, args = getopt.getopt(argv,"h:q:w:e:u:p:g:t:y:d:j:k:l:f",['adduser=','addser=','addgrp=','name=','pwd=','grp=','sername=','serport=','serprot=','rmuser=','rmser=','start=','flush='])
   except getopt.GetoptError:
      print("invalid inputs")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('dmz_server.py help menu')
         sys.exit()
      elif opt in ("-q", "--adduser"):
         au = True
      elif opt in ("-w", "--addser"):
         ase = True
      elif opt in ("-e", "--addgrp"):
          ag = True
      elif opt in ("-u", "--name"):
          username=arg
      elif opt in ("-p", "--pwd"):
          password = arg
      elif opt in ("-g", "--grp"):
          grp = arg
      elif opt in ("-t", "--sername"):
          sn = arg
      elif opt in ("-y", "--serport"):
          spt = arg
      elif opt in ("-d", "--serprot"):
          sp = arg
      elif opt in ("-j", "--rmuser"):
          ru = True
      elif opt in ("-k", "--rmser"):
          rse = True
      elif opt in ("-l", "--start"):
          rsg = True
      elif opt in ("-f", "--flush"):
          flush = True

   if (flush):
       dmz_query.delete_all_users()
   elif (au):
       dmz_query.add_user(username, password)
   elif (ase):
       user = dmz_query.view_user(username, password)
       dmz_query.add_service(user, sp, spt, sn)
   elif (ru):
       dmz_query.delete_user(username, password)
   elif (rse):
       user = dmz_query.view_user(username, password)
       dmz_query.remove_service(user, sp, spt, sn)
   elif(rsg):
       t1 = threading.Thread(target=runserver)
       t1.start()


if __name__ == "__main__":
   main(sys.argv[1:])


