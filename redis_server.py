import redis
def push_rule(rules,host='localhost'):
    r = redis.StrictRedis(host=host, port=6379, db=0)
    r.rpush('rules',*rules)
    r.publish('DMZ', str(len(rules)))
    return "Rules Pushed"