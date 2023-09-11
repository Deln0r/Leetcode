lass Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        res = []
        for idx, num in enumerate(groupSizes):
            if len(groups[num]) == num:
                    res.append(groups[num])
                    groups[num] = [idx]
            else:
                groups[num].append(idx)
                
        res.extend(groups.values())
        return res
