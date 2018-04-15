"""
import pageviewapi
tot=pageviewapi.per_article('sv.wikipedia', 'Lady Bird', '20180211', '20180212',
                        access='all-access', agent='all-agents', granularity='daily')


import pageviewapi.period
pageviewapi.period.sum_last('sv.wikipedia', 'Paris', last=30,
                            access='all-access', agent='all-agents')

tot=pageviewapi.period.avg_last('sv.wikipedia', 'Paris', last=30)
"""
import pageviewapi
tot=pageviewapi.per_article('sv.wikipedia', 'Baywatch', '20170602', '20170702',
                        access='all-access', agent='all-agents', granularity='daily')

print tot.items()[0][1][1]['views']

"""
AttrDict({u'items': [{u'access': u'all-access', u'views': 13, u'timestamp':
u'2017120600', u'agent': u'all-agents', u'project': u'sv.wikipedia',
u'granularity': u'daily', u'article': u'The_Ring_(film)'},
{u'access': u'all-access', u'views': 17, u'timestamp': u'2017120700',
u'agent': u'all-agents', u'project': u'sv.wikipedia', u'granularity': u'daily',
u'article': u'The_Ring_(film)'}, {u'access': u'all-access', u'views': 30,
u'timestamp': u'2017120800', u'agent': u'all-agents', u'project':
u'sv.wikipedia', u'granularity': u'daily', u'article': u'The_Ring_(film)'},
{u'access': u'all-access', u'views': 227, u'timestamp': u'2017120900',
u'agent': u'all-agents', u'project': u'sv.wikipedia', u'granularity':
u'daily', u'article': u'The_Ring_(film)'}, {u'access': u'all-access',
u'views': 46, u'timestamp': u'2017121000', u'agent': u'all-agents',
u'project': u'sv.wikipedia', u'granularity': u'daily', u'article':
u'The_Ring_(film)'}]})
"""
