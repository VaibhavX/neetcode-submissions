class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_table = {}
        final_list = []

        for item in strs:
            ordered_string = "".join(sorted(item))
            # print(ordered_string)
            if ordered_string in hash_table:
                hash_table[ordered_string].append(item)
            else:
                hash_table[ordered_string] = [item]
        
        for sublist in hash_table.values():
            final_list.append(sublist)
        
        return final_list
            
        