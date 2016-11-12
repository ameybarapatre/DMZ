import iptc

def dropAllInbound():
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    rule = iptc.Rule()
    rule.target = iptc.Target(rule, 'DROP')
    chain.insert_rule(rule)




def fire_rule(rul):
    print(rul , 'recieved')
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    rule = iptc.Rule()
    rule.protocol = rul['protocol']
    rule.src=rul['ip']+"/255.255.255.0"
    match = rule.create_match('tcp')
    match.dport = str(rul['port'])

    rule.target = iptc.Target(rule, rul['action'])
    chain.insert_rule(rule)


def startClean():
    chainIn = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    chainIn.flush()
    chainOut = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'OUTPUT')
    chainOut.flush()

if __name__=='__main__':
    startClean()
    print('cleaned')















