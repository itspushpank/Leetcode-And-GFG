class Solution:
    def romanToInt(self, s: str) -> int:
        char = list(s)
        rom = 0
        for i in range(len(s)):
            rom += 1 if char[i] == 'I' else 5 if char[i] == 'V' else 10 if char[i] == 'X' else 50 if char[i] == 'L' else 100 if char[i] == 'C' else 500 if char[i] == 'D' else 1000 if char[i] == 'M' else 0

        rom -= (s.count("IV") + s.count("IX")) * 2  
        rom -= (s.count("XL") + s.count("XC"))  * 20 
        rom -= (s.count("CD") + s.count("CM")) * 200  

        return rom    

