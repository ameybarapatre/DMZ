#import service_discovery_client
#import service_discovery_server
from dmz_database_query import dmz_query
from redis_server import push_rule
print (dmz_query.delete_all_users())
"""print(dmz_query.add_user("amey","amey"))
user=dmz_query.view_user("amey","amey")
print(dmz_query.add_service(user,"TCP","1000","Fist"))
print(dmz_query.add_service(user,"UDP","1000","Fist"))
print(dmz_query.add_user_ip("amey","amey","192.168.0.108"))
print(dmz_query.delete_user("amey","amey"))

#print(dmz_query.delete_user("amey","amey"))
#print(dmz_query.view_user("amey","amey"))
#print(push_rule(['asad' ,'asd']))

"""
