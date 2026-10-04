class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for brackets in s:
            if (brackets == "(" or brackets == "{" or brackets == "[" ):
                stack.append(brackets)
            else:
                if len(stack) == 0:
                    return False
                check = stack.pop()
                
                if ( (brackets == ")" and check == "(") or (brackets == "}" and check == "{") or (brackets == "]" and check == "[") ):
                    continue
                else:
                    return False   

        return len(stack) == 0





# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         bracks = {"(": ")", "[": "]", "{": "}"}
        
#         for i in s:
#             if i in bracks:
#                 stack.append(bracks[i])
#             else:
#                 if not stack or stack[-1] != i:
#                     return False
#                 stack.pop()
                
#         return not stack



