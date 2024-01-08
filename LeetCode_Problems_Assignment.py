#Question 1
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
          result.append(word1[i])
          result.append(word2[j])
          i += 1
          j += 1

         # Append remaining letters from word1, if any
        while i < len(word1):
          result.append(word1[i])
          i += 1

         # Append remaining letters from word2, if any
        while j < len(word2):
          result.append(word2[j])
          j += 1

        return ''.join(result)
    
#Question 2
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
         char_count = {}

    
         for char in s:
            char_count[char] = char_count.get(char, 0) + 1

   
         for char in t:
            if char in char_count:
               char_count[char] -= 1
               if char_count[char] == 0:
                  del char_count[char]
            else:
                return char  

#Question 3 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
          return 0

    
        for i in range(len(haystack) - len(needle) + 1):
        
            if haystack[i:i+len(needle)] == needle:
               return i  
        return -1  

#Question 4 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#Question 5
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)

        for substring_len in range(1, length // 2 + 1):
        
            if length % substring_len == 0:
                substring = s[:substring_len]
                num_repeats = length // substring_len
                reconstructed_string = substring * num_repeats

           
                if reconstructed_string == s:
                    return True

        return False

#Question 6
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0

    
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

   
        while slow < len(nums):
            nums[slow] = 0
            slow += 1

#Question 7 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
         for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
            
                 digits[i] += 1
                 return digits
            else:
                 digits[i] = 0
    
   
         digits.insert(0, 1)
         return digits

#Question 8 
class Solution:
    def arraySign(self, nums: List[int]) -> int:
         product = 1

   
         for num in nums:
           product *= num

    
         if product > 0:
                return 1
         elif product < 0:
                return -1
         else:
                return 0

#Question 9 

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

   
        common_diff = arr[1] - arr[0]

    
        for i in range(1, len(arr) - 1):
             if arr[i + 1] - arr[i] != common_diff:
                return False

        return True

#Question 10 

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

   
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
               increasing = False
               break

    
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
                break


        return increasing or decreasing


#Question 11

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

        total = 0
        prev_value = 0

   
        for char in reversed(s):
            current_value = roman_dict[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

        
            prev_value = current_value

        return total


        
    