def removeDuplicates(nums):
        len1 = len(nums)
        new_set = set(nums)
        k = len(new_set)
        new_list = list(new_set)
        new_list.append(_)
        return k, new_list

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
