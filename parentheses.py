import unittest


def isTextCorrect(text):

    open = '('
    close = ')'
    stack = []
    
    for s in text:
        if s == open:
            stack.append(s)
        elif s == close:
            if len(stack) == 0:
                return False
            else:
                last_item = stack.pop(-1)
                if last_item != open:
                    return False
    if len(stack) != 0:
        return False
    return True


class ParenthesesTests(unittest.TestCase):

    def testEmptyString(self):
        self.assertTrue(isTextCorrect(''))
        
    def testNoParentheses(self):
        self.assertTrue(isTextCorrect('abcdEFGH'))

    def testStartingParenthese(self):
        self.assertFalse(isTextCorrect('('))
        
    def testEndingParenthese(self):
        self.assertFalse(isTextCorrect(')'))
        
    def testMultipleParenthesesTrue1(self):
        self.assertTrue(isTextCorrect('(((())()()((())))())'))
        
    def testMultipleParenthesesTrue2(self):
        self.assertTrue(isTextCorrect('(ab()()()(()()())c(d()e)f)gh()'))
        
    def testMultipleParenthesesFalse1(self):
        self.assertFalse(isTextCorrect('(((()))()()((())))())'))
        
    def testMultipleParenthesesFalse2(self):
        self.assertFalse(isTextCorrect('(ab()()()(()()(())c(d()e)f)gh()'))        
        
def main():
    unittest.main()

    
if __name__ == '__main__':
    main()
    