class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for item in strs:
            length = len(item)
            encoded_string = encoded_string+str(length)+"#"+item+"#"
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_string = []
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            
            length = int(s[i:j])

            word = s[j+1:j+1+length]
            decoded_string.append(word)

            i = j+1+length+1
        
        return decoded_string
                
