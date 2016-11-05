import redis

def rules_daemon(host='localhost'):
    r = redis.StrictRedis(host=host, port=6379, db=0)
    p = r.pubsub()
    p.subscribe('DMZ')
    print("listening")
    f = False
    i = 0
    r.delete('rules')
    for message in p.listen():
        if f :
            print(message)
            rules = r.lrange('rules', i, i+int(message['data']))
            i += int(message['data'])
            print(i,rules)
        else :
            f=True


if __name__=='__main__':
    rules_daemon()
