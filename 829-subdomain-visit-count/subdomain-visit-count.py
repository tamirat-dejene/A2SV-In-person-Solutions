class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom_cnt, domains = {}, []

        for cnt_domain in cpdomains:
            cnt, domain = cnt_domain.split(" ")
            subdomains = domain.split('.')
            domains.append(subdomains)

            sd = ''
            for i, subdomain in enumerate(subdomains[::-1]):
                sd = subdomain + ('.' if i != 0 else '') + sd
                dom_cnt[sd] = dom_cnt.get(sd, 0) + int(cnt)
        
        return [" ".join([str(dom_cnt[k]), k]) for k in dom_cnt.keys()]


        