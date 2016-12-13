class SmileChecker:
    def __init__(self):
        self.a = []
    def append_smile(self, s):
            self.a.append(s)

    def check_correct(self):
        left = [':-(', ':-[', ':-{', ':-<']
        right = [':-)', ':-]', ':-}', ':->']
        couple = dict(zip(right, left))
        b = []
        for bracket in self.a:
            if bracket in left:
                b.append(bracket)
            elif bracket in right:
                if b == []:
                    return False
                if b[-1] != couple[bracket]:
                    return False
                else:
                    b.pop()
        if b == []:
            return True
        else:
            return False