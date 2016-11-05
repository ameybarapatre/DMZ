#import service_discovery_client
#import service_discovery_server
from dmz_database_query import dmz_query
from redis_server import push_rule
print (dmz_query.delete_all_users())
print(dmz_query.add_user("amey","amey"))
print(dmz_query.add_user("amey","amey"))
#print(dmz_query.view_user("amey","amey"))
#print(dmz_query.delete_user("amey","amey"))
#print(dmz_query.view_user("amey","amey"))
#print(push_rule(['asad' ,'asd']))