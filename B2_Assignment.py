#Built-In Function
#Q.1 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         s = s.strip()

         last_space = s.rfind(' ')

    
         if last_space == -1:
             return len(s)

  
         return len(s[last_space + 1:])
        
#Q.2 
    
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


#Simulation 
#Q.3 

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
             if op.isdigit() or (op[0] == '-' and op[1:].isdigit()):
            
                 stack.append(int(op))
             elif op == '+':
            
                 stack.append(stack[-1] + stack[-2])
             elif op == 'D':
            
                 stack.append(2 * stack[-1])
             elif op == 'C':
            
                 stack.pop()

   
        return sum(stack)

#Q.4 

class Solution:
    def judgeCircle(self, moves: str) -> bool:
         vertical = horizontal = 0

         for move in moves:
             if move == 'U':
                 vertical += 1
             elif move == 'D':
                 vertical -= 1
             elif move == 'L':
                 horizontal += 1
             elif move == 'R':
                 horizontal -= 1

    
         return vertical == horizontal == 0

#Q.5
    
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' ']*3 for _ in range(3)]

        def check_winner(player):
        
             for i in range(3):
                  if all(grid[i][j] == player for j in range(3)) or all(grid[j][i] == player for j in range(3)):
                     return True

       
             if all(grid[i][i] == player for i in range(3)) or all(grid[i][2-i] == player for i in range(3)):
                 return True

             return False

        for i, (row, col) in enumerate(moves):
             player = 'A' if i % 2 == 0 else 'B'
             grid[row][col] = player

        if check_winner(player):
             return player

        return "Draw" if len(moves) == 9 else "Pending"

#Q.6

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 0  
   
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in instructions:
            if instruction == 'G':
           
                x += deltas[direction][0]
                y += deltas[direction][1]
            elif instruction == 'L':
           
                direction = (direction - 1) % 4
            elif instruction == 'R':
            
                direction = (direction + 1) % 4

    
        return (x, y) == (0, 0) or direction != 0

#Matrix
#Q.1

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)

        return max_wealth
        
#Q.2

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
         n = len(mat)
         diagonal_sum = 0

    
         for i in range(n):
             diagonal_sum += mat[i][i]

    
         for i in range(n):
             diagonal_sum += mat[i][n - 1 - i]

    
         if n % 2 == 1:
             diagonal_sum -= mat[n // 2][n // 2]

         return diagonal_sum

#Q.3
    
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
        
            for i in range(left, right + 1):
               result.append(matrix[top][i])
            top += 1

       
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

        
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

        
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

#Q.4 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()

   
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

    
        for row in rows:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

    
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0

#Math
#Q.1

class Solution:
    def countOdds(self, low: int, high: int) -> int:
         if low % 2 == 0:
            low += 1

         if high % 2 == 0:
            high -= 1

   
         count = (high - low) // 2 + 1

         return count

#Q.2 
    
class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)

   
        sum_excluding_min_max = sum(salary) - min_salary - max_salary

    
        count = len(salary) - 2

   
        average = sum_excluding_min_max / count

        return average
        
#Q.3 
    
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
         count_5 = 0
         count_10 = 0

         for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                count_10 += 1
                count_5 -= 1
            elif bill == 20:
                if count_10 > 0:
                    count_10 -= 1
                    count_5 -= 1
                else:
                    count_5 -= 3

       
            if count_5 < 0:
                return False

         return True
        
#Q.4
    
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]

        return 0
    
#Q.5
    
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        def calculate_slope(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            if x2 - x1 == 0:
                return float('inf')
            return (y2 - y1) / (x2 - x1)

        slope = calculate_slope(coordinates[0], coordinates[1])

        for i in range(2, len(coordinates)):
            current_slope = calculate_slope(coordinates[i - 1], coordinates[i])
            if current_slope != slope:
                return False

        return True

#Q.6 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

   
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))

   
        for i in range(len(a) - 1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

    
        if carry:
            result.append(str(carry))

    
        return ''.join(result[::-1])

#Q.7 
    
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))

    
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
           
                product = int(num1[i]) * int(num2[j])
                temp_sum = result[i + j + 1] + product
                result[i + j + 1] = temp_sum % 10
                result[i + j] += temp_sum // 10

    
        result_str = ''.join(map(str, result))
        result_str = result_str.lstrip('0')

    
        return result_str if result_str else "0"


#Q.8


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

   
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

   
        while n > 0:
       
            if n % 2 != 0:
                result *= x
            x *= x  
            n //= 2  

        return result
 