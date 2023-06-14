class Rules:
    def __init__(self) -> None:
        self.rules = {}

    def update_rules(self, rules: dict) -> None:
        self.rules = rules

    def get_rules(self) -> dict:
        return self.rules

rules = Rules()