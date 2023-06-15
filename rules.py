class Rules(object):
    def __new__(cls):
        inst = super(Rules, cls).__new__(cls)
        if not hasattr(cls, 'instance'):
            cls.instance = super(Rules, cls).__new__(cls)
            inst.rules = {}
        return cls.instance

    # def __init__(self) -> None:
    #     self.rules = {}

    def update_rules(self, rules: dict) -> None:
        self.rules = rules

    def get_rules(self) -> dict:
        return self.rules
    