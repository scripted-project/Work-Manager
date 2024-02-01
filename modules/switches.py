class Switch:
    def __init__(self, value):
        self.value = value
        self.cases = {}
        self.default_case = None
    def case(self, case_value):
        def decorator(func):
            self.cases[case_value] = func
            return func
        return decorator
    def default(self, func):
        self.default_case = func
        return func
    def execute(self):
        func = self.cases.get(self.value, self.default_case)
        return func