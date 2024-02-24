class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        has_secret = set([0, firstPerson])
        meetings.sort(key = lambda x:x[2])

        # group meetings by time
        for k,v in groupby(meetings, key = lambda x:x[2]):
            meetings_occuring_now = list(v)
            adj = defaultdict(list)
            done = set()
            queue = deque()

            # build graph, if person has secret add them to queue so 
            # we start with them in the BFS later
            for a,b, _ in meetings_occuring_now:
                adj[a].append(b)
                adj[b].append(a)
            for person in adj.keys():
                if person in has_secret:
                    queue.append(person)

            # normal BFS to spread the secret
            while queue:
                person = queue.popleft()
                if person in done:
                    continue
                done.add(person)
                has_secret.add(person)
                for other in adj[person]:
                    if other not in done:
                        queue.append(other)

        return list(has_secret)