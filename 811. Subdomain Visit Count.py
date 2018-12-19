import collections
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cnt = collections.defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            parts = domain.split('.')[::-1]
            for x in range(1, len(parts) + 1):
                cnt['.'.join(parts[:x][::-1])] += int(count)
        return ['{} {}'.format(v, k) for k, v in cnt.items()]

if __name__ == "__main__":
    print Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])