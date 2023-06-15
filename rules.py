class Rules(object):
    """ A singleton class to manage the active rules list. """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Rules, cls).__new__(cls)
            cls.instance.rules = {}
        return cls.instance

    def update_rules(self, rules: dict) -> None:
        """ Updates the active rule list
                
        :param rules: A list of rules for quota calculation
        :type rules: dict
        """
        self.rules = rules

    def get_rules(self) -> dict:
        """ Retrives the active rule list """
        return self.rules
    