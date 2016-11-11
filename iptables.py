import iptc

def dropAllInbound():
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    rule = iptc.Rule()
    rule.in_interface = 'eth+'
    rule.target = iptc.Target(rule, 'DROP')
    chain.insert_rule(rule)




def allow(rule):
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    rule = iptc.Rule()
    rule.in_interface = 'eth+'
    rule.protocol = 'tcp'
    match = rule.create_match('tcp')
    match.dport = '80'
    rule.target = iptc.Target(rule, 'ACCEPT')
    chain.insert_rule(rule)


def startClean():
    chainIn = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    chainIn.flush()
    chainOut = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'OUTPUT')
    chainOut.flush()