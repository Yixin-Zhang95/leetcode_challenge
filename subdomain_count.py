from collections import defaultdict
def sundomain_counts(cpdomains):
    ans = defaultdict(int)
    for domains in cpdomains:
        count, domain = domains.split()
        count = int(count)
        single_domain = domain.split('.')
        for i in range(0, len(single_domain)):
            ans['.'.join(single_domain[i:])] += count
    #return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
    result = []
    for domain, count in ans.items():
        result.append(str(count) + ' ' + str(domain))
    return result

test = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(sundomain_counts(test))