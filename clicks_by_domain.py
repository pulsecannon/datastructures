"""Given clicks by domain like this:


input_counts = [
       "600,google.com",
       "200,yahoo.com",
       "20,mobile.yahoo.com",
       "10,com.com",
       "5,mobile.yahoo",
]

Generate clicks by domain breakdown:

com: 830
yahoo.com: 220
google.com: 600
mobile.yahoo.com: 20
com.com: 10
mobile.yahoo: 5
"""

input_counts = [
       "600,google.com",
       "200,yahoo.com",
       "20,mobile.yahoo.com",
       "10,com.com",
       "5,mobile.yahoo",
]

import collections


def calculateClicksByDomain(counts):
    """Naive solution."""
    count_domain = (c.split(',') for c in counts)
    clicks_by_domain = collections.defaultdict(int)
    for count, full_domain in count_domain:
        count = int(count)
        domain_parts = full_domain.split('.')
        domain_parts.reverse()
        prev_part = None
        for idx in range(len(domain_parts)):
            if prev_part:
                part = domain_parts[idx] + '.' + prev_part
            else:
                part = domain_parts[idx]
            clicks_by_domain[(part, idx)] += count
            prev_part = part
    return clicks_by_domain


def calculateClicksByDomain1(counts):
    """Using stack, clean."""
    count_domain = [c.split(',') for c in counts]
    clicks_by_domain = collections.defaultdict(int)
    while count_domain:
        count, domain = count_domain.pop()
        count = int(count)
        clicks_by_domain[domain] += count
        remainder = domain.split(sep='.', maxsplit=1)
        if len(remainder) == 2:
            count_domain.append((count, remainder[-1]))
        else:
            continue
    return clicks_by_domain


if __name__  == '__main__':
    for key, domain in calculateClicksByDomain1(input_counts).items():
        print(key, domain)
