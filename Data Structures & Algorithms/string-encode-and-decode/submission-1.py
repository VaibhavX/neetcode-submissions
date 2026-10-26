class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            # print(s)
            encoded_string = encoded_string+ str(len(s))+"#"+s
        
        # print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        return_list = []
        i = 0
        while(i < len(s)):
            j = s.find("#", i)
            slice = int(s[i:j])
            item = s[j+1:j+slice+1]
            return_list.append(item)
            i = j+1+slice
        
        return return_list
