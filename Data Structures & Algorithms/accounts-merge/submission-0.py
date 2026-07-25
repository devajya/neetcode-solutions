class Solution:
    class DSU:
        def __init__(self, n):
            self.rank = [1] * n
            self.parent = [i for i in range(n)]
            self.num_components = n
        
        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x]) 
            return self.parent[x]
        
        def union(self, x, y):
            par_x = self.find(x)
            par_y = self.find(y)
            
            if par_x == par_y:
                return False

            if self.rank[x] > self.rank[y]:
                self.parent[par_y] = par_x
            elif self.rank[x] < self.rank[y]:
                self.parent[par_x] = par_y
            else:
                self.parent[par_x] = par_y
                self.rank[par_y] += 1
            
            self.num_components -= 1
            return True

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = self.DSU(len(accounts))
        mail_to_acc = {}

        for index, acc in enumerate(accounts):
            emails = acc[1:]
            for email in emails:
                if email in mail_to_acc:
                    dsu.union(index, mail_to_acc[email])
                else:
                    mail_to_acc[email] = index
        
        email_group = defaultdict(list)
        for email, index in mail_to_acc.items():
            parent = dsu.find(index)
            email_group[parent].append(email)

        ans = []

        for index, email in email_group.items():
            name = accounts[index][0]
            ans.append([name] + sorted(email_group[index]))
        
        return ans
        