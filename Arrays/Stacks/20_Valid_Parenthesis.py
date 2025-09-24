class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "()"
    print(f"Input: '{s1}'")
    print(f"Valid: {solution.isValid(s1)}")
    print()
    
    s2 = "()[]{}"
    print(f"Input: '{s2}'")
    print(f"Valid: {solution.isValid(s2)}")
    print()
    
    s3 = "([{}])"
    print(f"Input: '{s3}'")
    print(f"Valid: {solution.isValid(s3)}")
    print()
    
    s4 = "(]"
    print(f"Input: '{s4}'")
    print(f"Valid: {solution.isValid(s4)}")
    print()
    
    s5 = ")("
    print(f"Input: '{s5}'")
    print(f"Valid: {solution.isValid(s5)}")
    print()
    
    s6 = "((("
    print(f"Input: '{s6}'")
    print(f"Valid: {solution.isValid(s6)}")
    print()
    
    s7 = "{[()()]}"
    print(f"Input: '{s7}'")
    print(f"Valid: {solution.isValid(s7)}")
    print()
    
    s8 = "())"
    print(f"Input: '{s8}'")
    print(f"Valid: {solution.isValid(s8)}")
    print()
    
    s9 = ""
    print(f"Input: '{s9}'")
    print(f"Valid: {solution.isValid(s9)}")
    print()
    
    s10 = "["
    print(f"Input: '{s10}'")
    print(f"Valid: {solution.isValid(s10)}")